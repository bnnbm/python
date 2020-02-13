'''
Created on 2020. 1. 13.

@author: gd7
'''
import operator
a,list = {},[]
while True :
    if len(a) == 0 :
        print("2:등록, 3:수정, 4:삭제, 9:종료")
        num = input("번호를 입력하세요=>")
        if num == "9" :
            break
        elif num == "2" :
            eng = input("등록할 영어 단어 =>")
            ko = input("등록할 한글 단어 =>")
            a[eng] = ko
        elif num != "2" or "3" or "4" or "9" :
            print("번호가 틀립니다.")
            continue
    if len(a) != 0 :
        print("1:조회, 2:등록, 3:수정, 4:삭제, 9:종료")
        num = input("번호를 입력하세요=>")
        if num == "9" :
            break
        elif num == "2" :
            eng = input("등록할 영어 단어 =>")
            if eng in a :
                print("이미 등록된 단어입니다.")
            else :
                ko = input("등록할 한글 단어 =>")
                a[eng] = ko
        elif num == "1" :
            print("=========================등록된 단어 갯수 : " + str(len(a)))
            arraylist = int(input("정렬기준(1:영문기준,2:한글기준 ,그외값 입력순서)=>"))
            if arraylist == 1 :
                print("=======사 전  내 용(영문기준 정렬) =========")
                list = sorted(a.items(), key=operator.itemgetter(0))
                print(list)
            elif arraylist == 2 :
                print("=======사 전  내 용(한글기준 정렬) =========") 
                list = sorted(a.items(), key=operator.itemgetter(1))
                
                print(list)
            elif arraylist != 1 or 2 :
                print("=======사 전  내 용  =========")
                for i in a.keys() :
                    print("%s = %s" %(i,a[i]))
        elif num =="3" :
            eng = input("수정할 영어 단어=>")
            if eng in a :
                a[eng] = input("등록할 한글 단어=>")
            else :
                print("등록된 단어가 아닙니다.")
        elif num =="4" :
            eng = input("삭제할 영어 단어=>")
            if eng in a :
                del a[eng]
            else :
                print("등록된 단어가 아닙니다.")
        elif num != "1" or "2" or "3" or "4" or "9" :
            print("번호가 틀립니다.")  