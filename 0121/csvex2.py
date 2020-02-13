'''
Created on 2020. 1. 21.

@author: gd7
csvex2.py : codecs 클래스를 이용하여 csv 파일 읽기
'''
import codecs
filename = "jeju1.csv"
csv = codecs.open(filename, "r","euc-kr").read()
data = []
rows = csv.split("\r\n")
for row in rows :
    if row == "" : continue #입력줄이 공백
    cells = row.split(",")
    data.append(cells)
for c in data :
    print(c[0],c[1],c[2])