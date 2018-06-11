i =0
for a in range(1,5):
    for b in range(1,5):
        for c in range(1,5):
            if (a!=b)and(b!=c)and(c!=a):
                print('%d,%d,%d'%(a,b,c))
                i=i+1
                print('第%i个数字'%i)



list=[{'北京':{'面积':'1000平','人口':'200w'},'上海':{'面积':':600平','人口':'150w'}}]
for a in list:
    for b,c in a.items():
        for d,e in c.items():
            print(b,d,e)
