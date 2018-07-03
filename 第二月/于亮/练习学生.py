class student:
    def __init__(self,name,sex,age):
        self.name=name
        self.sex=sex
        self.age=age
        self.chengji={}
    def chengji(self,k,v):
        self.chengji[k]=v #{'语文':60,'数学':60}


    def __str__(self):
        return '学生姓名是'+str(self.name)+'性别'+str(self.sex)+'年龄'+str (self.age) + '成绩'+str(self.chengji)

        f=open('6.txt','w')
        f.write(b)
        f.close()

def hanshu(a):
    for i in range(1,4):
        k=input('请输入科目')
        v=int(input('请输入成绩'))
        a.chengji(k,v)
xue=student('小明','男',18)
xue1=student('小红','女',20)
xue2=student('小刚','男',25)
hanshu(xue)
