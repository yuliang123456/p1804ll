import random
while True:
#1=石头 2=剪刀 3=布
    wo=int(input('请你除权'))
    pc = random.randint(1,3)
    print('diannaochishen %d'%pc)
    if (wo==1 and pc==2) or (wo==2 and pc==3) or (wo==3 and pc==1):
        print('diannnnn ruobao')
    elif wo==pc:
        print('ping')
    else:
        print('diannaolihai')


