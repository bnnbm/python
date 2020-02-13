'''
Created on 2020. 2. 7.

@author: gd7
soupex3.py : 내가 만든 HTML 분석하기
'''
from bs4 import BeautifulSoup
fp = open("books.html", encoding="utf-8")
soup = BeautifulSoup(fp,"html.parser")
#람다식을 이용하여 출력하기
sel = lambda q : print(soup.select_one(q).string)
sel("#nu") #id="nu" 태그 정보 출력
sel("li#nu") #li 태그 이면서 id="nu" 태그 정보 출력
sel("ul > li#nu") #ul 태그의 하위 태그인 li 태그 의 id="nu" 태그 정보 출력
sel("#bible #nu") #id="bible"인 태그의 하위의 id="nu"인 태그 정보 출력
sel("#bible > #nu") #id="bible 인 태그의 하위 태그중 id="nu" 태그 정보 출력
sel("ul#bible > #nu")
sel("li[id='nu']") #li 태그 중 id 속성의 값이 nu인 태그 정보 출력
sel("li:nth-of-type(4)") # li태그중 4번째인 태그 정보 출력
#기존 방식으로 출력하기
print(soup.select("li")[3].string)
print(soup.find_all("li")[3].string)