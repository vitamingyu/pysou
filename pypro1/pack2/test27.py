# 상속 연습
class Person:
    say='난 사람이야~' # 얘넨 공유자원
    nai='20'
    __my = 'private 멤버' # private <= 앞에 __ 2개 붙이면 현재 클래스 내에서만 쓰임

    def __init__(self,nai):
        print('Person 생성자')
        self.nai=nai

    def printInfo(self):
        print('나이:{}, 이야기:{}'.format(self.nai,self.say))

    def hello(self):
        print('안녕')
        print(self.__my)

    @staticmethod
    def kbs(tel):
        print('kbs_static method(클래스 소속) : ', tel)

print(Person.say,Person.nai)
p = Person('25')
print(p.say,p.nai)
p.printInfo()

p.hello()
p.kbs('111-1234')

print('***' * 20)
class Employee(Person):
    subject='근로자'

    def __init__(self):
        print('Employee 생성자')

    def printInfo(self): # method overriding
        print('Employee의 오버라이딩된 printInfo')

    def eprintInfo(self):
        print(self.say,super().say)
        self.hello()
        self.printInfo()
        super().printInfo()

e = Employee()
print(e.say,e.subject)
e.eprintInfo()

print('****'*15)
class Worker(Person):
    say = 'worker의 say'
    def __init__(self,nai):
        print('Worker 생성자')
        super().__init__(nai) # Bound Method call

    def printInfo(self): # Method overriding
        print('Worker에 선언된 printInfo')

    def wprintInfo(self):
        self.printInfo()
        super().printInfo()

w=Worker('30')
print(w.say,w.nai)
w.wprintInfo()

print("^^^"*20)
class Programmer(Worker):
    def __init__(self,age): # nai라 써도 됨 강사님은 가독성을 위해 nai를 씀
        print('Programmer 생성자')
        #Fixme  super().__init__(age) # Bound Call
        Worker.__init__(self,age) #Todo UnBound Call

    def pprintInfo(self):
        self.wprintInfo()

    def hello2(self):
        print('안녕2')
        #print(self.__my) 클래스 밖에서 호출시 오류남 (private 맴버 이므로)




pr = Programmer(33)
print(pr.say,pr.nai)
pr.pprintInfo()
pr.hello2()
pr.kbs('111-1234')
Programmer.kbs('111-1234') # 권장

print('클래스 타입 확인 ===')
print(type(1.2))
print(type(pr))
print(Programmer.__bases__)
print(Worker.__bases__)
print(Person.__bases__) # 모든 클래스의 수퍼클래스 object
