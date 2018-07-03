'''
class animal:
    def __init__(self):
        self.legs =4
        self.weiba=1
    def eat(self):
        print('会吃')
    def sleep(self):
        print('会睡')
    def drink(self):
        print('会喝水')

class dog(animal):
    def jiao(self):
        print('会叫')

a=dog()
a.jiao()
a.eat()
a.sleep()
a.drink()
'''

class Father(object):
    def __init__(self):
        self.xing='王'
        self.__height='180'
    def kaiche(self):
        print('是个老司机//')
    def __dubo(self):
        print('小赌移情，大赌。。。。')

class Son(Father):
    pass
大头儿子=Son()
print(大头儿子.xing)
大头儿子.height='160'
print(大头儿子.height)
大头儿子.kaiche()
大头儿子.dubo()



