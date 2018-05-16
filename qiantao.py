sex = input('你的性别')
a=int(input('你的分数'))
if sex == '男':
    if a > 80:
        print ('合格')
    else:
        print ('<80 不及格,继续加油.')
else:
    if a >= 70:
        print ('恭喜')
    else:
        print ('<70 不及格，努力吧.')
