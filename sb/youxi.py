while True
import random
    liang = int(input('我们来猜拳'))
'''
石头=1
剪刀=2
布=3
'''
    xin = random.randint(1,3)
        print('你出的是什么 %d ' % xin)
    if xin==1:
        print('你出的是石头')
    elif xin==2:
        print('你出的是剪刀')
    else:
        print('你出的是布')
    if liang==1:
        print('那我出的是石头')
    elif liang==2:
        print('那我出的是剪刀')
    elif liang==3:
        print('那我出的是布')
    else:
        print('我在逗你玩')
    if ((xin==1 and liang==3) or (xin==2 and liang==1 ) or (xin==3 and liang==2)):
        print('xin 你弱爆了')
    elif xin==liang:
        print('平手，在来')
    else:
        print('xin 恭喜你')
