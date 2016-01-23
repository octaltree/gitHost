#!/usr/bin/python3
# written in Python 3.4.3

from enum import Enum
import sys
#import traceback
import argparse
import urllib.parse
import urllib.request
import urllib.error
import json
import re
import datetime
#import logging

# undefined :: a
undefined = None

USERAGENT = "gitHost/0.0.1.0" # 何かしら指定しないとhubに怒られる
URLOAUTHCALLBACK = "http://github.com/octaltree" # :: Str
TIMEFORMAT = "%Y,%j,%H,%M,%S,%f"

class Github:
    undefined

class Bitbucket:
    undefined

class Gitlab:
    undefined

class OAuthConsumer:
    # :: OAuthConsumer -> Str -> Str -> a
    def __init__(self, key, secret):
        self.key = key
        self.secret = secret
        return None
    __str__ = lambda self: str(vars(self)) + " :: OAuthConsumer"
    json = lambda self: json.dumps(vars(self))
    # :: Dict -> OAuthConsumer
    def fromDict(dic):
        return OAuthConsumer(dic['key'], dic['secret'])
    key = None # :: Str
    secret = None # :: Str

class OAuthToken:
    def __init__(self, token):
        try:
            self.access_token = token['access_token']
        except KeyError:
            exit("fail at OAuthToken(" + str(token) + ")")
        self.create_at = datetime.datetime.now()
        self.token_type = token.get("token_type")
        self.scope = token.get("scope", self.scope)
        self.scope = token.get("scopes", self.scope)
        self.refresh_token = token.get("refresh_token")
        self.expires_in = token.get("expires_in") # TODO :: datetime.timedelta
        return None

    __str__ = lambda self: str(vars(self)) + " :: OAuthToken"
    def json(self):
        dic = vars(self)
        dic.update({"create_at": self.create_at.strftime(TIMEFORMAT)})
        return json.dumps(dic, ensure_ascii=False, indent=4, separators=(',', ':'))
    access_token = None # :: Str
    refresh_token = None # :: Str
    scope = None # :: Str
    token_type = None # :: Str
    expires_in = None # :: datetime.timedelta
    created_at = None # :: datetime.datetime

# main :: IO Int
def main():
    hoge = OAuthToken({'access_token': 'asdf'})
    print(hoge.json())
    return undefined

if __name__ == "__main__" :
  exit(main())

# vim:fenc=utf-8 ff=unix ft=python ts=4 sw=4 sts=4 si et fdm=indent fdl=0 fdn=1:
# vim:cinw=if,elif,else,for,while,try,except,finally,def,class:
