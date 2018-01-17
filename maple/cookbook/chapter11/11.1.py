#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @desc  : Created by San on 18-1-17 下午11:23
# @site  : https://github.com/SunmoonSan

# 作为客户端与HTTP服务交互

from urllib import request, parse

# GET
url = 'http://httpbin.org/get'

parms = {
    'name1': 'value1',
    'name2': 'value2'
}

querystring = parse.urlencode(parms)
print(querystring)

u = request.urlopen(url+'?'+querystring)
resp = u.read()
print(resp)

print('-'*60)

url = 'http://httpbin.org/post'

# Dictionary of query parameters (if any)
parms = {
   'name1' : 'value1',
   'name2' : 'value2'
}

# Encode the query string
querystring = parse.urlencode(parms)

# Make a POST request and read the response
# u = request.urlopen(url, querystring)
# resp = u.read()
# print(resp)

# Extra headers
headers = {
    'User-agent' : 'none/ofyourbusiness',
    'Spam' : 'Eggs'
}

# req = request.Request(url, querystring.encode('ascii'), headers=headers)
# u = request.urlopen(req)
# resp = u.read()
# print(resp)

import requests

url = 'http://httpbin.org/post'

parms = {
    'name1': 'value1',
    'name2': 'value2'
}

headers = {
    'User-agent' : 'none/ofyourbusiness',
    'Spam' : 'Eggs'
}

resp = requests.post(url, data=parms, headers=headers)
text = resp.text
print(text)

print('-'*60)

resp = requests.head('http://www.python.org/index.html')
print(resp.status_code)
# print(resp.headers['last-modified'])
# print(resp.headers['content-type'])
# print(resp.headers['content-length'])




