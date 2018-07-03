class people:
    ：def __init__(self,name,sex,age):
        self.name=name
        self.sex=sex
        self.age=age
        self.li={}
    def add_items(self,k,v):
        self.li[k]=v
    def __str__(self):
        return '学生姓名是'+str(self.name)+'性别'+str(self.sex)+'年龄'+str(self.age)+'成绩'+str(self.li)+'\n'
    def chengji(self):
        for i in range(1,4):
            k=input('请输入你的科目')
            v=input('请输入你的成绩')
            self.add_items(k,v)
bai=people('白','女','18')
da=people('王','男','20')
print(str(bai))
bai.chengji()
print(str(bai))
print(str(da))
da.chengji()
print(str(da))


f=open('chengji.txt','w')
f.write(str(bai))
f1=open('chengji.txt','a')

f1.write(str(da))
f.close()
f1.close()


