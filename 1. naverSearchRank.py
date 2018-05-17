# -*- coding:utf-8 -*-
import requests as rq
from bs4 import BeautifulSoup

# requests 세션 객체 생성
sess = rq.Session()

# 세션에 User-Agent 정보 추가
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
              AppleWebKit/537.36 (KHTML, like Gecko) \
              Chrome/60.0.3112.113 Whale/1.0.41.8 Safari/537.36'
sess.headers['User-Agent'] = user_agent

# 네이버 데이터 랩의 검색어 순위 페이지 가져오기
req = sess.get('https://datalab.naver.com/keyword/realtimeList.naver')

# 정상적으로 페이지를 가져왔는지 확인
if req.status_code == 200:
    # 가져온 페이지의 HTML 텍스트를 추출
    html = req.text

    # BeautifulSoup를 이용하여 html 파싱
    soup = BeautifulSoup(html, 'html.parser')

    # 가장 최근에 갱신된 네이버 검색어 순위를 가져옴
    keyword = soup.find('div', class_='keyword_rank select_date')

    # 언제 갱신되었는지 추출하여 보여줌
    print(keyword.find('strong', class_='rank_title v2').text)

    # 검색어 순위 정보를 추출함
    keywordL = keyword.find_all('li')
    keywordL = list(map(lambda x: x.text.split(), keywordL))

    # 추출한 검색어 순위 정보를 보여줌
    for l in keywordL:
        print(' '.join(l))
else:
    # 페이지를 가져오는데 실패하였을 때
    print('HTTP 통신에 실패하였습니다.')