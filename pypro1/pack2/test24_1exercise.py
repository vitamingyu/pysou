class Machine:
    def Change(self, coin, cup):
        if (coin - 200 * cup) < 0:
            print('요금이 부족합니다')
            return 0
        else:
            change = coin - 200 * cup
            return change

class CoinIn:
    def __init__(self):
        self.machine = Machine()

    def culc(self):
        print('-------- 커피 자판기 ---------')
        coin = int(input('동전을 입력하세요: '))
        cup = int(input('몇 잔을 원하세요: '))

        change = self.machine.Change(coin, cup)
        if change > 0:
            print('{} 잔의 커피가 나왔습니다. 거스름돈은 {}원입니다.'.format(cup,change))
        else:
            print('거스름돈이 없습니다.')

if __name__ == '__main__':
    CoinIn().culc()
