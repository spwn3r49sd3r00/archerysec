#                   _
#    /\            | |
#   /  \   _ __ ___| |__   ___ _ __ _   _
#  / /\ \ | '__/ __| '_ \ / _ \ '__| | | |
# / ____ \| | | (__| | | |  __/ |  | |_| |
#/_/    \_\_|  \___|_| |_|\___|_|   \__, |
#                                    __/ |
#                                   |___/
# Copyright (C) 2017-2018 ArcherySec
# This file is part of ArcherySec Project.

"""Author: Anand Tiwari """

import json
from django.core import signing


class SaveSettings:

    def __init__(self, setting_file):

        self.setting_file = setting_file

    def save_zap_settings(self, apikey, zaphost, zaport):
        """
        Save ZAP Settings into setting file.
        :param apikey:
        :param zaphost:
        :param zaport:
        :return:
        """
        try:
            with open(self.setting_file, 'r+') as f:
                sig_apikey = signing.dumps(apikey)
                data = json.load(f)
                data['zap_api_key'] = sig_apikey
                data['zap_path'] = str(zaphost)
                data['zap_port'] = zaport
                f.seek(0)
                json.dump(data, f, indent=4)
                f.truncate()
        except Exception as e:
            return e
        return f.close()

    def save_burp_settings(self, burphost, burport):
        """
        Save Burp Settings into setting file.
        :param burphost:
        :param burport:
        :return:
        """
        try:
            with open(self.setting_file, 'r+') as f:
                data = json.load(f)
                data['burp_path'] = burphost
                data['burp_port'] = burport
                f.seek(0)
                json.dump(data, f, indent=4)
                f.truncate()
        except Exception as e:
            return e
        return f.close()

    def openvas_settings(self, ipaddress, openvas_user, openvas_password):
        """
        Save OpenVAS Settings into Setting files.
        :param ipaddress:
        :param username:
        :param passwrod:
        :return:
        """
        try:
            with open(self.setting_file, 'r+') as f:
                sig_ov_user = signing.dumps(openvas_user)
                sig_ov_pass = signing.dumps(openvas_password)
                sig_ov_ip = signing.dumps(ipaddress)
                data = json.load(f)
                data['open_vas_user'] = sig_ov_user
                data['open_vas_pass'] = sig_ov_pass
                data['open_vas_ip'] = sig_ov_ip
                f.seek(0)
                json.dump(data, f, indent=4)
                f.truncate()

        except Exception as e:
            return e
        return f.close()

    def save_email_settings(self, email_subject, email_from, email_to):
        """

        :param email_subject:
        :param email_from:
        :param email_to:
        :return:
        """

        try:
            with open(self.setting_file, 'r+') as f:
                data = json.load(f)
                data['email_subject'] = email_subject
                data['from_email'] = email_from
                data['to_email'] = email_to
                f.seek(0)
                json.dump(data, f, indent=4)
                f.truncate()
        except Exception as e:
            return e
        return f.close()
