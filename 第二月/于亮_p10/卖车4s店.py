

class YilanTeCar(object):
    def move(self):
        print('车在移动')
    def stop(self):
        print('.....停车....')


class SuonataCar(object):
    def move(self):
        print('车在移动')
    def stop(self):
        print('.....停车....')
class CaeStore(object):
    def order(self,typeName):

        if typeName=='伊兰特':
            Car = YilanTeCar()
        elif typeName =='索纳塔':
            Car = SuonataCar()
        return car

