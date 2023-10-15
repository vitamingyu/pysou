# singer type의 객체 생성
class Singer:
    title_song='대한민국' # 기본으로 다 public임

    def sing(self):
        msg='노래는 '
        print(msg, self.title_song)