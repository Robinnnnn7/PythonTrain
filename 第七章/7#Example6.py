# 7#Example6.py  按 分隔写入文件
ls = ['中国','美国','日本']
f = open('new1.txt','w')
f.write('$'.join(ls))
f.close()
                    
