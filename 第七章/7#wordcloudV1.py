# 7#wordcloudV1.py
import wordcloud
c = wordcloud.WordCloud()
c.generate("wordcloud  by Python Python Python Python")
c.to_file('pywordcloud.png')
