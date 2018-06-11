name=input('请输入要复制的文件名')
old_file = open(name,'r')
new_file =open('bebi_laowang.txt','w')
content=old_file.read()
new_file.write(content)

