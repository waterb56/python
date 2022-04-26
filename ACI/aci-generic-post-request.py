import urllib3
import json
import requests

username = input('username: ')
password = input('password: ')
apic = 'sandboxapicdc.cisco.com'
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
url = f"https://{apic}/api/aaaLogin.json"
payloadDict = {
    "aaaUser": {
        "attributes": {
            "name": username,
            "pwd": password
        }
    }
}
payloadJson = json.dumps(payloadDict)
header = {
    'Content-Type': 'application/json',
}
token = requests.post(url, verify=False, data=payloadJson, headers=header, auth=(username, password))
tokenJson = token.json()
imdata = tokenJson['imdata']
imdataDict = imdata[0]
aaaLogin = imdataDict['aaaLogin']
attribute = aaaLogin['attributes']
token = attribute['token']

# Post url and payload below
url = 'generic url'
payload = 'generic payload'

# Execute POST
header = {
    'Cookie': f'APIC-cookie={token}',
    'Authorization': 'Bearer' + ' ' + token
}
request = requests.post(url, headers=header, data=payload, verify=False)
response = request.status_code
print(response)