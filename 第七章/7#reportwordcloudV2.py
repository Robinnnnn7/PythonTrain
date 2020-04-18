# 7#reportwordcloudV2.py
import jieba
import wordcloud
from scipy.misc import imread
mask = imread("fivestart.png")
f = open('paper.txt','r',encoding='utf-8')
t = f.read()
f.close()
ls = jieba.lcut(t)
txt = " ".join(ls)
w = wordcloud.WordCloud(font_path = "msyh.ttc",mask = mask\
                        width = 1000,height = 700,background_color = "white",\
                        )
w.generate(txt)
w.to_file("paperwordcloud.png")
