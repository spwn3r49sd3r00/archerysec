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

from staticscanners.models import gitlabsca_scan_db, gitlabsca_scan_results_db
import uuid
import hashlib
from datetime import datetime
import json

from webscanners.zapscanner.views import email_sch_notify

vul_col = ''
Target = ''
VulnerabilityID = ''
PkgName = ''
InstalledVersion = ''
FixedVersion = ''
Title = ''
Description = ''
Severity = ''
References = ''


def gitlabsca_report_json(data, project_id, scan_id, username):
    """

    :param data:
    :param project_id:
    :param scan_id:
    :return:
    """

    vul_col = ''

    vuln = data['vulnerabilities']

    for vuln_data in vuln:
        try:
            name = vuln_data['name']
        except Exception as e:
            name = "Not Found"

        try:
            message = vuln_data['message']
        except Exception as e:
            message = "Not Found"

        try:
            description = vuln_data['description']
        except Exception as e:
            description = "Not Found"

        try:
            cve = vuln_data['cve']
        except Exception as e:
            cve = "Not Found"

        try:
            scanner = vuln_data['scanner']
        except Exception as e:
            scanner = "Not Found"

        try:
            location = vuln_data['location']
        except Exception as e:
            location = "Not Found"

        try:
            identifiers = vuln_data['identifiers']
        except Exception as e:
            identifiers = "Not Found"

        try:
            severity = vuln_data['severity']
        except Exception as e:
            severity = "Not Found"

        try:
            file = vuln_data['location']['file']
        except Exception as e:
            file = "Not Found"

        if severity == "Critical":
            severity = 'High'
            vul_col = "danger"

        elif severity == "High":
            vul_col = "danger"

        elif severity == 'Medium':
            vul_col = "warning"

        elif severity == 'Low':
            vul_col = "info"

        elif severity == 'Unknown':
            severity = "Low"
            vul_col = "info"

        elif severity == 'Everything else':
            severity = "Low"
            vul_col = "info"


        vul_id = uuid.uuid4()

        dup_data = message + severity + file

        duplicate_hash = hashlib.sha256(dup_data.encode('utf-8')).hexdigest()

        match_dup = gitlabsca_scan_results_db.objects.filter(username=username,
                                                             dup_hash=duplicate_hash).values('dup_hash')
        lenth_match = len(match_dup)

        if lenth_match == 1:
            duplicate_vuln = 'Yes'
        elif lenth_match == 0:
            duplicate_vuln = 'No'
        else:
            duplicate_vuln = 'None'

        false_p = gitlabsca_scan_results_db.objects.filter(username=username,
                                                           false_positive_hash=duplicate_hash)
        fp_lenth_match = len(false_p)

        if fp_lenth_match == 1:
            false_positive = 'Yes'
        else:
            false_positive = 'No'

        save_all = gitlabsca_scan_results_db(
            vuln_id=vul_id,
            scan_id=scan_id,
            project_id=project_id,
            name=name,
            message=message,
            description=description,
            cve=cve,
            gl_scanner=scanner,
            location=location,
            file=file,
            Severity=severity,
            identifiers=identifiers,
            vul_col=vul_col,
            vuln_status='Open',
            dup_hash=duplicate_hash,
            vuln_duplicate=duplicate_vuln,
            false_positive=false_positive,
            username=username,
        )
        save_all.save()

    all_findbugs_data = gitlabsca_scan_results_db.objects.filter(username=username, scan_id=scan_id,
                                                                 false_positive='No')

    total_vul = len(all_findbugs_data)
    total_high = len(all_findbugs_data.filter(Severity="High"))
    total_medium = len(all_findbugs_data.filter(Severity="Medium"))
    total_low = len(all_findbugs_data.filter(Severity="Low"))
    total_duplicate = len(all_findbugs_data.filter(vuln_duplicate='Yes'))

    gitlabsca_scan_db.objects.filter(scan_id=scan_id).update(username=username,
                                                             total_vuln=total_vul,
                                                             SEVERITY_HIGH=total_high,
                                                             SEVERITY_MEDIUM=total_medium,
                                                             SEVERITY_LOW=total_low,
                                                             total_dup=total_duplicate
                                                             )
    subject = 'Archery Tool Scan Status - GitLab Dependency Report Uploaded'
    message = 'GitLab Dependency Scanner has completed the scan ' \
              '  %s <br> Total: %s <br>High: %s <br>' \
              'Medium: %s <br>Low %s' % (Target, total_vul, total_high, total_medium, total_low)

    email_sch_notify(subject=subject, message=message)
