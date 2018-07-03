class Car(object):
    def __init__(self,name):
        self.name=name
    def run(self):
        return '正在飞奔'
class Dazhong(Car):
    def run(self):
        return '大众正在跳舞'
class Bmw(Car):
    def run(self):
        return '宝马正在高速行驶'
class Benchi(Car):
    def run(self):
        return '奔驰正在维修'
class Person(object):
    def __init__(self,name):
        self.name=name
    def kai(self,n):

        print('%s在开%s去泡妞'%(self.name,n.run()) )
da=Dazhong('保时捷')
da1=Bmw('宝马750li')
da3=Benchi('奔驰s500')

p=Person('小溪')
p1=Person('小王')
p3=Person('小花')

p.kai(da)
p1.kai(da1)
p3.kai(da3)
