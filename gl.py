#!/usr/bin/python3

labkey="8ba20e67ea70d9622041588ecd50774ec56d005d1d363b9938803e7fe1b74179"
labsecret="36b982ce8292ac99c755811b4010bf596c82172b3bc2968df8b86efdd5daca09"
labtoken="YxP7jS3Ut7JhyxYDWKSz"

# main :: IO Int
def main():
    import sys
    args = sys.argv[1:]
    #test()
    createRepo()
    return undefined

def test():
    import urllib.parse
    import urllib.request
    import urllib.error
    url = "https://gitlab.com/api/v3/projects"
    headers = {
            "PRIVATE-TOKEN": "%s" % labtoken}
    req = urllib.request.Request(url, headers = headers)
    try:
        response = urllib.request.urlopen(req)
        print(response.read().decode('utf-8'))
        print(response.getheaders())
        print(response.status, response.reason)
    except urllib.request.HTTPError as e:
        print(e.read())

def createRepo():
    import urllib.parse
    import urllib.request
    import urllib.error
    url = "https://gitlab.com/api/v3/projects"
    headers = {
            "PRIVATE-TOKEN": "%s" % labtoken}
    req = urllib.request.Request(url, data = b'name=asdfjkl', headers = headers)
    try:
        response = urllib.request.urlopen(req)
        print(response.read().decode('utf-8'))
        print(response.getheaders())
        print(response.status, response.reason)
    except urllib.request.HTTPError as e:
        print(e.read())
        print(e.getheaders())
        print(e.status, e.reason)


# undefined :: a
undefined = None

if __name__ == "__main__" :
  exit(main())

# vim:fenc=utf-8 ff=unix ft=python ts=4 sw=4 sts=4 si et fdm=indent fdl=0 fdn=1:
# vim:cinw=if,elif,else,for,while,try,except,finally,def,class:
