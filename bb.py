#!/usr/bin/python3

import sys
import urllib.parse
import http.client
import json
from enum import Enum

bucketkey = "jn7Py6A4XXaXY6FLS9"
bucketsecret = "EDfSJfKU8UGkQCeGNYks9tShsqWR8QRT"
# "https://bitbucket.org/site/oauth2/authorize?client_id=%s&response_type=code" % bucketkey
# でcodeをもらってくる
code="BRFMz9UyrGcJEaGDMx"
#curl -X POST -u "client_id:secret" \
#  https://bitbucket.org/site/oauth2/access_token \
#  -d grant_type=authorization_code -d code={code}
# でaccess tokenにかえる
# 一時間で有効切れになるのでreferesh tokenも保存しておく

# headerに足す
# Authorization: Brearer access_token

# main :: IO Int
def main():
    args = sys.argv[1:]
    useragent = "gitHost"
    getBucketRepos("octaltree")
    return 0

def getBucketRepos(owner):
    method = "GET"
    hostname = "api.bitbuket.org"
    endpoint = "/2.0/repositories"
    path = endpoint + "/%s" % owner
    url = urllib.parse.urlunparse(("", "", path, "", "", ""))
    header = {
            "User-Agent": "getHost"}
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
