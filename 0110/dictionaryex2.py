'''
Created on 2020. 1. 10.

@author: gd7
dictionaryex2.py : 딕셔너리 예제2
'''
foods = {"떡볶이":"오뎅","짜장면":"단무지","라면":"김치","맥주":"치킨"}
for i in foods.keys() :
    print("%s => %s" %(i,foods[i]))

#화면에서 음식을 입력받아서 궁합 음식 출력하기
#입력받은 음식값이 "종료"인 경우 프로그램이 종료하기
while True:
    myfood = input(str(list(foods.keys())) + "중 음식명을 입력하세요 (종료 입력시 종료) : ")
    if myfood == "종료" :
        print("등록된 음식의 갯수는 : " + str(len(foods)))
        print("좋아하는 음식  : " + str(list(foods.keys())))
        print("궁합 음식  : " + str(list(foods.values())))
        print(list(foods.items()))
        print(list(foods.items())[-1])
        break
    if myfood in foods :
        print("<%s> 궁합 음식은 <%s>입니다." %(myfood,foods[myfood]))
    else :
        print("등록된 음식이 아닙니다.")
        #등록하는 프로그램 추가하기
        #등록하시겠습니까?(Y/N)? Y인 경우는 등록하기
        answer = input("등록하시겠습니까?(Y/N) : ")
        if answer == "Y" or answer == 'y' :
            newfood = input("궁합 음식을 입력하세요 : ")
            foods[myfood] = newfood
            print("음식이 등록되었습니다.")