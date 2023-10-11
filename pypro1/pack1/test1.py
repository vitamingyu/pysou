'''
따옴표 세개는
여러 줄 주석
'''
# 한 줄 주석
from datashape.typesets import boolean
print('환영합니다. 파이썬 세상 만세');

var1 = '안녕';  # var1 = "안녕";
print(var1)  # 참조형 변수 : 인스턴스의 주소를 기억
var1 = 5; print(var1)

a = 10
b = 20.5
c = b  # 주소를 치환
print(a, b, c)
print('주소 : ', id(a), id(b), id(c))
print(a is b, a == b)  # is : 주소 비교, == : 값 비교
print(b is c, b == c)

print()
a = [1, 2]
b = a
c = [1, 2]
print(a is b, a == b)
print(a is c, a == c)  # a와 c는 값이 같지만 주소가 다름

print()
A = 1; a = 2;  # 변수는 대소문자 구분
print(A, ' ', a)

print()
import keyword  # 설치는 되었으나 메모리에 로딩되지 않은 모듈 로딩하기
print('예약어 목록 : ' , keyword.kwlist)  # 예약어는 사용자 정의 이름이로 사용하면 안됨

print()
print(10, oct(10), hex(10), bin(10))  # 10 0o12 0xa 0b1010
print(10, 0o12, 0xa, 0b1010)

print('자료형 확인')
print(5, type(5))  # int
print(5.1, type(5.1))  # float
print(5+6j, type(5+6j))  # complex
print(True, type(True))  # bool
print('a', type('a'))  # str

print('묶음형 자료형 ---')
print((1,), type((1,)))  # tuple
print([1], type([1]))  # list
print({1}, type({1}))  # set
print({'key':1}, type({'key':1}))  # dict

print("\n연산자 둘러보기------")
v1 = 3 # 치환
v1 = v2 = v3 = 3
print(v1,v2,v3)

print('a', end=',') # 자바에선 system.out
print('b')
print("=" * 50)

v1 = 1,2,3;
print(v1) # tuple (1, 2, 3)
v1, v2 = 10, 20
print(v1, v2)
v2, v1 = v1, v2
print(v1, v2)
print("=" * 50)

print('값 할당 packing')
*v1, v2 = 1,2,3,4,5
print(v1, v2)
v1, *v2 = 1,2,3,4,5
print(v1, v2)
v1, *v2, v3 = 1,2,3,4,5
print(v1, v2, v3)
print("=" * 50)

# print에 대해
print(format(1.5678, '10.3f'))
print('나는 나이가 %d 이다.'%23)
print('나는 나이가 %s 이다.'%'스물셋')
print('나는 나이가 %d 이고 이름은 %s이다.'%(23, '홍길동'))
print('나는 나이가 %s 이고 이름은 %s이다.'%(23, '홍길동'))
print('나는 키가 %f이고, 에너지가 %d%%.'%(177.7, 100))
print('이름은 {0}, 나이는 {1}'.format('한국인', 33))
print('이름은 {}, 나이는 {}'.format('신선해', 33))
print('이름은 {1}, 나이는 {0}'.format(34, '강나루'))
print("=" * 50)

# 산술, 관계, 논리, 기타연산
print(5 + 3 ,5 * 3, 5 - 3, 5 / 3, 5 // 3, 5 % 3, 5 ** 3) # 8 15 2 1.6666666666666667 1 2 125
print(divmod(5, 3)) # 몫과 나머지를 구한다.
print(3 + 4 * 5, (3 + 4) * 5) # 23 35 연산 우선 순위 : 소괄호() > 산술(*, / > +, -) > 관계 > 논리 > 치환
print(5 > 3, 5 == 3, 5 != 3)
print(5 > 3 and 4 < 3, 5 > 3 or 4 < 3, not(5 >= 3))
print('문자열 더하기 연산', end = ':')
print('가을' + '하늘') # 파이썬은 '와 " 구분하지 않는다.
print("*" * 20)
print("=" * 50)

# 누적
a = 10
a = a + 1
a += 1
# a++ 파이썬에서는 증감연산자는 사용할 수 없다.
print('a :', a)
print('부호 변경 :', a, -a, --a, +a, ++a, a * -1) # 변수 앞에 -붙이거나, 곱을 하면 부호가 변경된다.
print("=" * 50)
print('boolean :', bool(False), bool(0.0), bool(None), bool(""), bool([]), bool({}), bool(set()))
print('boolean :', bool(True), bool(1), bool(-3.4), bool("kbs"), bool([1]), bool({1}), bool(set((1,))))
print("=" * 50)
print("escape 문자\어쩌구 저쩌구")
print('aa\tb') 
print('aa\nb') 
print('aa\bb')
print(r'aa\tb') # r을 붙이면 순수데이터로 인정한다.
print(r'aa\nb') 
print(r'aa\bb')

# python coding 규칙 : PEP 8




