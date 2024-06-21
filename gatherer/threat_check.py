import requests
import json

def check_threat_intelligence(ips):
    threat_reports = {}
    url = 'https://api.abuseipdb.com/api/v2/check'
    for ip in ips:
        querystring = {
            'ipAddress': ip,
            'maxAgeInDays': '90'
        }

        headers = {
            'Accept': 'application/json',
            'Key': '02eaa00fa1674173079dbdbb92f65a48bceeee0d16f188cd7cd8f72b1b77c8a4c0ae35aeca0d4010'
        }

        response = requests.request(method='GET', url=url, headers=headers, params=querystring)
        decodedResponse = json.loads(response.text)

        threat_reports[ip] = decodedResponse
    return threat_reports
