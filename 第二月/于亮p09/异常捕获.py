'''
try:
    print(1)
    print(name)
    print( '%d' %'name')
    print('zhangsan')
    print(True)
except (TypeError,NameError):
    print('程序出现问题')
else:
    print('程序正常')
'''

try:

    print(1)
    a=input('请输入你想要输入的文件')
    b=open('a','w')
    s=b.read()
    print(s)
except Exception as result:
    print('程序出现问题,原因是%s'%result)
else:
    print('程序正常')
finally:
    b.close()
print(b.closed)
