class Jisuanqi(object):
    __instance=None
    __flag=False
    def __init__(self,name):
        if Jisuanqi.__flag == False:
            self.name=name
            Jisuanqi.__flag=True
    def __new__(cls,k):
        if cls.__instance==None:
            cls.__instance=object.__new__(cls)
            return cls.__instance
    def jisq(self):
        while True:
            try:
                a=int(input('请输入一个数字'))
                c=input('输入 + or - or * or /')
                b=int(input('请输入第二个数字'))
                if c=='+':
                    print(a+b)
                elif c=='-':
                    print(a-b)
                elif c=='*':
                    print(a*b)
                elif c=='/':
                    print(a/b)
                d=int(input('1.继续运算 2.结束运算'))
                if d ==2:
                    break
            except Exception as result:
                print('程序异常，原因是:%s'%result)
f=Jisuanqi('计算器')
print(f.name)
f.jisq()


