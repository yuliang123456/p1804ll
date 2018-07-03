class ren_lei:
    def __init__(self,name,xue,qiang):
        self.name=name
        self.xue=xue
        self.qiang=qiang
    def __str__(self):
        a=self.name+'出现了,'+self.xue +'...' + '拿着:'+self.qiang+'出来了'
        #a='%s,%s,%s'%(self.name,self.xue,self.qiang)
        return(a)
    def an_zidan(self):
        print('%s安装子弹...'%self.name)
    def an_danjia(self):
        print('%s安装弹夹...'%self.name)
    def na_qiang(self):
        print('%s拿抢...'%self.name)
    def kai_qiang(self):
        print('%s开枪...'%self.name)

laowang = ren_lei('老王','满血','AK')
laowang.an_zidan()
laowang.an_danjia()
laowang.na_qiang()
laowang.kai_qiang()
print(laowang)


class zi_dan:
    def __init__(self,name):
        self.name=name
    def sha_di(self):
        print('%s杀害敌人....'%self.name)

zd=zi_dan('杀伤力')
zd.sha_di()



class dan_jia:
    def __init__(self,name,rongliang,baocun):
        self.name=name
        self.rongliang=rongliang
        self.baocun=baocun
    def __str__(self):
        a=self.name+'最大储存子弹'+self.rongliang+self.baocun
        return(a)
    def bao_c(self):
        print('子弹存到%s '%self.name)
    def tan_c(self):
        print('从%s弹出子弹'%self.name)
dan=dan_jia('弹夹','100发','保存的子弹')
dan.bao_c()
dan.tan_c()

