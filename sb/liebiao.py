
name_list = []
while True:
    name = input('请输入你的姓名')
    name_list.append(name)
    if name == 'q':
        break
rint(name_list)
print('第三位是: %s' % name_list[3])
print('第五位是: %s' % name_list[5])
print('第八位是: %s' % name_list[8])
print('第十位是: %s' % name_list[10])
#排序
name_list.sort()
print(name_list)
#倒序
name_list.sort(reverse=True)
print(name_list)
#弹出最后一个
print(name_list.pop())
#删除列表第八
del(name_list[8])
#创建新用户
name2 = [1,2,3,4,5,6,7,8]
#追加倒列表最后
name_list.extend(name2)
#查询小明所在位置
print(list_name)
print('小明所在位置:%d'%name_list.index('小明'))
