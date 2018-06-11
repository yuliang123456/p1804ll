class student:
    def __init__(self,name,age,chengji):
        self.name=name
        self.age=age
        self.chengji=chengji

    def __str__(self):
        #a=self.name,self.age,self.chengji
        return '%s,%d,%s'%(self.name,self.age,self.chengji)
    def chengji(self):
        print('学生的成绩是%s'%self.name)
    def age(self):
        print('学生的年龄是%d'%self.age)
    def chengji2(self):
        self.chengji.sort(reverse=True)
        self.chengji=self.chengji[0]
        print(self.chengji)
student1=student('小明',22, [11,26,38])
print(student1.name)
print(student1.age)
student1.chengji2()
print(student1)
