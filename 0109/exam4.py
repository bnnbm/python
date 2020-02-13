'''
Created on 2020. 1. 9.

@author: gd7
exam4.py : 삼각형 출력하기

삼각형의 높이를 입력 받은 후 삼각형을 출력하는 프로그램을 작성
'''
print("직각삼각형")
num = int(input("높이를 입력하세요 : "))
for i in range(1,num+1) :
    print("*"*i)
print("역 직각삼각형")
for i in range(num,0,-1) :
    print("*"*i)
print("직각삼각형 반대")
for i in range(1,num+1) :
    print(" "*(num-i),end="")
    print("*"*i)
print("이등변 삼각형")
for i in range(0,num+1) :
    print(" "*(num-i),end="")
    print("*"*(i*2-1))
