class Kaodigua:
    def __init__(self):
        self.info='生地瓜'
        self.lever=0
        self.Condiment=[]
    def cook(self,sj):
        self.lever+=sj
        if self.lever>=8:
            self.info='烤湖了'
        elif self.lever>=6:
            self.info='火候有点大'
        elif self.lever>=5:
            self.info='火候刚刚好:'
        elif self.lever>=3:
            self.info='半生不熟'
        else:
            self.info='生的'
    def xincondiment(self,Condiment):
        self.Condiment.append(Condiment)
    def __str__(self):
        for i in self.Condiment:
            self.info += i +','
        return'当前的地瓜状态是%s 烤地瓜用了多长 %d 分钟时间'%(self.info,self.lever)




digua=Kaodigua()
print(digua.info)
digua.cook(3)
print(digua.info)
digua.cook(2)
print(digua.info)


digua.xincondiment('孜然')
digua.xincondiment('辣椒油')
digua.xincondiment('豆油')
digua.xincondiment('辣酱')

print(digua)

