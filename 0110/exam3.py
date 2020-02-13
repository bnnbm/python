'''
Created on 2020. 1. 10.

@author: gd7
exam3.py : 배열의 값의 합과 평균을 구하는 함수 작성하기
'''


def getSum(numlist) :
    return sum(numlist)
def getMean(numlist) :
    #원래 한줄에 사용되는 경우 표시'\ : 연결 문자.'
#    return sum(numlist) / len(numlist) \
#         if len(numlist) > 0 else 0
     if len(numlist) > 0:
         return sum(numlist) / len(numlist)
     else :
        return 0
    
list = [2,3,3,4,4,5,5,6,6,8,8]
print("list의 값의 합 :",getSum(list))
print("list의 값의 평균 :",getMean(list))

list2 = []
print("list의 값의 합 :",getSum(list2))
print("list의 값의 평균 :",getMean(list2))

tp = (2,3,3,4,4,5,5,6,6,8,8) #튜플
print("tp의 값의 합 :",getSum(tp))
print("tp의 값의 평균 :",getMean(tp))