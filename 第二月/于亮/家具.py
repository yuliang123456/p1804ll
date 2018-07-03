class house:
    def __init__(self,area,address):
        self.area=area
        self.address=address
        self.items=[]
    def __str__(self):
        a='家的大小是%s 地址在%s 其中包含的家具%s'%(self.area,self.address,(self.items))
        return(a)

    def add_items(self,item):
        if int(self.area) > int(item.area):
            self.area -= item.area
            self.items.append(item.name)
        else:
            print('家具太大了，我家小，进不了')

    #def add_items(self,item):
     #   self.items.append(item.name)


class bed:
    def __init__(self,area,name):
        self.area=area
        self.name=name
    def __str__(self):
        b='已经买好了%s,家的大小是%s,'%(self.name,self.area)
        return(b)
class bed:
    def __init__(self,area,name):
        self.area=area
        self.name=name
    def __str__(self):
        c='已经买好了%s,家的大小是%s,'%(self.name,self.area)
        return(c)
class deng:
    def __init__(self,area,name,color):
        self.area=area
        self.name=name
        self.color=color
    def __str__(self):
        d='买了一个%s,颜色是%s,'%(self.name,self.color)
        return(d)
    def open(self):
        print('打开%s'%self.name)
    def liang(self):
        print('%s亮了'%self.name)
    def close(self):
        print('关闭%s'%self.name)





house1=house(222,'北京')
print(house1)

xiaobed=bed(100,'婴儿床')
print(xiaobed)
house1.add_items(xiaobed)

bigbed=bed(100,'大床')
print(bigbed)
house1.add_items(bigbed)
taideng=deng(20,'台灯','黑色')
print(taideng)
house1.add_items(taideng)
taideng.open()
taideng.liang()
taideng.close()
print(house1)

