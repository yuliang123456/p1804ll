


class A(object):
    __instace=None  #用于保存实例化的对象
    __init_flag=True  #表示init———一次都没有执行
    def __init__(self,name):
        if A.__init_flag==True: #这里表示 第一次执行
            self.name=name
            A.__init_flag=False  #标记未已经执行了一次，以后不要在执行了
    def __new__(cls,*k):
        if cls.__instace ==None:  #表示第一次创建 实例对象
            cls.__instace=object.__new__(cls)
        return cls.__instace  # 将对象的引用传递倒init中
a=A('宝马')
b=A('奥迪')
print(id(a))
print(id(b))
print(a.name)
print(b.name)
