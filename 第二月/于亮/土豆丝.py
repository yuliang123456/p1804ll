class Tudousi:
    def __init__(self):
        self.info='炒土豆丝'
        self.lever=0
        self.Condiment=[]
    def cook(self,sj):
        self.lever+=sj
        if self.lever>=8:
            self.info='炒湖了'
        elif self.lever>=6:
            self.info='炒的火候有点大'
        elif self.lever>=5:
            self.info='炒得火候刚刚好:'
        elif self.lever>=3:
            self.info='炒得半生不熟'
        else:
            self.info='你这炒的没熟'
    def xincondiment(self,Condiment):
        self.Condiment.append(Condiment)
    def __str__(self):
        for i in self.Condiment:
            self.info += i +','
        return'当前的炒土豆丝状态是%s 炒土豆丝用了多长 %d 分钟时间'%(self.info,self.lever)




tds=Tudousi()
guo=Tudousi()
print('首先把锅预热')
print('接下来把豆油放入锅中')
tds.xincondiment('豆油')
guo.cook(4)
print(guo)
print(tds.info)
tds.cook(3)
print(tds.info)
tds.cook(2)
print(tds.info)

tds.xincondiment('孜然')
tds.xincondiment('辣椒油')
tds.xincondiment('豆油')
tds.xincondiment('辣酱')

print(tds)

