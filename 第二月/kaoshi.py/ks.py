class PeopleYl(object):
    def __init__(self):
        self.__money=60
    def getMoney(self):
        return self.__money
    def setMoney(self,value):
        if isinstance(value,int):
            self.__money = value
class li_si(PeopleYl):
    def __init__(self,money):
        self.money = money
    def set (self):
        money = property(getMoney,setMoney)
f2=li_si(70)
f2.money=10
print(f2.money)




