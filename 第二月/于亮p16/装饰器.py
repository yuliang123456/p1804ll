def wai(a):
    def nei(name='员工'):
        if name == '员工':
            a()
        else:
            print('此功能直提供给内部员工使用')
            print('输入的 名字是%s'% name)
    return nei
def wai1(b):
    def nei(mima='123'):
        if mima == '123':
            b()
        else:
            print('密码布正确')
            print('输入的密码是%s '%mima)
    return nei

@wai
def f1():
    print('===f1===')
@wai1
def f2():
    print('===f2===')
@wai
@wai1
def f3():
    print('===f3===')

f1('员工')
f2('123')
f3()
#cc=input('请输入')

#if 'f1' == cc:
#
#    a = wai(f1)
#   a('员工')
#if 'f2'== cc:
#    a = wai(f2)
#    a('员工')

