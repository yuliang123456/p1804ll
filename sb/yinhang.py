import random
list_p=[]#定义一个空列表
def zaocan():#银行菜单
    print('*'* 30)
    print('欢迎来到银行系统，有什么需求。')
    print('1.办卡')
    print('2.显示')
    print('3.查询')
    print('4.存钱')
    print('5.取钱')
    print('6.退出')
def banka():
    print('*'*30)
    print ('请输入你的个人信息')
    name=input('请输入名字')
    age=int(input('请输入你的年龄'))
    phone=input('请输入你的电话号')
    zhuzhi=input('请写入你的家庭住址')
    mima=int(input('请输入密码'))
    dic={'name1':name,'age1':age,'phone1':phone,'zhuzhi1':zhuzhi,'mima1':mima}
    list_p.append(dic)
   # print(list_P)
    print('详细信息如下：')
    print('  name : %s '% dic['name1'])
    print('  age : %s '% dic['age1'])
    print('  phone : %s '% dic['phone1'])
    print('  zhuzhi : %s '% dic['zhuzhi1'])
    global money

    money =int(input('你需要充值'))
    print('恭喜你获得新卡号')

    suijishu=random.randint(100000000000000000,9999999999999999999)
    print(suijishu)
    #print('恭喜你获得新卡号')
   # money =int(input('你需要充值'))
    print('成功存了%s'%money)
   # print(list_p)
    '''
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
    print('成功存了%s'%moneyi)

    '''
def xianshi():
    print('显示所有资料')
    for i in list_p:
        print(i)
def chaxun():

    l=input('请输入你要查询的名字')
    passwd=int(input('请输入密码'))
    for dic in list_p:
        if l == dic['name1']:
            if passwd==dic['mima1']:
                print('*'*30)
                print('姓名: %s'% dic['name1'])
                print('年龄: %s'% dic['age1'])
                print('电话: %s'% dic['phone1'])
                print('住址: %s'% dic['zhuzhi1'])
                print('显示金额%s' %money)


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
        xianshi()
    elif xin =='3':
        chaxun()
    elif xin =='4':
        cunqian()
    elif xin =='5':
        quqian()
    else:
        wo = input('你想要推出吗?Y/N')
        if wo == 'Y':
            print('成功推出')
            break



