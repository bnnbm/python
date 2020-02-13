'''
Created on 2020. 1. 9.

@author: gd7
exam2.py : 초를 입력받아 몇 시간 몇 분 몇 초인지 출력하기
'''
time = int(input("초를 입력하세요  : "))
h = time//3600
m = (time%3600)//60
s = (time%3600)%60
print(h,"시간 ",m,"분",s,"초")

print(time//3600, "시간 ",end="")
time %= 3600;
print(time//60, "분 ",time%60,"초")