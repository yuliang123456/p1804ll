class Donkey(object):
    '''驴类'''
    def manzou(self):
        print('走的慢。。。')
class Horse(object):
    '''马类'''
    def mali(self):
        print('耐力组 跑的快')
class Mule(Donkey,Horse):
    def jiao(self):
        print('唱歌')
    pass
骡子=Mule()
骡子.manzou()
骡子.mali()
骡子.jiao()
print(Mule.__mro__)
