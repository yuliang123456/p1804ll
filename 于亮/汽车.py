class car:
    def __init__(self,lu_num,co_num):

        self.lunzi=lu_num
        self.color=co_num
    def run(self):
        print('%s 跑起来了..%d轮子的 %s颜色的车 '%( self.name,self.lunzi,self.color))
    def jiao(self):
        print('%s 叫起来了...'% self.name)
    def zhuiwei(self):
        print('%s 到家了还追呢...'% self.name)
baoma=car(4,'黑色')
baoma.name='宝马'
baoma.run()
baoma.jiao()
baoma.zhuiwei()

aodi=car(5,'粉色')
aodi.name='奥迪'
aodi.run()
aodi.jiao()
aodi.zhuiwei()

