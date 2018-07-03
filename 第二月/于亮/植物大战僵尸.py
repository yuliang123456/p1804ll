
class xrk:
    def __init__(self,name):
        self.name=name
    def caiguang(self):
        print('%s补充能量' %self.name)
xiang=xrk('向日葵')
xiang.caiguang()

class wd:
    def __init__(self,name,color,leixing,xueliang):
        self.name=name
        self.color=color
        self.leixing=leixing
        self.xueliang=xueliang
    def yaotou(self):
        print('%s摇头'%self.name)
    def fapao(self):
        print('%s进行炮弹攻击'%self.name)
    def __str__(self):
        a=self.name + self.color + '类型:' + self.leixing + self.xueliang +'状态'
        #a='%s豌豆,%s颜色,%s类型,%s血量' %(self.name,self.color,self.leixing,self.xueliang)
        return(a)
wandou=wd('豌豆','绿色','进攻','满血')
wandou1=wd('豌豆','蓝色','进攻','满血')
wandou.yaotou()
wandou.fapao()
print(wandou)
print(wandou1)
class jg:
    def __init__(self,name,xueliang,leixing):
        self.name=name
        self.xueliang=xueliang
        self.leixing=leixing
    def zdang(self):
        print('%s阻挡僵尸偷吃食物'%self.name)
    def __str__(self):
        a=self.name+'在' +self.xueliang+'状态下'+self.leixing

        #a='%s坚果,%s血量,%s类型' %(self.name,self.xueliang,self.leixing)
        return(a)
x=jg('坚果','满血','防御')
x.zdang()
print(x)
class js:
    def __init__(self,name,color,xueliang,leixing,sudu):
        self.name=name
        self.color=color
        self.xueliang=xueliang
        self.leixing=leixing
        self.sudu=sudu
    def go(self):
        print('%s僵尸缓缓走来'%self.name)
    def eat(self):
        print('%s僵尸前进吃食物'%self.name)
    def out(self):
        print('%s僵尸收到了炮弹的攻击'%self.name)
    def __str__(self):
        a=self.name + '僵尸出现了'+ self.color + '的光芒'+ self.xueliang+'点血量' + self.sudu +' 前进'

        #a='%s僵尸,%s颜色,%s血量,%s类型,%s速度'%(self.name,self.color,self.xueliang,self.leixing,self.sudu)
        return(a)
jiangshi=js('普通','黑色','100','进攻','匀速')
jiangshi1=js('变异','红色','80','进攻','快速')
jiangshi.go()
x.zdang()
jiangshi.eat()
x.zdang()
wandou.fapao()
jiangshi.out()
print(jiangshi)
print(jiangshi1)

