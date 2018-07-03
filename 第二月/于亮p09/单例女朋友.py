class Nv(object):
    __girl=None
    __only_you=False
    def __init__(self,name):
        if self.__only_you==False:
            self.name=name
            self.__only_you=True
    def __new__(cls,*k):
        if cls.__girl==None:
            cls.__girl=object.__new__(cls)
        return cls.__girl
a= Nv('小花')
b=Nv('小红')
print(a.name)

print(b.name)
