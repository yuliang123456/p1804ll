'''
def jiecheng(n):
    t=1
    for a in range(1,n+1,1):
        t=t*a
    print(t)
jiecheng(6)
'''
def calNum(num):
    if num >= 1:
        a=num*calNum(num-1)
    else:
        a = 1
    return a
b = calNum(6)
print(b)

