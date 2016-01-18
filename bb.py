#!/usr/bin/python3

import sys
import urllib.parse
import urllib.request
import http.client
import json
from enum import Enum

bucketkey="Ev4c4krDQqHyRd2XH6"
bucketsecret="TvvCNhsZGwFWJ6eBM9Q2crLDUawsQ4Ar"
# "https://bitbucket.org/site/oauth2/authorize?client_id=%s&response_type=code" % bucketkey
# でcodeをもらってくる
bucketcode="6z7mS3RUT2d2EHnJqP"
#curl -X POST -u "client_id:secret" \
#  https://bitbucket.org/site/oauth2/access_token \
#  -d grant_type=authorization_code -d code={code}
# でaccess tokenにかえる
# 一時間で有効切れになるのでreferesh tokenも保存しておく

# headerに足す
# Authorization: Brearer access_token

USERAGENT = "gitHost"

# main :: IO Int
def main():
    args = sys.argv[1:]
    tokenjson = "" +\
            '{ "access_token": "hISQ-Yqa6x8Vzd9JJbJUjHwnL6g6m8LLSvUmsvTuVQMSE8M-0Fy9ZXdw2mXXHJxuPHarKLvwV4QXZPcFYQ=="\n' +\
            ', "scopes": "repository:write"\n' +\
            ', "expires_in": 3600\n' +\
            ', "refresh_token": "Be3gjjHwwhe5nHXFdw"\n' +\
            ', "token_type": "bearer"\n' +\
            '}\n'
    print(tokenjson)
    return 0

def getBucketToken(consumerkey, consumersecret, code): # TODO
    scheme = "https"
    schemehandler = urllib.request.HTTPSHandler()
    netloc = "bitbucket.org"
    path = "/site/oauth2/access_token"
    data = urllib.parse.urlencode([
        ("grant_type", "authorization_code"),
        ("code", "%s" % code)]).encode('utf-8') # :: Bytes
    headers = { "User-Agent": USERAGENT,
            "Content-Type": "application/x-www-form-urlencoded;charset=utf-8"}
    url = urllib.parse.urlunparse((scheme, netloc, path, "", "", "")) # :: Str

    passmgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
    passmgr.add_password(None, url, consumerkey, consumersecret)
    opener = urllib.request.build_opener(schemehandler,
            urllib.request.HTTPBasicAuthHandler(passmgr))
    #opener.open(url)
    urllib.request.install_opener(opener)
    request = urllib.request.Request(url, data, headers)
    response = urllib.request.urlopen(request)
    print(passmgr)
    print(opener)
    print(request)
    print(response)
    print(response.getheader())
    print(response.read())
    return undefined

def getBucketRepos(owner): # TODO
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
    return undefined

# undefined :: a
undefined = None

if __name__ == "__main__" :
  exit(main())

# vim:fenc=utf-8 ff=unix ft=python ts=4 sw=4 sts=4 si et fdm=indent fdl=0 fdn=1:
# vim:cinw=if,elif,else,for,while,try,except,finally,def,class:
