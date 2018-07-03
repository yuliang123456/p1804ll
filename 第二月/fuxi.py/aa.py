'''
for i in range(1,10):
    for j in range(1,i+1):
        k = i*j
        print('%d*%d=%d'%(i,j,k),end='\t')
    print('\n')





l = []
for i in range(3):
    a = int(input('ss'))
    l.append(a)
    l.sort()
    print(l)
'''

import re
a = re.match('1[^012]\d{10}$','12345678887')
print(a.group())
