import random
list_p=[]#定义一个空列表
def zaocan():#银行菜单
    print('*'* 30)
    print('欢迎来到银行系统，有什么需求。')
    print('1.办卡')
    print('2.注销')
    print('3.查询')
    print('4.存钱')
    print('5.取钱')
    print('6.退出')
money=0
def banka():  #办卡菜单
    global money
    print('*'*30)
    print ('请输入你的个人信息')
    name=input('请输入名字')
    age=int(input('请输入你的年龄'))
    phone=input('请输入你的电话号')
    sf=input('请输入你的身份证号')
    zhuzhi=input('请写入你的家庭住址')
    mima=int(input('请输入密码'))
    dic={'name1':name,'age1':age,'phone1':phone,'sf1':sf,'zhuzhi1':zhuzhi,'mima1':mima,'money1':money}
    list_p.append(dic)
    print('详细信息如下：')
    print('  name : %s '% dic['name1'])
    print('  age : %s '% dic['age1'])
    print('  phone : %s '% dic['phone1'])
    print('  zhuzhi : %s '% dic['zhuzhi1'])

    money =int(input('你需要充值'))
    dic['money1']=money
    print('恭喜你获得新卡号')
    suijishu=random.randint(100000000000000000,9999999999999999999)
    print(suijishu)
    print('成功存了%s'%money)

def chaxun():

    l=input('请输入你要查询的名字')
    passwd=int(input('请输入密码'))
    for dic in list_p:
        if len(dic )!=0:
            if l == dic['name1'] and passwd==dic['mima1']:
                print('*'*30)
                print('姓名: %s'% dic['name1'])
                print('年龄: %s'% dic['age1'])
                print('电话: %s'% dic['phone1'])
                print('住址: %s'% dic['zhuzhi1'])
                print('账户余额%s' %dic['money1'])
        else:
            print('账户不存在')

money=0
def cunqian():  #存钱菜单
    print('欢迎你存钱')
    user=input('请输入你的账户名')
    mima=int(input('请输入密码'))
    for dic in list_p:
        if user == dic['name1']:
            if user ==dic['name1'] and mima ==dic['mima1']:

                print('登录成功')
                ni=int(input('输入你想要存的金额'))
                global money
                dic['money1']=ni+ dic['money1']
                print('显示余额%s'%dic['money1'])
            elif user !=dic['name1'] or mima !=dic['mima1']:

                print('账户或密码错误,请仔细核对后重新登录')




money=0
def quqian():  #取钱菜单
    print('欢迎你取钱')
    user=input('请输入你的账户名')
    mima=int(input('请输入密码'))
    for dic in list_p:
        if user == dic['name1']:
            if user ==dic['name1'] and mima ==dic['mima1']:

                print('登录成功')
                ni=int(input('输入你想要取的金额'))
                global money
                dic['money1'] =dic['money1']-ni
                print('显示余额%s'%dic['money1'])
            elif user !=dic['name1'] or mima !=dic['mima1']:

                print('账户或密码错误,请仔细核对后重新登录')



def zhuxiao():  #注销菜单

    user=input('请输入你的账户名')
    mima=int(input('请输入密码'))
    for dic in list_p:
        if user == dic['name1'] and mima ==dic['mima1']:
            list_p.remove(dic)
            print('注销成功')

while True:
    zaocan()
    xin = input('请选择需要操作的')
    print('你选择的操作是:%s' %xin)
    if xin =='1':
       banka()
    elif xin =='3':
        chaxun()
    elif xin =='4':
        cunqian()
    elif xin =='5':
        quqian()
    elif xin=='2':
        zhuxiao()
    else:
        wo = input('你想要退出吗?Y/N')
        if wo == 'Y':
            print('~'*30)
            print('成功退出,欢迎下次光临')
            break



