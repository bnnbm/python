'''
Created on 2020. 1. 9.

@author: gd7
forex1.py : 구구단 출력하기
'''
i,j = 0,0
for i in range(2,10) :
    print(i,"단")
    for j in range(2,10) :
        print(i,"X",j,"=",i*j)
    