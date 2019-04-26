# -*- coding: utf-8 -*-
#                    _
#     /\            | |
#    /  \   _ __ ___| |__   ___ _ __ _   _
#   / /\ \ | '__/ __| '_ \ / _ \ '__| | | |
#  / ____ \| | | (__| | | |  __/ |  | |_| |
# /_/    \_\_|  \___|_| |_|\___|_|   \__, |
#                                     __/ |
#                                    |___/
# Copyright (C) 2017 Anand Tiwari
#
# Email:   anandtiwarics@gmail.com
# Twitter: @anandtiwarics
#
# This file is part of ArcherySec Project.

from django.shortcuts import render, render_to_response, HttpResponse, HttpResponseRedirect
from compliance.models import inspec_scan_db, inspec_scan_results_db
import hashlib
from staticscanners.resources import InspecResource


def inspec_list(request):
    """
    inspec Scan list.
    :param request:
    :return:
    """
    all_inspec_scan = inspec_scan_db.objects.all()

    return render(request, 'inspec/inspecscans_list.html',
                  {'all_inspec_scan': all_inspec_scan})


def list_vuln(request):
    all_failed = ''
    all_passed = ''
    all_skipped = ''

    if request.method == 'GET':
        scan_id = request.GET['scan_id']
    else:
        scan_id = None

    inspec_all_vuln = inspec_scan_results_db.objects.filter(scan_id=scan_id).values(
        'controls_id',
        'controls_title',
        'controls_tags_severity',
        'controls_tags_audit',
        'controls_tags_fix',
    ).distinct()
    inspec_all_audit = inspec_scan_results_db.objects.filter(scan_id=scan_id)

    all_compliance = inspec_scan_db.objects.filter(scan_id=scan_id)

    return render(request, 'inspec/inspecscan_list_vuln.html',
                  {'inspec_all_vuln': inspec_all_vuln,
                   'inspec_all_audit': inspec_all_audit,
                   'all_compliance': all_compliance

                   }
                  )


def inspec_vuln_data(request):
    """
    :param request:
    :return:
    """
    if request.method == 'GET':
        scan_id = request.GET['scan_id']
        vuln_id = request.GET['vuln_id']
    else:
        scan_id = None
        vuln_id = None

    if request.method == "POST":
        false_positive = request.POST.get('false')
        status = request.POST.get('status')
        vuln_id = request.POST.get('vuln_id')
        scan_id = request.POST.get('scan_id')
        inspec_scan_results_db.objects.filter(vuln_id=vuln_id,
                                              scan_id=scan_id).update(false_positive=false_positive,
                                                                      vuln_status=status)

        if false_positive == 'Yes':
            vuln_info = inspec_scan_results_db.objects.filter(scan_id=scan_id, vuln_id=vuln_id)
            for vi in vuln_info:
                Name = vi.Name
                NamespaceName = vi.NamespaceName
                Severity = vi.Severity
                dup_data = Name + Severity + NamespaceName
                false_positive_hash = hashlib.sha256(dup_data.encode('utf-8')).hexdigest()
                inspec_scan_results_db.objects.filter(vuln_id=vuln_id,
                                                      scan_id=scan_id).update(false_positive=false_positive,
                                                                              vuln_status=status,
                                                                              false_positive_hash=false_positive_hash
                                                                              )

        return HttpResponseRedirect(
            '/inspec/inspec_vuln_data/?scan_id=%s&test_name=%s' % (scan_id, vuln_id))

    # inspec_vuln_data = inspec_scan_results_db.objects.filter(
    #     scan_id=scan_id,
    #     name=test_name
    # )

    inspec_vuln_data = inspec_scan_results_db.objects.filter(scan_id=scan_id,
                                                             vuln_id=vuln_id,
                                                             vuln_status='Open',
                                                             false_positive='No'
                                                             )

    vuln_data_closed = inspec_scan_results_db.objects.filter(scan_id=scan_id,
                                                             vuln_id=vuln_id,
                                                             vuln_status='Closed',
                                                             false_positive='No')
    false_data = inspec_scan_results_db.objects.filter(scan_id=scan_id,
                                                       vuln_id=vuln_id,
                                                       false_positive='Yes')

    return render(request, 'inspec/inspecscan_vuln_data.html',
                  {'inspec_vuln_data': inspec_vuln_data,
                   'false_data': false_data,
                   'vuln_data_closed': vuln_data_closed
                   })


def inspec_details(request):
    """

    :param request:
    :return:
    """

    if request.method == 'GET':
        scan_id = request.GET['scan_id']
        vuln_id = request.GET['vuln_id']
    else:
        scan_id = None
        vuln_id = None

    inspec_vuln_details = inspec_scan_results_db.objects.filter(
        scan_id=scan_id,
        vuln_id=vuln_id
    )

    return render(request, 'inspec/inspec_vuln_details.html',
                  {'inspec_vuln_details': inspec_vuln_details,
                   }
                  )


def del_inspec(request):
    """
    Delete inspec Scans.
    :param request:
    :return:
    """
    if request.method == 'POST':
        scan_id = request.POST.get("scan_id")
        scan_item = str(scan_id)
        value = scan_item.replace(" ", "")
        value_split = value.split(',')
        split_length = value_split.__len__()
        # print "split_length", split_length
        for i in range(0, split_length):
            scan_id = value_split.__getitem__(i)
            item = inspec_scan_db.objects.filter(scan_id=scan_id)
            item.delete()
            item_results = inspec_scan_results_db.objects.filter(scan_id=scan_id)
            item_results.delete()
        # messages.add_message(request, messages.SUCCESS, 'Deleted Scan')
        return HttpResponseRedirect('/inspec/inspec_list')


def inspec_del_vuln(request):
    """
    The function Delete the inspec Vulnerability.
    :param request:
    :return:
    """
    if request.method == 'POST':
        vuln_id = request.POST.get("del_vuln", )
        scan_id = request.POST.get("scan_id", )
        scan_item = str(vuln_id)
        value = scan_item.replace(" ", "")
        value_split = value.split(',')
        split_length = value_split.__len__()
        print("split_length"), split_length
        for i in range(0, split_length):
            vuln_id = value_split.__getitem__(i)
            delete_vuln = inspec_scan_results_db.objects.filter(vuln_id=vuln_id)
            delete_vuln.delete()
        all_inspec_data = inspec_scan_results_db.objects.filter(scan_id=scan_id)

        total_vul = len(all_inspec_data)
        total_high = len(all_inspec_data.filter(Severity="High"))
        total_medium = len(all_inspec_data.filter(Severity="Medium"))
        total_low = len(all_inspec_data.filter(Severity="Low"))
        total_duplicate = len(all_inspec_data.filter(vuln_duplicate='Yes'))

        inspec_scan_db.objects.filter(scan_id=scan_id).update(
            total_vuln=total_vul,
            SEVERITY_HIGH=total_high,
            SEVERITY_MEDIUM=total_medium,
            SEVERITY_LOW=total_low,
            total_dup=total_duplicate
        )

        return HttpResponseRedirect("/inspec/inspec_all_vuln/?scan_id=%s" % scan_id)


def export(request):
    """
    :param request:
    :return:
    """

    if request.method == 'POST':
        scan_id = request.POST.get("scan_id")
        report_type = request.POST.get("type")

        inspec_resource = InspecResource()
        queryset = inspec_scan_results_db.objects.filter(scan_id=scan_id)
        dataset = inspec_resource.export(queryset)
        if report_type == 'csv':
            response = HttpResponse(dataset.csv, content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="%s.csv"' % scan_id
            return response
        if report_type == 'json':
            response = HttpResponse(dataset.json, content_type='application/json')
            response['Content-Disposition'] = 'attachment; filename="%s.json"' % scan_id
            return response
        if report_type == 'yaml':
            response = HttpResponse(dataset.yaml, content_type='application/x-yaml')
            response['Content-Disposition'] = 'attachment; filename="%s.yaml"' % scan_id
            return response
