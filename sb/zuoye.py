str=('人生苦段,我用python,life is short')
print(len(str))
print(str.startswith('s'))
print(str.count('p'))
print(str.count('i'))
print(str.upper())
print(str.lower())
print(str.title())
str1=str[-20:]
print(str1)


names=['小王','小花','小红','小李子']
for i in names:
    print('%s你好'%i)

my=['汽车','自行车','动车','摩托车']
for a in my:
    print('我喜欢%s'%a)
wo=['新欢','旧爱','恋人','女朋友']
for q in wo:
    print('今晚约%s共进晚餐'%q)
print('旧爱说:今天有事情，去不了了')

wo[1]='佩奇'
print(wo)
for q in wo:
    print('今晚约%s共进晚餐'%q)
i=input('找到了更大的餐厅，还想找几个小伙伴热闹一下')
a=('二狗')
b=('二驴子')
c=('亚瑟')
wo.insert(0,a)
wo.insert(2,b)
wo.append(c)
print(wo)
for q in wo:
    print('今晚约%s共进晚餐'%q)
    print('今晚不好意思了，只能邀请两位，实在很抱歉')
    wo.pop(0)
    l=input('很抱歉')
    print(l)
    print(wo)
    wo.pop(1)
    l=input('很抱歉')
    print(i)
    print(wo)
    wo.pop(2)
    l=input('很抱歉')
    print(i)
    print(wo)
    wo.pop(3)
    l=input('很抱歉')
    print(i)
    print(wo)
    wo.pop(2)
    l=input('很抱歉')
    print(i)
    print(wo)
    print('欢迎两位')
    wo.clear()
print(wo)
