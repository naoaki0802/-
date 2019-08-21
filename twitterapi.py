# -*- coding: utf-8 -*-
 
from requests_oauthlib import OAuth1Session
import json
import datetime, time, sys
 
CK = '8uYOL8qfRB---------------'                             # Consumer Key
CS = 'HFIcvU2nCB----------------------------------------'    # Consumer Secret
AT = '104137178-----------------------------------------'    # Access Token
AS = '4ViVoEMdiH-----------------------------------'         # Accesss Token Secert
 
session = OAuth1Session(CK, CS, AT, AS)
 
url = 'https://api.twitter.com/1.1/search/tweets.json'
res = session.get(url, params = {'q':u'沖縄旅行', 'count':10})
 
#--------------------
# ステータスコード確認
#--------------------
if res.status_code != 200:
    print ("Twitter API Error: %d" % res.status_code)
    sys.exit(1)
 
#--------------
# ヘッダー部
#--------------
print ('アクセス可能回数 %s' % res.headers['X-Rate-Limit-Remaining'])
print ('リセット時間 %s' % res.headers['X-Rate-Limit-Reset'])
sec = int(res.headers['X-Rate-Limit-Reset'])\
           - time.mktime(datetime.datetime.now().timetuple())
print ('リセット時間 （残り秒数に換算） %s' % sec)
 
#--------------
# テキスト部
#--------------
res_text = json.loads(res.text)
for tweet in res_text['statuses']:
    print ('-----')
    print (tweet['created_at'])
    print (tweet['text'])
