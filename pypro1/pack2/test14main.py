# 사용자 정의 모듈 call
from pypro1 import moduleTest

print('뭔가를 하다가... 다른 모듈 호출')

import test14other

print('score : ',test14other.score)
print(test14other.__file__) # 경로명
print(test14other.__name__) # 모듈명

list1 = [1,2]
list2=[3,4]
test14other.listHap(list1,list2)

def abc():
    if __name__ == '__main__':
        print('메인 모듈이야')
abc()

print()
test14other.kbs()
from test14other import kbs, Mbc, score
kbs()
Mbc()
print(score)

# 다른 패키지 내의 모듈 읽기
import pypro1.moduleTest.test14etc
moduleTest.test14etc.Hap(5, 3)

from pypro1.moduleTest.test14etc import Cha
Cha(5, 3)

import test14etc2
test14etc2.Gob(5, 3)
from test14etc2 import Nanugi
Nanugi(5, 3)