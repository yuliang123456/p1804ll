a = 1
while a <= 9:
    b = 1
    while b <= a:
        print('%d*%d=%d'%(a,b,a*b),end='\t')
        b = b + 1
    a = a + 1
    print('\n')
