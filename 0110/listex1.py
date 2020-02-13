'''
Created on 2020. 1. 10.

@author: gd7
listex1.py : 리스트 예제
   파이선 : 리스트(자바의 배열, List) => []
                딕셔너리(자바의 Map) = {}
                튜플(상수처리된 Map) => ()
'''
a = [0,0,0,0]
b = []
suma, sumb = 0,0
for i in range(0,len(a)) :
    a[i] = int(input(str(i+1) + "번째 값 :"))
    suma += a[i]
    b.append(a[i])
    sumb += b[i]
print(a)
print(b, len(b))
print("a 리스트 합계:", suma)
print("b 리스트 합계:", sumb)