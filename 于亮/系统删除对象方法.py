#__init__ 系统默认方法，用于类的初始化信息，类创建的时候被调用
#__str__  系统默认方法，用于返回print 打印类对象时 显示的内容，当打印对象时候被调用
#__del__  系统默认方法，当创建的对象被删除/销毁的时候  系统自动调用


#两种请况 __del__会被系统自动调用执行
#1。当尅程序执行结束，系统自动销毁 美亚引用的对象（不再使用的对象）
#2。当对象 被彻底删除/销毁的时候 系统会自动的调用 del方法   引用

class animal:
    def __init__(self,name):
        self.name=name
        self.f=open('name.txt','r')
    def get_name()
        self,name=self.f.read
        return self.name


    def __del__(self):
        self.f.write(self,name)
        self.f.close()
        print('111111111111')
dog=animal('小猫')
print(dog.get_name())
dog.f =open('name.txt','w')
dog.f.write('旺财')

print('....................')


'''
dog = animal('金毛')
del dog
psterint('.............')i
'''
