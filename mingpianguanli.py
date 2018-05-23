list1=[]
def syestenmMenu():
    print('*'*30)

    print('欢迎使用名片管理系统')

    print('1.新建名片')
    print('2.显示全部')
    print('3.查询名片')
    print('4.删除')
    print('5.退出系统')
    print('*'*30)
def xinjian():
    name = input('请输入你的名字')
    age = int(input('输入你的年龄'))
    com = input('请输入公司名')
    phone_num = input('请输入手机号')
    dic = {'name1':name,'age1':age,'company':com,'phone':phone_num}
    list1.append(dic)
    print(list1)
    print('名片保存成功，姓名是：%s' % dic['name1'])
def xianshi():
    print('显示所有名片')
    for i in list1:
        print(i)
    print('显示所有名片列表')

def chaxun():
    wo = input('选择你要查询的名字')
    for i in list1:
        if wo == i['name1']:
            print('*'*30)
            print('姓名: %s' % i['name1'])
            print('公司: %s' % i['company'])
            print('年龄: %d' % i['age1'])
            print('手机号: %s' % i['phone'])
def shanchu():
    ni = input('选择你要删除的名字')
    for dic  in  list1:
        if(dic['name1']==ni):
            list1.remove(dic)
    print('成功删除')

syestenmMenu()

while True:
    user=int(input('你输入的是什么数字'))
    if user == 1:
        print('新建名片')
        xinjian()
    elif  user ==2:
        print('显示全部')
        xianshi()
    elif user ==3:
        print('查询名片')
        chaxun()
    elif user ==4:
        print('删除')
        shanchu()
    else:
        ni = input('你确定要推出吗？Y/N')
        if (ni=='Y'):
            print('成功退出')
            break
