class MyError(Exception):
    def __init__(self,name):
        self.name=name

def get_pwd():
    a=input('请你输入用户名')
    if a !='123':
        raise MyError('用户名不正确')
def get_ming():
    a=input('请你输入密码')
    if a!='111':
        raise MyError('密码不正确')
    else:
        print('登录成功')
try:
    get_pwd()
    get_ming()
except Exception as re:
    print('遇到你的异常是%s'%re)
