#子类调用父类的方法和重写


class Father(object):
    def __init__(self,name):

        self.xing=name
    def kaiche(self):
        print('老司机')
    def eat(self):
        print('能吃')

class Son(Father):

    def __init__(self,name):
        #self.ming=name
        super().__init__(name)

    def kaiche(self):
        super().kaiche()
        print('是个赛车手')
    def eat(self):
        super().eat()
son=Son('大头儿子')
#print(son.ming)
print(son.xing)
son.kaiche()
son.eat()
