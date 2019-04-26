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

from __future__ import unicode_literals

from django.db import models


class zap_spider_db(models.Model):
    spider_url = models.TextField(blank=True)
    spider_scanid = models.TextField(blank=True)
    urls_num = models.TextField(blank=True)


class zap_scans_db(models.Model):
    scan_url = models.URLField(blank=True)
    scan_scanid = models.TextField(blank=True)
    rescan_id = models.TextField(blank=True, null=True)
    vul_num = models.TextField(blank=True)
    vul_status = models.TextField(blank=True)
    total_vul = models.IntegerField(blank=True, null=True)
    high_vul = models.IntegerField(blank=True, null=True)
    medium_vul = models.IntegerField(blank=True, null=True)
    low_vul = models.IntegerField(blank=True, null=True)
    info_vul = models.IntegerField(blank=True, null=True)
    project_id = models.UUIDField(null=True)
    date_time = models.DateTimeField(null=True)
    rescan = models.TextField(blank=True, null=True)
    total_dup = models.TextField(blank=True, null=True)


class zap_spider_results(models.Model):
    spider_id = models.TextField(blank=True)
    spider_urls = models.TextField(blank=True)


class zap_scan_results_db(models.Model):
    vuln_id = models.TextField(blank=True)
    scan_id = models.TextField(blank=True)
    rescan_id = models.TextField(blank=True, null=True)
    confidence = models.TextField(blank=True)
    wascid = models.TextField(blank=True)
    cweid = models.TextField(blank=True)
    risk = models.TextField(blank=True)
    reference = models.TextField(blank=True)
    url = models.TextField(blank=True)
    name = models.TextField(blank=True)
    solution = models.TextField(blank=True)
    param = models.TextField(blank=True)
    evidence = models.TextField(blank=True)
    sourceid = models.TextField(blank=True)
    pluginId = models.TextField(blank=True)
    other = models.TextField(blank=True)
    attack = models.TextField(blank=True)
    messageId = models.TextField(blank=True)
    method = models.TextField(blank=True)
    alert = models.TextField(blank=True)
    ids = models.TextField(blank=True)
    description = models.TextField(blank=True)
    req_res = models.TextField(blank=True)
    project_id = models.TextField(blank=True)
    vuln_color = models.TextField(blank=True)
    rescan = models.TextField(blank=True, null=True)
    note = models.TextField(blank=True)
    rtt = models.TextField(blank=True)
    tags = models.TextField(blank=True)
    timestamp = models.TextField(blank=True)
    responseHeader = models.TextField(blank=True)
    requestBody = models.TextField(blank=True)
    responseBody = models.TextField(blank=True)
    requestHeader = models.TextField(blank=True)
    cookieParams = models.TextField(blank=True)
    res_type = models.TextField(blank=True)
    res_id = models.TextField(blank=True)
    date_time = models.DateTimeField(null=True)
    false_positive = models.TextField(null=True, blank=True)
    jira_ticket = models.TextField(null=True, blank=True)
    vuln_status = models.TextField(null=True, blank=True)
    dup_hash = models.TextField(null=True, blank=True)
    vuln_duplicate = models.TextField(null=True, blank=True)
    false_positive_hash = models.TextField(null=True, blank=True)
    scanner = models.TextField(default='ZAP Scanner', editable=False)


class cookie_db(models.Model):
    url = models.TextField(blank=True)
    cookie = models.TextField(blank=True)


class excluded_db(models.Model):
    exclude_url = models.TextField(blank=True)


class burp_scan_db(models.Model):
    url = models.URLField(blank=True)
    scan_id = models.UUIDField(blank=True)
    rescan_id = models.TextField(blank=True, null=True)
    scan_date = models.TextField(blank=True)
    scan_status = models.TextField(blank=True)
    project_id = models.UUIDField(blank=True)
    total_vul = models.IntegerField(blank=True, null=True)
    high_vul = models.IntegerField(blank=True, null=True)
    medium_vul = models.IntegerField(blank=True, null=True)
    low_vul = models.IntegerField(blank=True, null=True)
    info_vul = models.IntegerField(blank=True, null=True)
    date_time = models.DateTimeField(blank=True, null=True)
    rescan = models.TextField(blank=True, null=True)
    total_dup = models.TextField(blank=True, null=True)


class burp_scan_result_db(models.Model):
    scan_id = models.UUIDField(blank=True)
    rescan_id = models.TextField(blank=True, null=True)
    project_id = models.TextField(blank=True)
    vuln_id = models.TextField(blank=True)
    rescan = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    remediation = models.TextField(blank=True, null=True)
    reference = models.TextField(blank=True, null=True)
    vulnerability_classifications = models.TextField(blank=True, null=True)
    path = models.TextField(blank=True, null=True)
    type_index = models.TextField(blank=True, null=True)
    serial_number = models.TextField(blank=True, null=True)
    origin = models.TextField(blank=True, null=True)
    severity = models.TextField(blank=True, null=True)
    confidence = models.TextField(blank=True, null=True)
    caption = models.TextField(blank=True, null=True)
    request_response_url = models.TextField(blank=True, null=True)
    request_response_request_type = models.TextField(blank=True, null=True)
    request_response_request_data = models.TextField(blank=True, null=True)
    request_response_response_type = models.TextField(blank=True, null=True)
    request_response_response_data = models.TextField(blank=True, null=True)
    was_redirect_followed = models.TextField(blank=True, null=True)
    request_time = models.TextField(blank=True, null=True)
    internal_data = models.TextField(blank=True, null=True)
    false_positive = models.TextField(null=True, blank=True)
    jira_ticket = models.TextField(null=True, blank=True)
    vuln_status = models.TextField(null=True, blank=True)
    dup_hash = models.TextField(null=True, blank=True)
    vuln_duplicate = models.TextField(null=True, blank=True)
    false_positive_hash = models.TextField(null=True, blank=True)
    scanner = models.TextField(default='Burp Scanner', editable=False)
    severity_color = models.TextField(null=True, blank=True)


class burp_issue_definitions(models.Model):
    remediation = models.TextField(blank=True, null=True)
    issue_type_id = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    reference = models.TextField(blank=True, null=True)
    vulnerability_classifications = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)


class netsparker_scan_db(models.Model):
    url = models.URLField(blank=True)
    scan_id = models.UUIDField(blank=True)
    rescan_id = models.TextField(blank=True, null=True)
    scan_date = models.TextField(blank=True)
    scan_status = models.TextField(blank=True)
    project_id = models.UUIDField(blank=True)
    total_vul = models.IntegerField(blank=True, null=True)
    critical_vul = models.IntegerField(blank=True, null=True)
    high_vul = models.IntegerField(blank=True, null=True)
    medium_vul = models.IntegerField(blank=True, null=True)
    low_vul = models.IntegerField(blank=True, null=True)
    info_vul = models.IntegerField(blank=True, null=True)
    date_time = models.DateTimeField(blank=True, null=True)
    rescan = models.TextField(blank=True, null=True)
    total_dup = models.TextField(blank=True, null=True)


class netsparker_scan_result_db(models.Model):
    scan_id = models.UUIDField(blank=True)
    rescan_id = models.TextField(blank=True, null=True)
    project_id = models.TextField(blank=True)
    vuln_id = models.TextField(blank=True)
    rescan = models.TextField(blank=True, null=True)
    vuln_url = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    severity = models.TextField(blank=True, null=True)
    certainty = models.TextField(blank=True, null=True)
    rawrequest = models.TextField(blank=True, null=True)
    rawresponse = models.TextField(blank=True, null=True)
    extrainformation = models.TextField(blank=True, null=True)
    classification = models.TextField(blank=True, null=True)
    false_positive = models.TextField(null=True, blank=True)
    vuln_color = models.TextField(blank=True, null=True)
    jira_ticket = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    impact = models.TextField(null=True, blank=True)
    actionsToTake = models.TextField(null=True, blank=True)
    remedy = models.TextField(null=True, blank=True)
    requiredSkillsForExploitation = models.TextField(null=True, blank=True)
    externalReferences = models.TextField(null=True, blank=True)
    remedyReferences = models.TextField(null=True, blank=True)
    proofOfConcept = models.TextField(null=True, blank=True)
    proofs = models.TextField(null=True, blank=True)
    vuln_status = models.TextField(null=True, blank=True)
    dup_hash = models.TextField(null=True, blank=True)
    vuln_duplicate = models.TextField(null=True, blank=True)
    false_positive_hash = models.TextField(null=True, blank=True)
    scanner = models.TextField(default='Netsparker', editable=False)


class web_scan_db(models.Model):
    scan_url = models.URLField(blank=True)
    scan_id = models.UUIDField(blank=True)
    scan_date = models.TextField(blank=True)
    scan_status = models.TextField(blank=True)
    project_id = models.UUIDField(blank=True)
    total_vul = models.IntegerField(blank=True)
    high_vul = models.IntegerField(blank=True)
    medium_vul = models.IntegerField(blank=True)
    low_vul = models.IntegerField(blank=True)
    info_vuln = models.IntegerField(blank=True)
    scanner = models.TextField(blank=True)


class email_config_db(models.Model):
    email_id_from = models.EmailField(blank=True)
    email_subject = models.TextField(blank=True)
    email_message = models.TextField(blank=True)
    email_id_to = models.EmailField(blank=True)


class arachni_scan_db(models.Model):
    url = models.URLField(blank=True)
    scan_id = models.UUIDField(blank=True)
    rescan_id = models.TextField(blank=True, null=True)
    scan_date = models.TextField(blank=True)
    scan_status = models.TextField(blank=True)
    project_id = models.UUIDField(blank=True)
    total_vul = models.IntegerField(blank=True, null=True)
    high_vul = models.IntegerField(blank=True, null=True)
    medium_vul = models.IntegerField(blank=True, null=True)
    low_vul = models.IntegerField(blank=True, null=True)
    info_vul = models.IntegerField(blank=True, null=True)
    date_time = models.DateTimeField(blank=True, null=True)
    rescan = models.TextField(blank=True, null=True)
    total_dup = models.TextField(blank=True, null=True)


class arachni_scan_result_db(models.Model):
    scan_id = models.UUIDField(blank=True)
    rescan_id = models.TextField(blank=True, null=True)
    project_id = models.TextField(blank=True)
    vuln_id = models.TextField(blank=True)
    rescan = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True)
    description = models.TextField(blank=True)
    remedy_guidance = models.TextField(blank=True)
    severity = models.TextField(blank=True)
    proof = models.TextField(blank=True)
    vuln_color = models.TextField(blank=True)
    url = models.TextField(blank=True)
    action = models.TextField(blank=True)
    body = models.TextField(blank=True)
    false_positive = models.TextField(blank=True)
    cwe = models.TextField(blank=True)
    ref_key = models.TextField(blank=True)
    ref_value = models.TextField(blank=True)
    vector_input_key = models.TextField(blank=True)
    vector_input_values = models.TextField(blank=True)
    vector_source_key = models.TextField(blank=True)
    vector_source_values = models.TextField(blank=True)
    page_body_data = models.TextField(blank=True)
    request_url = models.TextField(blank=True)
    request_method = models.TextField(blank=True)
    request_raw = models.TextField(blank=True)
    response_ip = models.TextField(blank=True)
    response_raw_headers = models.TextField(blank=True)
    jira_ticket = models.TextField(null=True, blank=True)
    vuln_status = models.TextField(null=True, blank=True)
    dup_hash = models.TextField(null=True, blank=True)
    vuln_duplicate = models.TextField(null=True, blank=True)
    false_positive_hash = models.TextField(null=True, blank=True)
    scanner = models.TextField(default='Arachni', editable=False)


class task_schedule_db(models.Model):
    task_id = models.TextField(blank=True, null=True)
    target = models.TextField(blank=True, null=True)
    schedule_time = models.TextField(blank=True, null=True)
    project_id = models.TextField(blank=True, null=True)
    scanner = models.TextField(blank=True, null=True)
    periodic_task = models.TextField(blank=True, null=True)


class webinspect_scan_db(models.Model):
    url = models.URLField(blank=True)
    scan_id = models.UUIDField(blank=True)
    rescan_id = models.TextField(blank=True, null=True)
    scan_date = models.TextField(blank=True)
    scan_status = models.TextField(blank=True)
    project_id = models.UUIDField(blank=True)
    total_vul = models.IntegerField(blank=True, null=True)
    critical_vul = models.IntegerField(blank=True, null=True)
    high_vul = models.IntegerField(blank=True, null=True)
    medium_vul = models.IntegerField(blank=True, null=True)
    low_vul = models.IntegerField(blank=True, null=True)
    info_vul = models.IntegerField(blank=True, null=True)
    date_time = models.DateTimeField(blank=True, null=True)
    rescan = models.TextField(blank=True, null=True)
    total_dup = models.TextField(blank=True, null=True)


class webinspect_scan_result_db(models.Model):
    scan_id = models.UUIDField(blank=True)
    rescan_id = models.TextField(blank=True, null=True)
    project_id = models.TextField(blank=True)
    vuln_id = models.TextField(blank=True)
    rescan = models.TextField(blank=True, null=True)
    vuln_url = models.TextField(blank=True, null=True)
    false_positive = models.TextField(null=True, blank=True)
    vuln_color = models.TextField(blank=True, null=True)
    jira_ticket = models.TextField(null=True, blank=True)
    scheme = models.TextField(blank=True, null=True)
    host = models.TextField(blank=True, null=True)
    port = models.TextField(blank=True, null=True)
    attackmethod = models.TextField(blank=True, null=True)
    vulnerablesession = models.TextField(blank=True, null=True)
    triggerSession = models.TextField(blank=True, null=True)
    vulnerabilityID = models.TextField(blank=True, null=True)
    severity = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    reportSection = models.TextField(blank=True, null=True)
    highlightSelections = models.TextField(blank=True, null=True)
    rawResponse = models.TextField(blank=True, null=True)
    SectionText = models.TextField(blank=True, null=True)
    severity_name = models.TextField(blank=True, null=True)
    vuln_status = models.TextField(null=True, blank=True)
    dup_hash = models.TextField(null=True, blank=True)
    vuln_duplicate = models.TextField(null=True, blank=True)
    false_positive_hash = models.TextField(null=True, blank=True)
    scanner = models.TextField(default='Webinspect', editable=False)


class acunetix_scan_db(models.Model):
    url = models.URLField(blank=True)
    scan_id = models.UUIDField(blank=True)
    rescan_id = models.TextField(blank=True, null=True)
    scan_date = models.TextField(blank=True)
    scan_status = models.TextField(blank=True)
    project_id = models.UUIDField(blank=True)
    total_vul = models.IntegerField(blank=True, null=True)
    critical_vul = models.IntegerField(blank=True, null=True)
    high_vul = models.IntegerField(blank=True, null=True)
    medium_vul = models.IntegerField(blank=True, null=True)
    low_vul = models.IntegerField(blank=True, null=True)
    info_vul = models.IntegerField(blank=True, null=True)
    date_time = models.DateTimeField(blank=True, null=True)
    rescan = models.TextField(blank=True, null=True)
    total_dup = models.TextField(blank=True, null=True)


class acunetix_scan_result_db(models.Model):
    scan_id = models.UUIDField(blank=True)
    rescan_id = models.TextField(blank=True, null=True)
    project_id = models.TextField(blank=True)
    vuln_id = models.TextField(blank=True)
    rescan = models.TextField(blank=True, null=True)
    false_positive = models.TextField(null=True, blank=True)
    vuln_color = models.TextField(blank=True, null=True)
    jira_ticket = models.TextField(null=True, blank=True)
    vuln_status = models.TextField(null=True, blank=True)
    dup_hash = models.TextField(null=True, blank=True)
    vuln_duplicate = models.TextField(null=True, blank=True)
    false_positive_hash = models.TextField(null=True, blank=True)
    ScanName = models.TextField(null=True, blank=True)
    ScanShortName = models.TextField(null=True, blank=True)
    ScanStartURL = models.TextField(null=True, blank=True)
    ScanStartTime = models.TextField(null=True, blank=True)
    ScanFinishTime = models.TextField(null=True, blank=True)
    ScanScanTime = models.TextField(null=True, blank=True)
    ScanAborted = models.TextField(null=True, blank=True)
    ScanResponsive = models.TextField(null=True, blank=True)
    ScanBanner = models.TextField(null=True, blank=True)
    ScanOs = models.TextField(null=True, blank=True)
    ScanWebServer = models.TextField(null=True, blank=True)
    ScanTechnologies = models.TextField(null=True, blank=True)
    ScanCrawler = models.TextField(null=True, blank=True)
    ScanReportItems = models.TextField(null=True, blank=True)
    VulnName = models.TextField(null=True, blank=True)
    VulnModuleName = models.TextField(null=True, blank=True)
    VulnDetails = models.TextField(null=True, blank=True)
    VulnAffects = models.TextField(null=True, blank=True)
    VulnParameter = models.TextField(null=True, blank=True)
    VulnAOP_SourceFile = models.TextField(null=True, blank=True)
    VulnAOP_SourceLine = models.TextField(null=True, blank=True)
    VulnAOP_Additional = models.TextField(null=True, blank=True)
    VulnIsFalsePositive = models.TextField(null=True, blank=True)
    VulnSeverity = models.TextField(null=True, blank=True)
    VulnType = models.TextField(null=True, blank=True)
    VulnImpact = models.TextField(null=True, blank=True)
    VulnDescription = models.TextField(null=True, blank=True)
    VulnDetailedInformation = models.TextField(null=True, blank=True)
    VulnRecommendation = models.TextField(null=True, blank=True)
    VulnTechnicalDetails = models.TextField(null=True, blank=True)
    VulnCWEList = models.TextField(null=True, blank=True)
    VulnCVEList = models.TextField(null=True, blank=True)
    VulnCVSS = models.TextField(null=True, blank=True)
    VulnCVSS3 = models.TextField(null=True, blank=True)
    VulnReferences = models.TextField(null=True, blank=True)
    UriName = models.TextField(null=True, blank=True)
    VulnUrl = models.TextField(null=True, blank=True)
    VulnFullUrl = models.TextField(null=True, blank=True)
    scanner = models.TextField(default='Acunetix', editable=False)
