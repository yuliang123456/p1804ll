
class people:
    def __init__(self,name,salary):
        self.__name=name
        self.salary=salary

    def get_name(self):
        return self.__name
    def set_name(self,n):
        self.__name=n
        return self.__name
    def get_salary(self):
        return self.salary
    def __send_msg(self):
        print('验证码发送成功')
    def get_msg(self):

        return self.__send_msg()
xiaohua=people('小花', 6000)
print(xiaohua.get_name() )
xiaohua.set_name('小白')
print(xiaohua.get_name() )
xiaohua.get_msg()
laowang=people('老王',2000)


'''
class people:
    def __init__(self,name,yao,xiong,tun):
        self.name=name
        self.__yao=yao
        self.__xiong=xiong
        self.__tun=tun
    def get_yao(self,n):
        if n =='医生':
            return self.git_yao
        else:
            return 200
cc=people('小超',22,33,44)
s=cc.get_yao('医生:')
print(s)
'''


