#! /usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import json

headers = {
    "Accept": "application/vnd.github.v3+json",
    "Authorization": "token b16d13814ec6ffbb4750a40b6f409dff35e83962", # 此处的XXX代表上面的token
    "X-OAuth-Scopes": "repo"
}

url = "https://api.github.com/user/repos"
r = requests.get(url,headers=headers)
print(type(r.text))
# fw = open("/Users/Repostory/c-github/result.txt",'a')
# fw.write(r.text)
# fw.close()
jst = json.loads(r.text)
# print(type(jst[0]))
# dict = jst[0]
# print(dict['full_name'])
for item in jst:
    print(item['full_name'])
    #print('\n')
#print(type(jst))
