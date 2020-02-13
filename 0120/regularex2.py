'''
Created on 2020. 1. 20.

@author: gd7
regularex2.py : 정규식 예제 2. 정규화 모듈 사용하기
   정규식 표현법
   () : 그룹화
   [] : 문자
   {} : 갯수
   \d : 숫자
   (\d{6})[-]\d{7} : 첫번째 그룹 : 숫자 6자리. 다음 문자 - 이면서
                     다음 문자는 숫자로 7자리로 이루어진 문자열
   \g<1> : 첫번째 그룹
   
   ? : 0 또는 1개
   ca?t : a 문자가 없거나 여러개인 경우
         "ct" : true
         "cat" : true
         "caaaat : false
   * : 0개 이상
   ca*t : a 문자가 없거나 여러개인 경우
         "ct" : true
         "cat" : true
         "caaaat : ture
   + : 1개 이상
   ca+t : a 문자가 1개이거나 여러개인 경우
         "ct" : false
         "cat" : true
         "caaaat : ture
   {n} : n개 반복
   ca{2}t : a 문자가 2개
         "ct" : false
         "cat" : false
         "caat" : true
         "caaaat : false
   {n,m} : n개 이상 m개 이하 반복
   ca{2,5}t : a 문자가 2개이상 5개 이하 반복
         "ct" : false
         "cat" : false
         "caat" : true
         "caaaaat" : true
         "caaaaaaaat : false
'''
import re #정규식 사용을 위한 모듈
data = '''
   park 800905-1234567
   kim  700905-1234567
   choi 850101-a123456
'''
pat = re.compile("(\d{6})[-]\d{7}")
print(pat.sub("\g<1>-*******",data))