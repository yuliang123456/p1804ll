#name = 1
#while name <= 1:
print('欢迎使用计算机')
   # name = name + 1

def jia(x,y):
    return(x+y)
def jian(x,y):
    return(x-y)
def cheng(x,y):
    return(x*y)
def chu(x,y):
    return(x/y)

a=int(input('请输入第一个数字'))
while True:

    b=input('请输入符号,或输入q推出')
    while (b != '+' and b != '-' and b != '*' and b != '/' and b != 'q'):
        print('非法输入，请正确输入如：+ - * /')
        b=input('请输入符号,或输入q推出')

    if b == 'q':
        break

    c=int(input('请输入第二个数字'))

    if b == '+':
        a = jia(a,c)
        print(a)
    elif b == '-':
        a = jian(a,c)
        print(a)
    elif b == '*':
        a = cheng(a,c)
        print(a)
    else:
        a = chu(a,c)
        print(a)

