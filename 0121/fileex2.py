'''
Created on 2020. 1. 21.

@author: gd7
fileex2.py : 파일 쓰기
'''
outfp = None
outfp = open("data.txt","w",encoding='UTF8')
while True :
    outStr = input("내용 입력:")
    if outStr != "" :
        outfp.writelines(outStr + "\n")
    else :
        break
outfp.close()
print("프로그램 종료")