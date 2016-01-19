#!/usr/bin/python3

from enum import Enum

USERAGENT = "gitHost"

bucketkey="Ev4c4krDQqHyRd2XH6"
bucketsecret="TvvCNhsZGwFWJ6eBM9Q2crLDUawsQ4Ar"
# repo read, admin権限必要
# "https://bitbucket.org/site/oauth2/authorize?client_id=%s&response_type=code" % bucketkey
# でcodeをもらってくる
bucketcode="4RcZ8CTkBe6FAFzNhP"
#curl -X POST -u "client_id:secret" \
#  https://bitbucket.org/site/oauth2/access_token \
#  -d grant_type=authorization_code -d code={code}
# でaccess tokenにかえる
# 一時間で有効切れになるのでreferesh tokenも保存しておく

# headerに足す
# Authorization: Brearer access_token

# Either返さずログだして死んでもいいかも

class FakedEither(Enum):
    Left = 0
    Right = 1

# main :: IO Int
def main():
    import sys
    import json
    args = sys.argv[1:]
    tokenjson = '{"access_token": "As8tJt_YaeymjnKwow8t9XASqUX20MgCvczFbyYIbJrjNIbAj1IC0zRWPmaFul1WO0zyQhYJMt-hpcaOqA==", "scopes": "repository:admin repository", "expires_in": 3600, "refresh_token": "2g7VCmzNcR8p3XDWa6", "token_type": "bearer"}'
    tokens = json.loads(tokenjson) # :: dic
    refreshBucketAccessToken(bucketkey, bucketsecret, tokens['refresh_token'])
    #if len(args) == 0 :
    #    return 0
    #elif args[0] == "show" :
    #    print(getBucketRepos(tokens['access_token'], "octaltree"))
    #elif args[0] == "new" :
    #    print(newBucketRepo(tokens['access_token'], "octaltree", "apitest2"))
    #    #print(newBucketRepo('dummy', "octaltree", "apitest2")[1].read())
    return 0

def refreshBucketAccessToken(clientkey, clientsecret, refreshtoken):
    import urllib.parse
    import urllib.request
    import urllib.error
    import base64
    url = "https://bitbucket.org/site/oauth2/access_token"
    data = urllib.parse.urlencode([
        ("grant_type", "refresh_token"),
        ("refresh_token", "%s" % refreshtoken)]).encode('utf-8') # :: Bytes
    headers = {
            "Authorization": "Basic %s" % base64.b64encode((clientkey + ":" + clientsecret).encode('utf-8')).decode('utf-8'),
            "User-Agent": "curl/7.35.0"}
    print(headers)
    req = urllib.request.Request(url, data=data, headers=headers)
    passmgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
    passmgr.add_password(None, url, clientkey, clientsecret)
    #passmgr.add_password(None, "//bitbucket.org/site/oauth2/access_token", clientkey, clientsecret)
    #passmgr.add_password(None, "/site/oauth2/access_token", clientkey, clientsecret)
    #passmgr.add_password(None, "https://bitbucket.org", clientkey, clientsecret)
    #passmgr.add_password(None, "bitbucket.org", clientkey, clientsecret)
    #passmgr.add_password(None, "http://bitbucket.org", clientkey, clientsecret)
    opener = urllib.request.build_opener(
            #urllib.request.HTTPHandler(req),
            #urllib.request.HTTPSHandler(req),
            #urllib.request.ProxyHandler(),
            urllib.request.HTTPBasicAuthHandler(passmgr))
    urllib.request.install_opener(opener)
    try:
        response = urllib.request.urlopen(req)
        print(response.read())
    except urllib.request.HTTPError as e:
        print(e.read())
    return undefined

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
    print(response.getheaders())
    print(response.read())
    return undefined

def newBucketRepo(token, user, reponame, repoalias = ''): # TODO 例外, ProxyHandler
    import urllib.request
    import urllib.parse
    import urllib.error
    # is_private 標準がfalseなのでtrueに
    # 付随してfork_policyやらいろいろ
    repoalias = reponame if repoalias == '' else repoalias
    req = urllib.request.Request("https://api.bitbucket.org/2.0/repositories/%s/%s" % (urllib.parse.quote(user), reponame),
            data = urllib.parse.urlencode({"name": "%s" % repoalias}).encode('utf-8'), # BytesUtf8
            headers = { "User-Agent": USERAGENT, "Authorization": "Bearer %s" % token})
    try:
        response = urllib.request.urlopen(req)
        charset = charsetFromContentType(response.getheader('content-type'))
        return (FakedEither.Right, response.read().decode(charset if charset != '' else 'utf-8'))
    except urllib.error.HTTPError as e:
        return (FakedEither.Left, e)

# getBucketRepos :: Str -> Str -> IO (FakedEither, HTTPError|Str)
def getBucketRepos(token, user): # TODO ProxyHandler
    import urllib.request
    import urllib.parse
    import urllib.error
    req = urllib.request.Request("https://api.bitbucket.org/2.0/repositories/%s" % urllib.parse.quote(user),
            headers = { "User-Agent": USERAGENT, "Authorization": "Bearer %s" % token})
    try:
        response = urllib.request.urlopen(req)
        charset = charsetFromContentType(response.getheader('content-type'))
        return (FakedEither.Right, response.read().decode(charset if charset != '' else 'utf-8'))
    except urllib.error.HTTPError as e:
        return (FakedEither.Left, e)

# getBucketRepos :: Str -> Str -> IO (FakedEither, HTTPError|Str)
def getBucketReposWithProxy(token, user): # TODO
    import urllib.request
    import urllib.parse
    import urllib.error
    req = urllib.request.Request("https://api.bitbucket.org/2.0/repositories/%s" % urllib.parse.quote(user),
            headers = { "User-Agent": USERAGENT, "Authorization": "Bearer %s" % token})
    opener = urllib.request.build_opener(
            urllib.request.ProxyHandler())
    urllib.request.install_opener(opener)
    try:
        response = urllib.request.urlopen(req)
        charset = charsetFromContentType(response.getheader('content-type'))
        return (FakedEither.Right, response.read().decode(charset if charset != '' else 'utf-8'))
    except urllib.error.HTTPError as e:
        return (FakedEither.Left, e)

# charsetFromContentType :: Str -> Str
def charsetFromContentType(str):
    import re
    # 基本''を返す 指定してあればそれを返す
    lines = str.split(';')
    charsets = list(filter(lambda s: 'charset' in s, lines))
    if len(charsets) == 0 :
        return ''
    charset = charsets.pop().replace(' ', '')
    mat = re.match('^charset=(.*?)[;]*$', charset)
    return mat.group(1) if mat else ''

# undefined :: a
undefined = None

if __name__ == "__main__" :
  exit(main())

# vim:fenc=utf-8 ff=unix ft=python ts=4 sw=4 sts=4 si et fdm=indent fdl=0 fdn=1:
# vim:cinw=if,elif,else,for,while,try,except,finally,def,class:
