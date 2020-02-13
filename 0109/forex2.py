'''
Created on 2020. 1. 9.

@author: gd7
forex2.py : 가로 구구단 출력하기
'''
i,j = 0,0
for i in range(2,10) :
    print("%5d단%17s" % (i," "),end="") # 15s : 공백 15칸
print()
for j in range(2,10) :
    for i in range(2,10,1) :
        print("%2d X%2d =%3d  " % (i,j,(i*j)),end="")
    print()
