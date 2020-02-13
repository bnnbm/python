'''
Created on 2020. 2. 7.

@author: gd7
soupex2.py : 크롤링 예제2 자바의 jsoup과 비슷함
'''
from bs4 import BeautifulSoup # pip install beautifulsoup4 #html 분석 모듈
import urllib.request as req #url 사용 모듈
url =\
"http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"
#res : url 전달된 데이터. soup의 분석 대상 데이터
res = req.urlopen(url)
soup = BeautifulSoup(res,"html.parser") #BeautifulSoup 객체
title = soup.find("title").string #title 태그의 내용
wf = soup.find("wf").string
print(title)
print(wf)
