'''
Created on 2020. 1. 21.

@author: gd7
fileex3.py : 파일 존재 여부 확인 하기
'''
import os.path
file = 'C:\\Data\\Python\\nofile.txt'
file = "csvex1.py"
file = "../0120"
if os.path.isfile(file) :
    print("Yes. it is a file")
elif os.path.isdir(file) :
    print("Yes. it is a directory")
if os.path.exists(file) :
    print("Something exist")
else : 
    print("Nothing")