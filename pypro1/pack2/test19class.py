# class : 멤버로 변수와 메소드를 포함한 집합체, 객체 중심의 독립적인 프로그래밍이 가능함. OOP구현
class Car:
    handle = 0
    speed = 0

    def __init__(self,name,speed):
        self.name=name
        self.speed=speed

    def showData(self):
        km='킬로미터'
        msg='속도 : ' + str(self.speed)+km
        return msg

print(Car.handle)

car1 = Car('tom',80)
print('car1 : ',car1.handle,car1.name,car1.speed) # 0 tom 80
car1.color = ('보라') # car1 객체
print('car1 : ',car1.color)
print()
car2 = Car('james',100)
print('car2 : ',car2.handle,car2.name,car2.speed)
print()
print(Car.handle,car1.handle,car2.handle)
print(Car.speed,car1.speed,car2.speed)
print(car1.color) # 나머지 car와 car2로 찍으면 오류남 color객체 없으니
print(Car,car1,car2)
print(id(Car),id(car1),id(car2)) # 3개의 객체니 주소도 다 다름
print(car1.__dict__) # 객체의 멤버 확인
print(car2.__dict__) # 객체의 멤버 확인
print('----메소드-----')
print('car1 : ', car1.showData())
print('car2 : ', car2.showData())

car1.speed=55
car2.speed=88
print('car1 : ',car1.showData())
print('car2 : ',car2.showData())
print()
Car.handle=1
print('car1 : ',car1.handle,car1.name,car1.speed) # 1 tom 55
print('car2 : ',car2.handle,car2.name,car2.speed) # 1 james 88
