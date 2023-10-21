# 클래스의 상속
class Animal: # 부모클래스
    def __init__(self):
        print('Animal 생성자')
    def move(self):
        print('움직이는 생물')

class Dog(Animal): # 자손클래스, 파생클래스
    def __init__(self):
        print('댕댕이 생성자')
    def my(self):
        print('난 댕댕이야~')

dog1=Dog()
dog1.my()
dog1.move()

print()
class Horse(Animal):
    pass

horse1=Horse()
horse1.move()
