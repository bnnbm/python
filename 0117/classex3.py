'''
Created on 2020. 1. 17.

@author: gd7
classex3.py : 상속 예제, 오버라이딩
'''
class Car :
    speed = 0
    def upSpeed(self, Value) :
        self.speed += Value
        print("현재 속도(부모클래스) : %d" %self.speed)

class Sedan(Car) : #상속표현
    pass           #추가되는 멤버 없는 경우

class Truck(Car) :
    def upSpeed(self, Value) :
        self.speed += Value
        if self.speed > 150 :
            self.speed = 150
        print("현재 속도(자손 클래스) : %d" %self.speed)

class Container :
    room = 1

class MovingCar (Car,Container) :
    pass

sedan1, truck1, mcar = None, None, None
truck1 = Truck()
sedan1 = Sedan()
mcar = MovingCar()
print("이동차량의 방갯수 : ",mcar.room, end="")
mcar.upSpeed(60)
print("트럭 ->", end="")
truck1.upSpeed(200)
print("승용차->",end="")
sedan1.upSpeed(200)