# 7#Example4.py  按$分隔读取文件
txt = open('fff.txt').read()
ls = txt.split('$')
# f.close()

print(ls)
