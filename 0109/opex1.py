'''
Created on 2020. 1. 9.
opex1.py : 연산자 연습
@author: gd7
'''
num1 = int(input("첫번째 정수 입력 : "))
num2 = int(input("두번째 정수 입력 : "))
print(num1,"+",num2,"=",(num1+num2))
print(num1,"-",num2,"=",(num1-num2))
print(num1,"*",num2,"=",(num1*num2))
print(num1,"/",num2,"=",(num1/num2)) 
print(num1,"/",num2,"=",(num1//num2)) # //하면 > 정수정수는 정수값으로 가져옴
print(num1,"%",num2,"=",(num1%num2))
print(num1,"**",num2,"=",(num1**num2)) # 제곱형태 3에 2승

print("a"+"b"+"c")
print("abc"*3)
print("""안녕하세요, 홍길동입니다. 반갑습니다. 어쩌구 저쩌구......
안녕하세요, 홍길동입니다. 반갑습니다. 어쩌구 저쩌구......""") #""",''' 끝날때까지 계속 문자열로 인식함