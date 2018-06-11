
class wd:
    def __init__(self,name,sex,age,zdli):
        self.name=name
        self.sex=sex
        self.age=age
        self.zdli=zdli
    def cczd(self):
        print('%s'%self.name)
    def zwxl(self):
        print('%s'%self.name)
    def dryx(self):
        print('%s'%self.name)
    def __str__(self):
        a=self.name + self.sex + self.age + self.zdli +'1000'
        return(a)
wy=wd('苍井井','女','18','初始战斗力')
wy1=wd('东尼木木','男','20','初始战斗力')
wy2=wd('波多多','女','19','初始战斗力')

wy.cczd()
wy.zwxl()
wy.dryx()
print(wy)
print(wy1)
print(wy2)
class wd:
    def __init__(self,name,zhand,zdli):
        self.name=name
        self.zhand=zhand
        self.zdli=zdli
    def cczd(self):
        print('%s草丛战斗'%self.name)
    def zwxl(self):
        print('%s自我修炼'%self.name)
    def dryx(self):
        print('%s多人游戏'%self.name)
    def __str__(self):
        a=self.name + self.zhand + self.zdli +'1000'
        return(a)
w=wd('苍井井','草丛战斗','消耗战斗力')
w1=wd('东尼木木','草丛战斗','消耗战斗力')
w2=wd('波多多','草丛战斗','消耗战斗力')

wy.cczd()
w.cczd()
w.zwxl()
w.dryx()
print(wy)
print(w)
print(w1)
print(w2)
wy1.cczd()
w.cczd()
w.zwxl()
w.dryx()
print(wy1)
print(w)
print(w1)
print(w2)

















'''
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
'''
