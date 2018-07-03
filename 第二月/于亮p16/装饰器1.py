
def wai (fun):
    def nei (*args,**kwargs):
        print('传递的参数是',args)
        print('=========')
        fun(*args,**kwargs)
    return nei
@wai
def foo(*args,**kwargs):
    print('...............')
    print('参数是',args)
    print('参数是',kwargs)

foo(1,2,3,4,5,'g',a=1,c='2')


#4返回值
def wai(fun):   #传递的函数的引用
    def nei():    #传递的 函数多需要的 参数
        print('.函数调用前的检查........')
        return(fun())
    return nei
@wai
def foo():
    return('=========')
print(foo())

#5增加外部 参数传递

def jsp(a):
    def wai(fun):   #传递的函数的引用
        def nei():    #传递的 函数多需要的 参数
            print('.函数调用前的检查........')
            print('判断需要使用参数 这里接受',a)
            return(fun())
        return nei
    return wai
@jsp(12345)
def foo():
    return('=========')
print(foo())
