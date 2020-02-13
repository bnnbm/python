'''
Created on 2020. 1. 20.

@author: gd7
yieldex1.py : 함수의 종료 없이, yield 예약어로 값 리턴
'''
def genFun(num) :
    for i in range(10,num+10) :
        yield(i)
        print(i,"값 반환")
        
print(list(genFun(5)))