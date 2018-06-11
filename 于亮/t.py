#1打开源文件
old_file=open('oname','r')
#old_file_name=old_file.name #得到一件打开的文件名
#2读取源文件内容
c=old_file.read()
#3打开一个新的备份文件
p=oname.rfind('.')
name=oname(:p)
namek=oname(p:)
naw_file=open(name+'-副本'+namek,'w')
new_file=open('副本'+oname,'w')
#4将文件写入新文件里
new_file.write(c)
#5关闭打开的文件
ole_file.close()
new_file.close()

