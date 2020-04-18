# 7#Example4.py  按空格分隔读取文件
txt = open('ff.txt',encoding='gbk').read()
ls = txt.split()
txt.close()

print(ls)
