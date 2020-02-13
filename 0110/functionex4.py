'''
Created on 2020. 1. 10.

@author: gd7
functionex4.py : 1. 리턴값을 두개 반환하기 : 리스트로 반환
                 2. 가변 매개변수 함수 정의
'''
def multi(v1,v2) :
    list=[]
    res1 = v1 + v2
    res2 = v1 - v2
    list.append(res1)
    list.append(res2)
    return list
def paramFunc(* p) : #0개 이상 매개변수
    result = 0
    for i in p :
        result += i
    return result
    

list = []
hap,sub = 0,0
list = multi(100,200)
hap = list[0]
sub = list[1]
print("multi 함수의 리턴값 : %d, %d " %(hap,sub))

## 가변 파라미터 연습
print("paramFunc(10,20)=",paramFunc(10,20))
print("paramFunc(10,20,30)=",paramFunc(10,20,30))

