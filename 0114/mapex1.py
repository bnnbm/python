'''
Created on 2020. 1. 14.

@author: gd7
'''
before = ["2019","07","15"]
print(type(before[0]))
after = list(map(int,before))
print(type(after[0]))
num = int("100") + 1
print(num)

mylist = [1,2,3,4,5]
#map을 이용하여 mylist 각각의 값에 10을 더하기
add =lambda num:num+10
mylist = list(map(add,mylist))
print(mylist)

list1 = [1,2,3,4]
list2 = [10,20,30,40]
#haplist 리스트에  list1과 list2의 각각의 더한 값을 저장하기
#haplist = []
hap = lambda num1,num2:num1+num2
#for i in range(len(list1)) :
#    haplist.append(hap(list1[i],list2[i]))
haplist = list(map(hap,list1,list2))
haplist = list(map(lambda num1,num2:num1+num2,list1,list2))    
print(haplist)