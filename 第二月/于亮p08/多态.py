
class Duck(object):
    def walk(self):
        print('小黄鸭在走两步')
    def swim(self):
        print('小黄鸭在湖中游泳')
class People(object):

    def walk(self):
        print('老王在走两步')

    def swim(self):
        print('老王在游泳')
def Func(obj):
    obj.walk()
    obj.swim()
duck=Duck()
p01=People()
Func(p01)


class Dog(object):
    def game(self):
        return '普通玩耍'
class Xtq(Dog):
    def game(self):
        return '天上飞'
class Person():
    def play_with_dog(self,dog):
        print('人在和',dog.game())
d=Dog()
p=Person()

p.play_with_dog(d)















