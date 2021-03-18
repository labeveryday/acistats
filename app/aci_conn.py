#!/usr/bin/env python
import json
import sys
import requests
from .credenitials import URL, USERNAME, PASSWORD


class iACI:
    def __init__(self, url=URL, username=USERNAME, password=PASSWORD):
        """POST logins into APIC and Returns Token
            Arguments:
                url: url of APIC
                username: APIC api username
                password: APIC api password
            type data: str
            return: Return the APIC token
            rtype: str
        """
        self.username = username
        self.password = password
        self.url = url
        self.token = self.get_token()

    def get_token(self):
        """POST logins into APIC and Returns Token
            return: Return the APIC token
            rtype: str
        """
        payload = {
            "aaaUser": {
                "attributes": {
                    "name": self.username,
                    "pwd": self.password
                    }
                }
            }
        headers = {"Content-Type": "application/json"}
        response = requests.request('POST', self.url + "/api/aaaLogin.json",
                                    headers=headers, json=payload)
        if response.status_code == 200:
            json_data = json.loads(response.text)
            return "APIC-cookie=" + json_data['imdata'][0]['aaaLogin']['attributes']['token']
        else:
            print(f"Login failed: {response.status_code}")
            sys.exit()

    def get_tenant(self):
        """GET created ACI tenants
            return: Return the APIC tenants
            rtype: dict
        """
        headers = {
            "Content-Type": "application/json",
            "Cookie": self.token
            }
        url = self.url + "/api/class/fvTenant.json"
        response = requests.request("GET", url, headers=headers)
        return json.loads(response.text)

    def get_subnet(self):
        """GET created ACI Subnets
            return: Return the APIC subnets
            rtype: dict
        """
        headers = {
            "Content-Type": "application/json",
            "Cookie": self.token
            }
        url = self.url + "/api/class/fvSubnet.json"
        response = requests.request("GET", url, headers=headers)
        return json.loads(response.text)

    def get_aci_health(self):
        """GET created ACI Fabric Health
            return: Return the APIC tenants
            rtype: dict
        """
        headers = {
            "Content-Type": "application/json",
            "Cookie": self.token
            }
        url = self.url + "/api/node/mo/topology/HDfabricOverallHealth5min-0.json"
        response = requests.request("GET", url, headers=headers)
        return json.loads(response.text)

    def get_aci_faultinfo(self):
        """GET created ACI Fabric Health
            type data: str
            return: Return the APIC tenants
            rtype: dict
        """
        headers = {
            "Content-Type": "application/json",
            "Cookie": self.token
            }
        url = (self.url + '/api/node/class/faultInfo.json?' +
            'query-target-filter=and(ne(faultInfo.severity,"cleared"))' +
            '&order-by=faultInfo.severity|desc&page=1&page-size=15')
        response = requests.request("GET", url, headers=headers)
        return json.loads(response.text)

    def get_crc_errors(self):
        headers = {
            "Content-Type": "application/json",
            "Cookie": self.token
            }
        url = (self.url + '/api/node/class/rmonEtherStats.json?' +
            'query-target-filter=and(gt(rmonEtherStats.cRCAlignErrors,"0")')
        response = requests.request("GET", url, headers=headers)
        return json.loads(response.text)
