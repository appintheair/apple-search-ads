
import pycurl
from StringIO import StringIO
import json
from pprint import pprint
import sys

SSLCERT_PATH = #PATH to certificate file
SSLCERT_PWD = #Password to certificate
SEARCHADS_ORG_ID = #Organization id


with open("GetSearchTermsData.json") as json_data:
    d = json.load(json_data)

c = pycurl.Curl()

url = "https://api.searchads.apple.com/api/v1/reports/campaigns/" + sys.argv[1] + "/searchterms"
orgIdHeader = "Authorization: orgId="+SEARCHADS_ORG_ID

c.setopt(pycurl.URL, url)
c.setopt(pycurl.HTTPHEADER, [orgIdHeader,'Content-Type: application/json'])
c.setopt(pycurl.POST, 1)
c.setopt(pycurl.SSLCERTTYPE, 'p12')
c.setopt(pycurl.SSLCERT,SSLCERT_PATH)
c.setopt(pycurl.SSLKEYPASSWD,SSLCERT_PWD)
c.setopt(pycurl.POSTFIELDS, json.dumps(d))
with open("GetSearchTermsDataResponse.json", "w") as outfile:
    c.setopt(c.WRITEFUNCTION, outfile.write)
    c.perform()





