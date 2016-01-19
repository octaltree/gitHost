#!/usr/bin/python3

import sys
#import argparse
import urllib.parse
import http.client
import json
from enum import Enum

class Visibility(Enum):
    No = 0
    Public = 1
    Private = 2
    All = 3

# main :: IO Int
def main():
    useragent = "gitHost"
    hubtoken = "8f32aae21b80d8644d3ed02fdec2e7b04031400f"
    #parser = argparse.ArgumentParser()
    #args = parser.parse_args()
    prms = sys.argv[1:]
    return 0

def hubGetRepos(token): # TODO
    method = "GET"
    hostname = "api.github.com"
    path = "/user/repos"
    url = urllib.parse.urlunparse(("", "", path, "", "", "")) # :: Str
    header = {
            "Authorization": "bearer %s" % token,
            "User-Agent": "gitHost"}
    body = json.dumps({})
    conn = http.client.HTTPSConnection(hostname)
    conn.request(method, url, body, header)
    response = conn.getresponse()
    print(response.read())
    print(str(response.status) + "  " + response.reason)

# hubCreateRepo :: Str -> Str -> Bool -> IO ()
def hubCreateRepo(token, name, isprivate): # TODO
    method = "POST"
    hostname = "api.github.com"
    path = "/user/repos"
    url = urllib.parse.urlunparse(("", "", path, "", "", "")) # :: Str
    header = {
            "Authorization": "bearer %s" % token,
            "User-Agent": "gitHost"}
    body = json.dumps({
        "name": name,
        "private": isprivate})
    conn = http.client.HTTPSConnection(hostname)
    conn.request(method, url, body, header)
    response = conn.getresponse()
    print(response.read())
    print(str(response.status) + "  " + response.reason)
    undefined

# hubOauth :: Str -> Str -> Str -> IO ()
def hubOauth(key, secret, scope): # TODO
    method = "GET"
    hostname = "github.com"
    path = "/login/oauth/authorize"
    query = urllib.parse.urlencode({
        "client_id": "%s" % hubkey,
        "scope": "public_repo"}) # :: Str
    url = urllib.parse.urlunparse(('', '', path, '', query, '')) # :: Str

    conn = http.client.HTTPSConnection(hostname)
    conn.request(method, url)
    response = conn.getresponse()

    #print(response.read().decode('utf-8'))
    print(str(response.status) + "  " + response.reason)
    return ()
    undefined

# undefined :: a
undefined = None

if __name__ == "__main__" :
  exit(main())

# vim:fenc=utf-8 ff=unix ft=python ts=4 sw=4 sts=4 si et fdm=indent fdl=0 fdn=1:
# vim:cinw=if,elif,else,for,while,try,except,finally,def,class:
