# 클래스의 포함관계 : 국인이네 냉장고(객체)에 음식(객체) 담기
# 객체는 객체를 포함할 수 있다

class Fridge:
    isOpened = False # 냉장고 문 개폐 여부
    foods=[] # 음식물 담기용 리스트

    def open(self):
        self.isOpened = True
        print('냉장고 문 열기')

    def put(self,thing):
        if self.isOpened:
            self.foods.append(thing) # 포함관계
            print('냉장고 속에 음식 담기 완료')
            self.list
        else:
            print('냉장고 문이 닫혀서 음식을 담을 수 없어요')
    def close(self):
        self.isOpened=False
        print('냉장고 문 꼭 닫기')

    def list(self):
        for f in self.foods:
            print('-',fr.name,f.expiry_data)
        print()

# 별도의 모듈 만들어야하는데 그냥 여기서 만들게
class FoodData:
    def __init__(self,name,expiry_date):
        self.name=name
        self.expir_date= expiry_date

# 실행
fr = Fridge()
apple = FoodData('사과','2023-11-05')
fr.put(apple)

fr.open()
fr.put(apple)
fr.close()
print('---')
cola = FoodData('콜라','2025-10-05')
fr.open()
fr.put(cola)
fr.close()
print('---')