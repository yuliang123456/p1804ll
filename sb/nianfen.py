year=int(input('请问今年是什么年'))
if year%4==0 and year%100!=0:
    print('润年')
elif year%400==0:
    print('润年')
else:
    print('平年')
