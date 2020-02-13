'''
Created on 2020. 1. 10.

@author: gd7
setex1.py : set 예제  => {}
'''
set1 = {1,2,3,4,5}
print(set1)
set2 = {1,2,3,4,5,1,2,3,4,5}
print(set2)
set3 = {5,6,7,8}
print(set3)

#교집합
print("set1과 set3의 교집합",set1 & set3)
print("set1과 set3의 교집합",set1.intersection(set3))
#합집합
print("set1과 set3의 합집합",set1 | set3)
print("set1과 set3의 합집합",set1.union(set3))