#! /usr/bin/env python
# -*- coding: utf-8 -*-

from time import sleep
import requests

headers = {
    "Accept": "application/vnd.github.v3+json",
    "Authorization": "token b86c03cd54396f93133b0d477f87eb371b4df27a", # 此处的XXX代表上面的token
    "X-OAuth-Scopes": "repo"
}
# def deleteRepository(name,username):
#         response = requests.delete('https://api.github.com/repos/'
#         + username + '/'+name+'?access_token=8b2277d262d51cbd582347d6d357ccd35e3d8d90')
#         print(response.status_code)


with open('/Users/Repostory/c-github/repos.txt', 'r', encoding='utf-8') as f:
    data = f.readlines()

url = "https://api.github.com/repos/{}/{}"
urls = []
for line in data:
    username, repo = line.strip().split("/")
    #deleteRepository(username,name)
    urls.append(url.format(username, repo))

for l in urls:
    r=requests.delete(url=l, headers=headers)
    sleep(10)
    print(r)
