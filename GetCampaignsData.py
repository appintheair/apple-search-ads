import pycurl
from StringIO import StringIO
import json
from pprint import pprint

SSLCERT_PATH = #Path to certificate
SSLCERT_PWD = #Password to certificate
SEARCHADS_ORG_ID = #Organization ID

with open("GetCampaignsData.json") as json_data:
    d = json.load(json_data)

c = pycurl.Curl()
c.setopt(pycurl.URL, "https://api.searchads.apple.com/api/v1/reports/campaigns")
orgIdHeader = "Authorization: orgId="+SEARCHADS_ORG_ID
c.setopt(pycurl.HTTPHEADER, [orgIdHeader,'Content-Type: application/json'])
c.setopt(pycurl.POST, 1)
c.setopt(pycurl.SSLCERTTYPE, 'p12')
c.setopt(pycurl.SSLCERT,SSLCERT_PATH)
c.setopt(pycurl.SSLKEYPASSWD,SSLCERT_PWD)
c.setopt(pycurl.POSTFIELDS, json.dumps(d))
with open("GetCampaignsDataResponse.json", "w") as outfile:
    c.setopt(c.WRITEFUNCTION, outfile.write)
    c.perform()






