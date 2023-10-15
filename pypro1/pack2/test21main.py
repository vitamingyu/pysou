import test21singer

def process():
    jungkuk=test21singer.Singer() # 생성자 호출
    print('타이틀 송 : ',jungkuk.title_song)
    jungkuk.sing()
    jungkuk.title_song='정국 찬양가'
    jungkuk.co='하이브'
    print('소속사가 ' + jungkuk.co + '인 가수의 노래 ' + jungkuk.title_song)

    print()
    iu = test21singer.Singer()
    print('타이틀 송 : ',iu.title_song)
    iu.sing()
    # print('소속사가 ' + iu.co + '인 가수의 노래 ' + iu.title_song) iu의 co설정 안하니 오류
    print(id(test21singer.Singer),id(iu)) # 1305101022608 1305056756944

    print()
    bp=test21singer.Singer
    print(id(test21singer.Singer),id(bp)) # 1305101022608 1305101022608
    #dp.sing() # error
    print('타이틀 송 : ',bp.title_song)

if __name__=='__main__':
    process()