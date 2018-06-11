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
    mima=int(input('请输入你的密码'))
    zhuzhi=input('请写入你的家庭住址')
    dic={'name1':name,'age1':age,'phone1':phone,'mima1':mima,'zhuzhi1':zhuzhi}
    print(dic)
    list_p.append(dic)
    print(list_p)
    suijishu=random.randint(100000000000000000,9999999999999999999)#随机生成的卡号
    print(suijishu)
    print('恭喜你获得新卡号')
    for dic in list_p:

        mima=int(input('请您再次确认卡号密码'))
        if dic['mima1']==mima:
            print('恭喜你设置成功')
            print('成功办卡%s请充值')
            global money
            money =int(input('你需要充值'))
            print('成功存了%s'%money)
            break
        else:
            print('密码错误，请从新输入')
                #print('卡被锁死，请24小时后重新输入')
                #mima=int(input('请您再次确认卡号密码'))
          # if dic['mima1']!=mima:

           #     print('*'*30)
            #    print('你已经输入三次错误')
             #   print('卡被锁死，请24小时后重新输入')
def chaxun():
    a=input('几十分大家看立即开始')
    for dic in list_p:
        if(dic['name1']==a):
            print('name : %s'% dic['name1'])
    #print('显示账户余额%s'%money)
money=0
def cunqian():
    print('欢迎你存钱')
    mima=int(input('请输入密码'))
    a=1
    for dic in list_p:
        while a<=3:
            if dic['mima1']==mima:
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
    mima=int(input('请输入密码'))
    b=1
    for dic in list_p:
        while b<=3:
            if dic['mima1']==mima:
                print('登录成功')
                ta=int(input('输入你想取的金额'))
                global money
                money=money-ta
                print('显示余额%s'%money)
                break
            else:
                print('密码错误,从新输入')
            b = b +1
while True:
    zaocan()
    kehu = input('请选择需要操作的')
    print('你选择的操作是:%s' %kehu)
    if kehu =='1':
       banka()
    elif kehu =='2':
       chaxun()
    elif kehu =='3':
       cunqian()
    elif kehu =='4':
       quqian()
    else:
        wo = input('你想要推出吗?Y/N')
        if wo == 'Y':
            print('*'*30)
            print('成功推出银行系统')
            break



