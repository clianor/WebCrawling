# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import requests as rq

user_id = 'your id'
user_pw = 'your pw'
haknum = 'your haknum'

rq.packages.urllib3.disable_warnings()
rq.packages.urllib3.util.ssl_.DEFAULT_CIPHERS += 'HIGH:!DH:!aNULL'

sess = rq.Session()
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
              AppleWebKit/537.36 (KHTML, like Gecko) \
              Chrome/60.0.3112.113 Whale/1.0.41.8 Safari/537.36'
sess.headers['User-Agent'] = user_agent

res = sess.get('http://portal.ks.ac.kr/')
res.raise_for_status()

res = sess.get('http://apps.ks.ac.kr/ptl/?')
res.raise_for_status()

res = sess.get('http://apps.ks.ac.kr/ksu/blank.jsp')
res.raise_for_status() 
cookie_1 = res.headers['Set-Cookie']
sess.headers['Set-Cookie'] = cookie_1.split(';')[0]

res = sess.get('https://cms1.ks.ac.kr/dummy.jsp?new20170310')
res.raise_for_status()
cookie_2 = res.headers['Set-Cookie']

res = sess.get('http://apps.ks.ac.kr/ptl/sso/business.jsp?')
res.raise_for_status()

res = sess.get('https://cms1.ks.ac.kr/dummy.jsp?new20170310')
res.raise_for_status()

data = {'isToken':'', 'secureToken':'', 'secureSessionId':''}
res = sess.post('http://apps.ks.ac.kr/ptl/sso/checkserver.jsp', data=data)
res.raise_for_status()

data = {'ssid':'1'}
res = sess.post('http://sso.ks.ac.kr/isignplus/index.jsp', data=data)
cookie_3 = res.headers['Set-Cookie']
sess.headers['Set-Cookie'] = cookie_3.split(';')[0]

data = {'ssid':'1', 'method':'preChallenge', 'device':'0'}
res = sess.post('http://sso.ks.ac.kr/LoginServlet', data=data)
res.raise_for_status()

data = {
    'secureToken':'',
    'secureSessionId':'',
    'isToken':'N',
    'reTry':'Y',
    'method':'checkToken'}
sess.headers['Set-Cookie'] = cookie_1.split(';')[0]
res = sess.post('http://apps.ks.ac.kr/ptl/sso/business.jsp', data=data)
res.raise_for_status()

data = {
    'isToken':'N',
    'secureToken':'',
    'secureSessionId':''}
res = sess.post('http://apps.ks.ac.kr/ptl/sso/login.jsp', data=data)
res.raise_for_status()

res = sess.get('https://cms1.ks.ac.kr/portalLoginImgSlide/index_400x359o.jsp?rt=1')
res.raise_for_status()

res = sess.get('https://apps.ks.ac.kr/ptl/sso/webcrypto/js/webcrypto/pka/file_open_frame.html')
res.raise_for_status()

data = {
    'issacweb_data':'',
    'challenge':'',
    'response':'',
    'mode':'login_proc',
    'return_url':'',
    'id':user_id,
    'pw':user_pw,
    'method':'idpwProcessEx',
    'ssid':'1'
}

sess.headers['Cookie'] = cookie_3.split(';')[0]
res = sess.post('https://sso.ks.ac.kr/LoginServlet', data=data)
res.raise_for_status()
soup = BeautifulSoup(res.text, 'html.parser')
secureToken = soup.find('input', {'name':'secureToken'})['value']
secureSessionId = soup.find('input', {'name':'secureSessionId'})['value']

data = {
    'secureToken':secureToken,
    'secureSessionId':secureSessionId,
    'isToken':'Y',
    'reTry':'N',
    'method':'checkToken'
}
res = sess.post('https://apps.ks.ac.kr/ptl/sso/business.jsp', data=data)
res.raise_for_status()
cookie_4 = res.headers['Set-Cookie']

data = {
    'isToken':'Y',
    'secureToken':secureToken,
    'secureSessionId':secureSessionId
}
sess.headers['Cookie'] = 'loginTab=1; ' + cookie_4.split(';')[0]
res = sess.post('https://apps.ks.ac.kr/ptl/sso/checkauth.jsp', data=data)
res.raise_for_status()

data = {
    'secureToken':secureToken,
    'secureSessionId':secureSessionId,
    'method':'updateSecureToken',
    'ssid':'1'
}
sess.headers['Cookie'] = 'NTASSESSIONID=' + secureSessionId
res = sess.post('https://sso.ks.ac.kr/LoginServlet', data=data)
res.raise_for_status()

sess.headers['Cookie'] = 'loginTab=1; ' + cookie_4.split(';')[0] + ' kssso=ok; ksuid=' + user_id
res = sess.get('https://apps.ks.ac.kr/ptl/portal.Login')
res.raise_for_status()

# sess.headers['Cookie'] = cookie_2.split(';')[0] + '; kssso=ok; ksuid=' + user_id + '; USER_ID=' + user_id + 'USER_DIV=70; USER_TP=1; PERSONAL_ID=' + haknum
# sess.headers['Content-Length'] = '1104'
# data = {
#     'returnURL':'http://cms1.ks.ac.kr/sportal'
# }
# res = sess.get('https://cms1.ks.ac.kr/sso/business.jsp', data=data)
# print(res)

sess.headers['Cookie'] = cookie_2.split(';')[0] + '; kssso=ok; ksuid=' + user_id + '; USER_ID=' + user_id + 'USER_DIV=70; USER_TP=1; PERSONAL_ID=' + haknum
res = sess.post('https://sso.ks.ac.kr/isignplus/index.jsp', data={'ssid':'37'})
res.raise_for_status()

data = {
    'ssid':'37',
    'method':'preChallenge',
    'device':'0'
}
res = sess.post('https://sso.ks.ac.kr/LoginServlet', data=data)
res.raise_for_status()

data = {
    'secureToken':secureToken,
    'secureSessionId':secureSessionId,
    'isToken':'Y',
    'reTry':'N',
    'method':'checkToken'
}
res = sess.post('https://cms1.ks.ac.kr/sso/business.jsp', data=data)
res.raise_for_status()

data = {
    'secureToken':secureToken,
    'secureSessionId':secureSessionId,
    'isToken':'Y'
}
res = sess.post('https://cms1.ks.ac.kr/sso/checkauth.jsp', data=data)
res.raise_for_status()

data = {
    'secureToken':secureToken,
    'secureSessionId':secureSessionId,
    'method':'updateSecureToken',
    'ssid':'37'
}
res = sess.post('https://sso.ks.ac.kr/LoginServlet', data=data)
res.raise_for_status()

res = sess.get('https://cms1.ks.ac.kr/sportal/')
res.raise_for_status()

res = sess.get('https://cms1.ks.ac.kr/sportal/Main.do')
res.raise_for_status()