'''
Created on 2020. 1. 10.

@author: gd7
tupleex1.py : 튜플 예제
   변경불가 리스트
'''
tp1 = (10,20,30) #튜플 선언 () 표시함
print(tp1)
#tp1.append(10) 변경 불가라서 사용불가
print(tp1[0],tp1[1],tp1[2])
#tp1[0] = 100 변경 불가라서 사용불가

#꼭 변경하고 싶을때
list = list(tp1) #리스트 변환
list.append(40)
tp1 = tuple(list) #리스트를 튜플로 변환
print(tp1)
print("tp1의 크기",len(tp1),"list의 크기",len(list))
print("tp1[1:3]",tp1[1:3],"list[1:3]=",list[1:3])
print("tp1[:3]=",tp1[:3],"list[:3]=",list[:3])
print("tp1[2:]=",tp1[2:],"list[2:]=",list[2:])
print("tp1[::2]=",tp1[::2],"list[::2]=",list[::2])