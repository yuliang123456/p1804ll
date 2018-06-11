'''
import random
import time
while True:
    a=random.randint(1,100)
    c=random.randint(1,100)
    b=('*'*c)
    print(c*'$')

    print(' '* a,'*')
    time.sleep(0.5)

'''
'''
a=lambda a,b:a+b
print(a(2,3))
a=lambda a,b:a*b
print(a(3,5))
a=lambda a,b:a-b
print(a(15,3))
'''
'''
l=[(lambda a:a**2),(lambda b:b**3),(lambda c:c*4)]
print(l[0](2))
print(l[1](3))
print(l[2](4))
'''
l=[(lambda a,b:a*b-2),(lambda a,b:a+b*2),(lambda a,c,d:a+(c*d))]

print(l[0](2,3))
print(l[1](5,6))
print(l[2](2,6,8))










