'''
Created on 2020. 1. 9.

@author: gd7
strex1.py : 문자열 처리하기
            문자열을 배열 처리 가능함
'''
print("안녕하세요")
print("안녕하세요"[0])
print("안녕하세요"[4])
print("안녕하세요"[-1])
#부분문자열
print("안녕하세요"[1:3]) #1번인덱스부터 2번인덱스까지 부분문자열 출력
print("안녕하세요"[:3]) #0번 인덱스~2번인덱스
print("안녕하세요"[3:]) #3번인덱스부터 끝까지 출력
print("안녕하세요"[::2]) #앞부터 2칸씩 건너서
print("안녕하세요"[::-1]) #뒤부터 1칸씩 건너서
print(type("안녕하세요"))
print("'안녕하세요' 문자열 길이 : ",len("안녕하세요"))
#len = len("안녕하세요")
print(len)
print(type(len))
a = "hello"
cnt = 0
for i in range(0,len(a)) :
    if(a[i] == 'l') :
        cnt+=1
print("l 문자의 갯수 =",cnt)
print("l 문자의 갯수 =",a.count('l'))
print("h 문자의 갯수 =",a.count('h'))
print("l 문자의 위치 =",a.find('l'))
print("a 문자의 위치 =",a.find('a'))
print("l 문자의 위치 =",a.index('l'))
print("a 문자의 위치 =",a.index('a')) #찾는 문자가 없으면 에러처리함