class DogYl(object):
    __isinstand=None
    def __init__(self,name):
        pass
    def __new__(cls):
        if cls.__isinstand==None:
            cls.__isinstand=object.__init__(cls)
        return cls.__isinstand

xiaohua=DogYl()
xiaohong=DogYl()
print(id(xiaohua))
print(id(xiaohong))
