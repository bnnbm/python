'''
Created on 2020. 1. 14.

@author: gd7
fiboex1.py : 피보너치 수열 구하기
피보너치 수열 : 0,1,1,2,3,5,8,13,21 ...
입력값 : 5
0,1,1,2,3
입력값 : 10
0,1,1,2,3,5,8,13,21,34
'''
def fibo(n) :
    global num1,num2,num3
    fibolist.append(num1)
    fibolist.append(num2)
    fibolist.append(num3)
    for i in range(3,n) :
        num1 = num2
        num2 = num3
        num3 = num1 + num2
        fibolist.append(num3)    

fibolist = []
num1 = 0
num2 = 1
num3 = num1 + num2
num = int(input("피보너치 수열을 구할 갯수를 입력하세요. 단 3 이상의 값 : "))
print("f(",num,")=",end="")
fibo(num)
print(fibolist)