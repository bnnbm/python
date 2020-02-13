'''
Created on 2020. 1. 17.

@author: gd7
classex5.py : 추상메서드 예제
'''

class SuperClass :
    #추상메서드
    def method(self) :
        raise NotImplementedError #반드시 오버라이딩 해야함
    
class SubClass1(SuperClass) :
    def method(self):
        print("SubClass1에서 method()를 오버라이딩 함")

class SubClass2(SuperClass) :
#    pass
    def method(self) :
        print("SubClass2에서 method()를 오버라이딩 함")
sub1 = SubClass1()
sub2 = SubClass2()
sub1.method()
sub2.method()