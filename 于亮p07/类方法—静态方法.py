
#实例 属 性 方法
#类 属性 方法


class People(object):
    guoji='china'  # 类属性
    def __init__(self):
        self.name='小明'  #实例属性
    def get_name(self):   #实例方法
        return self.name
    @classmethod
    def get_guoji(cls):
        return cls.guoji

print(People.guoji)
print(People.get_guoji())


class People(object):
    guoji='usa'
    def get_name(self):
        return self.name
    @classmethod
    def get_guoji(cls):
        return cls.guoji()
print(People.guoji)
print(People.get_guoji())




class People(object):
    guoji = china
    def __init__(self):
        self.name=小明
    def get_name


