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

# main :: IO Int
def main():
    return undefined

if __name__ == "__main__" :
  exit(main())

# vim:fenc=utf-8 ff=unix ft=python ts=4 sw=4 sts=4 si et fdm=indent fdl=0 fdn=1:
# vim:cinw=if,elif,else,for,while,try,except,finally,def,class:
