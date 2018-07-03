'''
f =open('test.txt','w')
f .write('sjfkjskjkf')
f.close()

f =open('test.txt','r')
f.read()
f.close()


f=open('test.txt','a')
f.write('你好')
f.close()


t=open('test1.txt','w')
t.write('春眠布觉小\n处处蚊子咬\n夜来风雨声\n')
t.close()
t=open('test1.txt','r')
b=t.readlines()
for i in b:
    s=i[:len(i)-1]
    print(s+'*')
t.close()
t1=open('test1.txt','a')
t1.write('春眠布觉小\n处处蚊子咬\n夜来风雨声\n')
t1.close()
'''

t=open('test1.txt','w')
t.write('春眠布觉小\n处处蚊子咬\n')
t.close()
t=open('test1.txt','r')
a=t.readline()
b=t.tell()
print('第一行内容是:%s'%a)
print('位置是%d'%b)
a=t.readline()
b=t.tell()
print('第二行内容是:%s'%a)
print('位置是%d'%b)
t.seek(0,0)
t=open('test1.txt','r')
a=t.readline()
print(a)
t.close()

