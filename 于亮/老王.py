class Rer:
    def __init__(self.name):
        self.name=name
        self.xue=100

        self.qing=None
    def __str__(self):
        return self.name+'剩余血量为:'
    def anzidan(self,danjia,zidan):
        danjia.baocunzidan(zidan)

    def andanjia(self,qiang,danjia):
        qiang.lianjiednajia(danjia)
    def naqiang(self.qiang):
        self.qiang=qiang
    def kaiqiang(self,diren):
        self.qiang.she(diren)
    def diaoxue(self.shashangli)
        self.xue-=shashangli


class Danjia:
    def __init__(self,rongliang):
        self.rongliang=rongliang
        self.rongnalist=[]

    def __str__(self):
        return'弹夹当抢的子弹数量为:'+str(len(self.rongnalist))
    def baocunzidan(self.zidan):
        if len(self.rongnalist)< self.rongliang:
            self.rongnalist.append(zidan)
    def chuzidan(self):
        if len(self.rongnalist)>0:
            zidan=self.

