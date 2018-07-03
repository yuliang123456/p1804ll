class Cat:
    def eat(self):
        print('%s 在吃鱼,'%self.name)
    def drink(self):
        print('%s 在喝酒,'%self.name)
    def introduce(self):
        print('我的名字%s，我今年%d岁了'%(self.name,self.age))

tom = Cat()
tom.age = 60
tom.color='black'
tom.name ='tom'
tom.introduce()
tom.eat()

lanmao = Cat()
lanmao.name = '蓝猫'
lanmao.age = 21
lanmao.color = 'red'
lanmao.introduce()
lanmao.eat()
