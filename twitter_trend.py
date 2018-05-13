#!/usr/bin/env python
# -*- coding: utf-8 -*-

from requests_oauthlib import OAuth1Session
import json

CK = '' # Consumer Key
CS = '' # Consumer Secret
AT = '' # Access Token
AS = '' # Accesss Token Secert

# タイムライン取得用のURL
url = "https://api.twitter.com/1.1/trends/place.json?id=23424856"
params = {}

# OAuth で GET
twitter = OAuth1Session(CK, CS, AT, AS)
req = twitter.get(url, params = params)

if req.status_code == 200:
    # レスポンスはJSON形式なので parse する
    trends_json = json.loads(req.text)
    for trends in trends_json:
        for trend in trends["trends"]:
            print(trend["name"])

else:
    # エラーの場合
    print ("Error: %d" % req.status_code)
