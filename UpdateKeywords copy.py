__author__ = 'BayramOld'


import pycurl
import json

import sys


SSLCERT_PATH = 'PATH TO SSL CERT'
SSLCERT_PWD = 'SSL CERT PASSWORD'
SEARCHADS_ORG_ID = 'SEARCH ADS ORG ID'


def batchStop(keywords):
    d = list()


    for kwd in keywords:
        keyword = {}
        keyword["text"] = kwd[1]
        keyword["campaignId"] = kwd[2]
        keyword["adGroupId"] = kwd[3]
        keyword["matchType"] = kwd[4]
        keyword["bidAmount"] = {"amount":""+str(0.3), "currency":"USD"}
        keyword["id"] = kwd[0]
        keyword["status"] = "PAUSED"
        keyword["importAction"] = "UPDATE"
        d.append(keyword)



    c = pycurl.Curl()

    url = "https://api.searchads.apple.com/api/v1/keywords/targeting"
    orgIdHeader = "Authorization: orgId="+SEARCHADS_ORG_ID

    c.setopt(pycurl.URL, url)
    c.setopt(pycurl.HTTPHEADER, [orgIdHeader,'Content-Type: application/json'])
    c.setopt(pycurl.POST, 1)
    c.setopt(pycurl.SSLCERTTYPE, 'p12')
    c.setopt(pycurl.SSLCERT,SSLCERT_PATH)
    c.setopt(pycurl.SSLKEYPASSWD,SSLCERT_PWD)
    c.setopt(pycurl.POSTFIELDS, json.dumps(d))
    with open("UpdateKeywordsResponse.json", "wb") as outfile:
        c.setopt(c.WRITEDATA, outfile)
        c.perform()


    with open('UpdateKeywordsResponse.json') as data_file:
        data = json.load(data_file)

    print(data)


def batchUpdate(keywords,amountToAdd,status):
    d = list()


    for kwd in keywords:
        keyword = {}
        keyword["text"] = kwd[1]
        keyword["campaignId"] = kwd[2]
        keyword["adGroupId"] = kwd[3]
        keyword["matchType"] = kwd[4]
        keyword["bidAmount"] = {"amount":""+str(kwd[5]+amountToAdd), "currency":"USD"}
        keyword["id"] = kwd[0]
        keyword["status"] = status
        keyword["importAction"] = "UPDATE"
        d.append(keyword)



    c = pycurl.Curl()

    url = "https://api.searchads.apple.com/api/v1/keywords/targeting"
    orgIdHeader = "Authorization: orgId="+SEARCHADS_ORG_ID

    c.setopt(pycurl.URL, url)
    c.setopt(pycurl.HTTPHEADER, [orgIdHeader,'Content-Type: application/json'])
    c.setopt(pycurl.POST, 1)
    c.setopt(pycurl.SSLCERTTYPE, 'p12')
    c.setopt(pycurl.SSLCERT,SSLCERT_PATH)
    c.setopt(pycurl.SSLKEYPASSWD,SSLCERT_PWD)
    c.setopt(pycurl.POSTFIELDS, json.dumps(d))
    with open("UpdateKeywordsResponse.json", "wb") as outfile:
        c.setopt(c.WRITEDATA, outfile)
        c.perform()


    with open('UpdateKeywordsResponse.json') as data_file:
        data = json.load(data_file)

    print(data)



def update(id,text,campaignId,adGroupId,matchType,bidAmount,status):

    with open("UpdateKeywords.json") as json_data:
        d = json.load(json_data)


    d[0]["text"] = text
    d[0]["campaignId"] = campaignId
    d[0]["adGroupId"] = adGroupId
    d[0]["matchType"] = matchType
    d[0]["bidAmount"]["amount"] = bidAmount
    d[0]["id"] = id
    d[0]["status"] = status

    print(d)

    c = pycurl.Curl()

    url = "https://api.searchads.apple.com/api/v1/keywords/targeting"
    orgIdHeader = "Authorization: orgId="+SEARCHADS_ORG_ID

    c.setopt(pycurl.URL, url)
    c.setopt(pycurl.HTTPHEADER, [orgIdHeader,'Content-Type: application/json'])
    c.setopt(pycurl.POST, 1)
    c.setopt(pycurl.SSLCERTTYPE, 'p12')
    c.setopt(pycurl.SSLCERT,SSLCERT_PATH)
    c.setopt(pycurl.SSLKEYPASSWD,SSLCERT_PWD)
    c.setopt(pycurl.POSTFIELDS, json.dumps(d))
    with open("UpdateKeywordsResponse.json", "wb") as outfile:
        c.setopt(c.WRITEDATA, outfile)
        c.perform()


    with open('UpdateKeywordsResponse.json') as data_file:
        data = json.load(data_file)

    print(data)

def createNegative(text,campaignId,adGroupId,matchType):

    with open("CreateNegativeKeywords.json") as json_data:
        d = json.load(json_data)


    d[0]["text"] = text
    d[0]["campaignId"] = campaignId
    d[0]["adGroupId"] = adGroupId
    d[0]["matchType"] = matchType


    print(str(d[0]["text"]))

    c = pycurl.Curl()

    url = "https://api.searchads.apple.com/api/v1/keywords/negative"
    orgIdHeader = "Authorization: orgId="+SEARCHADS_ORG_ID

    c.setopt(pycurl.URL, url)
    c.setopt(pycurl.HTTPHEADER, [orgIdHeader,'Content-Type: application/json'])
    c.setopt(pycurl.POST, 1)
    c.setopt(pycurl.SSLCERTTYPE, 'p12')
    c.setopt(pycurl.SSLCERT,SSLCERT_PATH)
    c.setopt(pycurl.SSLKEYPASSWD,SSLCERT_PWD)
    c.setopt(pycurl.POSTFIELDS, json.dumps(d))
    with open("UpdateKeywordsResponse.json", "wb") as outfile:
        c.setopt(c.WRITEDATA, outfile)
        c.perform()

    with open('UpdateKeywordsResponse.json') as data_file:
        data = json.load(data_file)

    print(data)



def create(text,campaignId,adGroupId,matchType,bidAmount):

    with open("CreateKeywords.json") as json_data:
        d = json.load(json_data)


    d[0]["text"] = text
    d[0]["campaignId"] = campaignId
    d[0]["adGroupId"] = adGroupId
    d[0]["matchType"] = matchType
    d[0]["bidAmount"]["amount"] = bidAmount


    print(d)

    c = pycurl.Curl()

    url = "https://api.searchads.apple.com/api/v1/keywords/targeting"
    orgIdHeader = "Authorization: orgId="+SEARCHADS_ORG_ID

    c.setopt(pycurl.URL, url)
    c.setopt(pycurl.HTTPHEADER, [orgIdHeader,'Content-Type: application/json'])
    c.setopt(pycurl.POST, 1)
    c.setopt(pycurl.SSLCERTTYPE, 'p12')
    c.setopt(pycurl.SSLCERT,SSLCERT_PATH)
    c.setopt(pycurl.SSLKEYPASSWD,SSLCERT_PWD)
    c.setopt(pycurl.POSTFIELDS, json.dumps(d))
    with open("UpdateKeywordsResponse.json", "wb") as outfile:
        c.setopt(c.WRITEDATA, outfile)
        c.perform()


    with open('UpdateKeywordsResponse.json') as data_file:
        data = json.load(data_file)

    print(data)

def stop(id,text,campaignId,adGroupId,matchType,bidAmount):
    update(id,text,campaignId,adGroupId,matchType,bidAmount,"PAUSED")

if __name__ == '__main__':
    update(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6],sys.argv[7])




