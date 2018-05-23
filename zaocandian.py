import random
list_p=[]
def zaocan():
    print('*'* 30)
    print('欢迎来到银行系统，有什么需求。')
    print('1.办卡')
    print('2.查询')
    print('3.存钱')
    print('4.取钱')
    print('5.退出')
def banka():
    print('*'*30)
    print ('请输入你的个人信息')
    name=input('请输入名字')
    age=int(input('请输入你的年龄'))
    phone=input('请输入你的电话号')
    zhuzhi=input('请写入你的家庭住址')
    dic={'name1':name,'age1':age,'phone1':phone,'zhuzhi1':zhuzhi}
    list_p.append(dic)
    sb=random.randint(111111111111111111,182222222222222222)
    print(sb)
    print('恭喜你获得新卡号')
    while True:
        mima=int(input('请输卡号密码'))
        if mima==123:
            print('恭喜你成功登录')
            break
        else:
            print('密码错误,从新输入')
    print('成功办卡%s请充值'%dic['name1'])
    global money
    money =int(input('你需要充值'))
    print('成功存了%s'%money)
def chaxun():

    print('登录成功')
    print('显示余额%s'%money)
money=0
def cunqian():
    print('欢迎你存钱')
    a=1
    while a<=3:
        mima=int(input('请输入密码'))
        if mima==123:
            print('登录成功')
            ni=int(input('输入你想要存的金额'))
            global money
            money=money+ni
            print('显示余额%s'%money)
            break
        else:
            print('密码错误,从新输入')
        a = a +1
def quqian():
    print('欢迎你来取钱')
    while True:
        mima=int(input('请输入密码'))
        if mima==123:
            print('登录成功')
            break
        else:
            print('密码错误，请从新输入')
    ta=int(input('输入你想取的金额'))
    global money
    money=money-ta
    print('显示余额%s'%money)
while True:
    zaocan()
    xin = input('请选择需要操作的')
    print('你选择的操作是:%s' %xin)
    if xin =='1':
       banka()
    elif xin =='2':
       chaxun()
    elif xin =='3':
       cunqian()
    elif xin =='4':
       quqian()
    else:
        wo = input('你想要推出吗?Y/N')
        if wo == 'Y':
            print('成功推出')
            break



