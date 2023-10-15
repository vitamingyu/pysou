# 클래스의 포함관계 : 자원의 재활용이 목적 - 약결합
# 완성차를 조립하기 위해 여러 개의 부품을 객체로 만들어 불러다 사용
from test22handle import PohamHandle

class PohamCar:
    turnShowMessage = '정지'

    def __init__(self, ownerName):
        self.ownerName = ownerName
        self.handle = PohamHandle()  # 괄호가 있어야 인스턴스 치환, 없으면 주소 치환. 클래스의 포함

    def turnHandle(self, q):
        if q > 0:
            self.turnShowMessage = self.handle.rightTurn(q)
            # self.안 쓰면 turnhandle안에서 찾고 바로 클래스 위 모듈에서 찾음
            # 그래서 저기 위에 '정지' 못 만나는거임
        elif q < 0:
            self.turnShowMessage = self.handle.leftTurn(q)
        elif q == 0:
            self.turnShowMessage = '직진'
            self.handle.quantity = 0


if __name__ == '__main__':
    tom = PohamCar("톰 아저씨")
    tom.turnHandle(20)
    print(tom.ownerName + "의 회전량은 " + tom.turnShowMessage + str(tom.handle.quantity))
    tom.turnHandle(0)
    print(tom.ownerName + "의 회전량은 " + tom.turnShowMessage + str(tom.handle.quantity))
    print()
    oscar=PohamCar("오스카 형")
    oscar.turnHandle(-10)
    print(oscar.ownerName + "의 회전량은 " + oscar.turnShowMessage + str(oscar.handle.quantity))
