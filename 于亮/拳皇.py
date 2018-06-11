class People:
    def __init__(self,name,height,weight):
        self.name = name
        self.height = height
        self.weight = weight
    def jump(self):
        print('%s哇 跳起来一顿下段踢....'%self.name)
    def run(self):
        print('%s哇 跑的挺快啊....'%self.name)
    def zhiquan(self):
        print('%s哇 反过来一个直拳.让你看看...'%self.name)

def bisha(ti):
    ti.jump()
    ti.run()
    ti.zhiquan()

def bisha1(ti):
    ti.run()
    ti.jump()
    ti.zhiquan()
congchao=People('小超','2.5米',200)
congchao.jump()
congchao.run()
congchao.zhiquan()


lvbu=People('吕布','2米',140)
bisha1(lvbu)
#lvbu.jump()
#lvbu.run()
#lvbu.zhiquan()
meinv=People('美女','1米',100)
bisha(meinv)
