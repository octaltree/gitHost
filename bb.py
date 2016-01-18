#!/usr/bin/python3

#from enum import Enum

USERAGENT = "gitHost"

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


# main :: IO Int
def main():
    import sys
    import json
    args = sys.argv[1:]
    tokenjson = '{"access_token": "JAb-xAUopHf8jmwSp1jvUv4oH1lqpgrYWqTJAS5Qz13UcuLifgWwYYhnjUmBQ_grS1qfxrwqjb_WVnYqkw==", "scopes": "repository:write", "expires_in": 3600, "refresh_token": "Be3gjjHwwhe5nHXFdw", "token_type": "bearer"}'
    tokens = json.loads(tokenjson) # :: dic
    #print(getBucketRepos(tokens['access_token'], "octaltree"))
    print(getBucketRepos("asdf", "octaltree"))
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
    print(response.getheaders())
    print(response.read())
    return undefined

# getBucketRepos :: Str -> Str -> IO Str
def getBucketRepos(token, owner): # TODO ProxyHandler
    import urllib.request
    import urllib.parse
    import urllib.error
    req = urllib.request.Request("https://api.bitbucket.org/2.0/repositories/%s" % owner,
            headers = { "User-Agent": USERAGENT, "Authorization": "Bearer %s" % token})
    try:
        response = urllib.request.urlopen(req)
        charset = charsetFromContentType(response.getheader('content-type'))
        return response.read().decode(charset if charset != '' else 'utf-8')
    except urllib.error.URLError as e:
        return None

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
