'''
Created on 2020. 1. 9.

@author: gd7
exam3.py : 숫자를 입력 받아 입력 수 까지 합을 출력하기
                     숫자를 입력 받아 입력 수 까지 짝수의 합을 출력하기
'''
num = int(input("숫자를 입력하세요 : "))
sum = 0    
print("for 구문")
for i in range(1,num+1) :
    sum = sum+i  
print("1부터 ",num,"까지의 합 :",sum)

print("짝수의 합")
sum = 0
for i in range(0,num+1,2) :
    sum = sum+i  
print("1부터 ",num,"까지의 합 :",sum)

print("홀수의 합")
sum = 0
for i in range(0,num+1,1) :
    sum = sum+i  
print("1부터 ",num,"까지의 합 :",sum)