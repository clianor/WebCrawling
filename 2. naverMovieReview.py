#-*- coding:utf-8 -*-
import requests as rq
from bs4 import BeautifulSoup

url = "https://movie.naver.com/movie/bi/mi/review.nhn?code=149236&page=1#"

sess = rq.Session()
sess.headers['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Whale/1.0.41.8 Safari/537.36"
req = sess.get(url)

soup = BeautifulSoup(req.text, 'html.parser')
reviewForm = soup.find('div', class_='review')

length = reviewForm.find('span', class_='cnt').find('em').text
print('전체 %s개' %(length))

reviewBody = reviewForm.find('ul', class_='rvw_list_area')
reviewTitle = [l.text for l in reviewBody.find_all('strong')]
reviewSummary = [l.text for l in reviewBody.find_all('p')]

for i, (title, summary) in enumerate(zip(reviewTitle, reviewSummary)):
    print('title :', title)
    print('summary :', summary)
    print('---------')