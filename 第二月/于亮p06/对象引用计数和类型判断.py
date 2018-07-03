import sys
class people:
    def __init__(self,name,salary):
        self.__name=name
        self.salary=salary

xiaohua01=people('小花01',500)
xiaohua02=xiaohua01
xiaohua03=xiaohua01

print(sys.getrefcount(xiaohua01)) #对象被引用了多少次，数量显示要比实际引用次数多
print(isinstance(xiaohua03,people)) # True :Flase 查询对象是否属于 制定的类
