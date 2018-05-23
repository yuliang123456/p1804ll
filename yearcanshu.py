





'''
def nian_p(year):
    if year%4==0 and year%100!=0:
        print('润年')
    if year%400==0:
        print('润年')
    else:
        print('平年')
    nian_p(year)
'''



list=[{'北京':{'面积':'1000平','人口':'200w'},'上海':{'面积':'600平','人口':'150w'},'成肚':{'面积':'160平','人口':'500w'}}]
for i in list:
    for a,b in i.items():
        for c,d in b.items():
            print(a,c,d)



'''
def hanshu(x,y):
    print('您要输入的第一个型参%s' %x)
    a=y**2
    print('您要输入的第二个型参%d' %a)
hanshu('好好学习', 2)
'''





