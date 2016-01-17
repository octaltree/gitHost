#!/usr/bin/python3

import sys
import urllib.parse
import http.client
import json
from enum import Enum

bucketkey = "jn7Py6A4XXaXY6FLS9"
bucketsecret = "EDfSJfKU8UGkQCeGNYks9tShsqWR8QRT"
# "https://bitbucket.org/site/oauth2/authorize?client_id=%s&response_type=code" % bucketkey
# でapi tokenをもらってくる
buckettoken="BRFMz9UyrGcJEaGDMx"

# main :: IO Int
def main():
    args = sys.argv[1:]

    useragent = "gitHost"
    method = "GET"
    hostname = "bitbucket.org"
    path = "/site/oauth2/authorize"
    query = urllib.parse.urlencode({
        "client_id": bucketkey,
        "response_type": "code"})
    header = {
            "User-Agent": useragent}
    url = urllib.parse.urlunparse(("", "", path, "", query, ""))
    #conn = http.client.HTTPSConnection(hostname)
    #conn.request(method, url, headers = header)
    #response = conn.getresponse()
    #print(response.read())
    #print(str(response.status) + "  " + response.reason)
    getBucketRepos()
    return 0

def getBucketRepos():
    hostname = "api.bitbuket.org"
    pathbase = "/2.0/repositories"
    path = pathbase + "/octaltree"
    url = urllib.parse.urlunparse(("", "", path, "", "", ""))
    header = {
            "User-Agent": "getHost"}
    method = "GET"

    print(url)
    conn = http.client.HTTPSConnection(hostname)
    conn.request(method, url, headers = header)
    response = conn.getresponse()
    print(response.read())
    print(str(response.status) + "  " + response.reason)



# undefined :: a
undefined = None

if __name__ == "__main__" :
  exit(main())

# vim:fenc=utf-8 ff=unix ft=python ts=4 sw=4 sts=4 si et fdm=indent fdl=0 fdn=1:
# vim:cinw=if,elif,else,for,while,try,except,finally,def,class:
