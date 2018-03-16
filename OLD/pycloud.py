# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 18:53:43 2017
    我今天就是要教你如何使用jieba来进行分词
    并用wordcloud绘制关键词肖像
@author: sunxu
"""
import matplotlib.pyplot as plt
from scipy.misc import imread
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import jieba
 
text_from_file_with_apath = open("D://Desk/2.txt",encoding = 'UTF-8').read()
frog_coloring = imread("D://Desk/C0.png")

wordlist_after_jieba = jieba.cut(text_from_file_with_apath, cut_all = True)
wl_space_split = " ".join(wordlist_after_jieba)

stops = STOPWORDS.copy()
stops.add("你们")
stops.add("他们")
stops.add("一个")
stops.add("我们")
stops.add("什么")
stops.add("这个")
stops.add("就是")

wc = WordCloud(background_color="white",random_state=57,
stopwords=stops,mask=frog_coloring)

# wc.font_path="simsun.ttc"   # 宋体
wc.font_path="simhei.ttf"   # 黑体

image_colors = ImageColorGenerator(frog_coloring)

wc.generate(wl_space_split)

plt.imshow(wc.recolor(color_func=image_colors))
plt.axis("off")
plt.show()