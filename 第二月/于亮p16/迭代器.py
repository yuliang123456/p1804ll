'''
from collections import Iterable
lis=[i for i in range(1,101) if i%2 !=0]
print(lis)
isinstance(iter[lis],Iterator)

'''

list=[]
fiblist=[]
for i in range(100):
    list.append(i)
list=iter(list)
n = 0
a,b=0,1
while n < 100:
    fiblist.append(b)
    a,b=b,a+b
    n +=1
for i in list:
    if i in fiblist:
        print (i)
