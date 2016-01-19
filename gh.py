#!/usr/bin/python3

USERAGENT='gitHost'

hubtoken = "8f32aae21b80d8644d3ed02fdec2e7b04031400f"

# main :: IO Int
def main():
    import sys
    args = sys.argv[1:]
    #test()
    newRepo('apitestsdf', False)
    return undefined

def test():
    import urllib.parse
    import urllib.request
    import urllib.error
    url = "https://api.github.com/user/repos"
    headers = {
            "Authorization": "token %s" % hubtoken,
            "User-Agent": "%s" % USERAGENT}
    req = urllib.request.Request(url, headers = headers)
    try:
        response = urllib.request.urlopen(req)
        print(response.read())
        print(response.getheaders())
        print(response.status, response.reason)
    except urllib.request.HTTPError as e:
        print(e.read())
        print(e.getheaders())
        print(e.status, e.reason)

def newRepo(name, isprivate):
    import urllib.parse
    import urllib.request
    import urllib.error
    import json
    url = "https://api.github.com/user/repos"
    headers = {
            "Authorization": "token %s" % hubtoken,
            "User-Agent": "%s" % USERAGENT}
    data = json.dumps({
        "name": name,
        "private": isprivate}).encode('utf-8')
    req = urllib.request.Request(url, data, headers)
    try:
        response = urllib.request.urlopen(req)
        print(response.read())
        print(response.getheaders())
        print(response.status, response.reason)
    except urllib.error.HTTPError as e:
        print(e.read())
        print(e.getheaders())
        print(e.status, e.reason)


# undefined :: a
undefined = None

if __name__ == "__main__" :
  exit(main())

# vim:fenc=utf-8 ff=unix ft=python ts=4 sw=4 sts=4 si et fdm=indent fdl=0 fdn=1:
# vim:cinw=if,elif,else,for,while,try,except,finally,def,class:
