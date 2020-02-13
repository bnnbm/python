'''
Created on 2020. 1. 21.

@author: gd7
fileex1.py : 파일 읽기

파일모드
   "r" : 읽기모드
   "w" : 쓰기모드, 파일이 존재하지 않으면 생성
   "r+" : 읽기/쓰기 겸용
   "a" : 쓰기모드
'''
infp = None
inStr = ""
infp = open("../0120/regularex3.py", "rt", encoding='UTF8')
while True :
    inStr = infp.readline()
    if inStr == None :
        break
    print(inStr, end="")
infp.close()