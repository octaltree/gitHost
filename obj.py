#!/usr/bin/python3
# written in Python 3.4.3

from enum import Enum
import sys
import os
import os.path
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
    # :: Github -> OAuthConsumer -> Dict -> Str -> a
    def __init__(self, consumer, dictoken, defaultuser = None):
        self.consumer = consumer
        self.tokens = dictoken
        self.defaultuser = defaultuser
        return None
    # :: Github -> Str
    def json(self):
        diccon = json.loads(self.consumer.json())
        dictoken = json.loads(self.toknes.json())
        dic = {
                "consumer": diccon,
                "tokens": dictoken}
        return json.dumps(dic, ensure_ascii=False)
    defaultuser = None # :: Str
    consumer = None # :: OAuthConsumer
    tokens = None # :: Dict # username to OAuthToken
    # :: Github -> Str -> Str -> OAuthToken
    def getOAuthToken(self, user, code):
        if self.consumer is None:
            exit("need consumerkey, secret to get access_token")
        data = urllib.parse.urlencode([
            ("client_id", consumer.key),
            ("client_secret", consumer.secret),
            ("code", code)
            ]).encode('utf-8') # :: BytesUtf8
        headers = {
                "Content-Type": "application/x-www-form-urlencoded;charset=utf-8",
                "Accept": "application/json"}
        req = urllib.request.Request("https://github.com/login/oauth/access_token",
                data, headers)
        token = json.loads(body(http(req))) # :: Dict
        try:
            t = OAuthToken(token)
            if self.tokens is None:
                self.tokens = {}
            self.tokens.update({user, t})
            return t
        except KeyError:
            exit(token)
    # :: Github -> Str
    def urlOAuthCode(self):
        urllib.parse.urlunparse(("https", "github.com", "/login/oauth/authorize", "",
            urllib.parse.urlencode([
                ("client_id", self.consumer.key),
                ("redirect_uri", URLOAUTHCALLBACK),
                ("scope", "public_repo,repo,user") # TODO userいらない?
                ]), ""))
    # :: Dict -> Str
    def urlFriendlyRepoFullName(repo):
        return repo['path_with_namespace']

class Bitbucket:
    # :: Bitbucket -> OAuthConsumer -> Dict -> Str -> a
    def __init__(self, consumer, dictoken):
        self.consumer = consumer
        self.tokens = dictoken
        self.defaultuser = defaultuser
        return None
    # :: Bitbucket -> Str
    def json(self):
        diccon = json.loads(self.consumer.json())
        dictoken = json.loads(self.toknes.json())
        dic = {
                "consumer": diccon,
                "tokens": dictoken}
        return json.dumps(dic, ensure_ascii=False)
    defaultuser = None # :: Str
    consumer = None # :: OAuthConsumer
    tokens = None # :: Dict # username to OAuthToken

class Gitlab:
    # :: Gitlab -> OAuthConsumer -> Dict -> Str -> a
    def __init__(self, consumer, dictoken):
        self.defaultuser = defaultuser
        self.consumer = consumer
        self.tokens = dictoken
        return None
    # :: Gitlab -> Str
    def json(self):
        diccon = json.loads(self.consumer.json())
        dictoken = json.loads(self.toknes.json())
        dic = {
                "consumer": diccon,
                "tokens": dictoken}
        return json.dumps(dic, ensure_ascii=False)
    defaultuser = None # :: Str
    consumer = None # :: OAuthConsumer
    tokens = None # :: Dict # username to OAuthToken

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
    # :: OAuthToken -> Dict -> a
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
        if token.get("expires_in") is not None:
            self.expires_in = datetime.timedelta(seconds=token['expires_in'])
        return None

    __str__ = lambda self: str(vars(self)) + " :: OAuthToken"
    def json(self):
        dic = vars(self)
        dic.update({"create_at": self.create_at.strftime(TIMEFORMAT)})
        dic.update({"expires_in": self.expires_in.total_seconds()})
        return json.dumps(dic, ensure_ascii=False)
    # :: Dict -> OAuthConsumer
    def fromDict(dic):
        res = OAuthToken(dic)
        res.refresh_token = dic.get("refresh_token")
        res.token_type = dic.get("token_type")
        res.scope = dic.get("scope")
        if dic.get('expires_in') is not None:
            res.expires_in = datetime.timedelta(seconds=dic['expires_in'])
        if dic.get('create_at') is not None:
            res.create_at = datetime.datetime.strptime(
                    dic['create_at'], TIMEFORMAT)
        return res

    access_token = None # :: Str
    refresh_token = None # :: Str
    scope = None # :: Str
    token_type = None # :: Str
    expires_in = None # :: datetime.timedelta
    created_at = None # :: datetime.datetime

# main :: IO Int
def main():
    touchConfig()
    dic = inputConfig(readConfig())
    hub = dic.get('github') # :: Github
    lab = dic.get('gitlab') # :: Gitlab
    bucket = dic.get('bitbucket') # ::  Bitbucket
    return undefined

# :: IO ()
def touchConfig():
    if not os.path.exists(os.path.expanduser("~/.githost/")):
        os.makedirs(os.path.expanduser(("~/.githost/")))
    f = open(os.path.expanduser("~/.githost/config"), "a")
    f.write('')
    return ()

# :: Str -> IO ()
def writeConfig(rawjson):
    f = open(os.path.expanduser("~/.githost/config"), "w")
    f.write(rawjson)
    return ()

# :: IO Str
def readConfig():
    f = open(os.path.expanduser("~/.githost/config"), "r")
    return f.read()

# :: Github -> Bitbucket -> Gitlab -> Str
def outputConfig(hub=None, bucket=None, lab=None):
    dic = {}
    if hub is not None:
        hub.update({"github": json.loads(hub.json())})
    if bucket is not None:
        bucket.update({"bitbucket": json.loads(bucket.json())})
    if lab is not None:
        lab.update({"gitlab": json.loads(lab.json())})
    return json.dumps(dic, ensure_ascii=False, indent=4, separators=(',', ':'))

# :: Str -> Dict
def inputConfig(rawjson):
    try:
        dic = json.loads(rawjson)
    except:
        print("~/.githost/config", file=sys.stderr)
        exit("can't read config")
    res = {}
    # :: Dict -> (OAuthConsumer, Dict, Str)
    def read(dic):
        c = OAuthConsumer.fromDict(dic['consumer'])
        t = {}
        [t.update({t[0]: OAuthToken.fromDict(t[1])})
                for t in dic['tokens'].items()]
        d = dic.get('defaultuser')
        return (c, t, d)
    if dic.get("github") is not None:
        t = read(dic)
        res.update({"github": Github(t[0], t[1], t[2])})
    if dic.get("bitbucket") is not None:
        t = read(dic)
        res.update({"bitbucket": Github(t[0], t[1], t[2])})
    if dic.get("gitlab") is not None:
        t = read(dic)
        res.update({"gitlab": Github(t[0], t[1], t[2])})
    return res

if __name__ == "__main__" :
  exit(main())

# vim:fenc=utf-8 ff=unix ft=python ts=4 sw=4 sts=4 si et fdm=indent fdl=0 fdn=2:
# vim:cinw=if,elif,else,for,while,try,except,finally,def,class:
