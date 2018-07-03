'''
class Dog(object):
    __isinstance = None
    def __init__(self):
        pass
    def __new__(cls,*args):
        if cls.__isinstance == None:
            cls.__isinstance=object. __new__(cls)

        return cls.__isinstance
xiaoh=Dog()
xiaox=Dog()
print(id(xiaoh))
print(id(xiaox))

class father(object):
    def __init__(self):
        print('==init===输出')
    def __str__(self):
        return('====str===调用')
    def __new__(cls):
        print('===调用')
        return object.__new__(cls)
    def __del__(self):
        print('====del=调用')
class sun(father):
    pass
he=sun()
print(he)
'''
class People(object):
    __money = 0
    def get_money



