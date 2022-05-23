import os
files = os.listdir(".")#获取当前目录下的文件
for filename in files:
    portion = os.path.splitext(filename)#将文件名拆成名字和后缀
    if portion[1] == ".php":#关于后缀
        newname = portion[0] + ".png"
        os.rename(filename, newname)#修改