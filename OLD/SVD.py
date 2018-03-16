# -*- coding: utf-8 -*-
"""
Created on Tue Oct 03 15:53:43 2017
    通过SVD对共现矩阵X进行奇异值分解来实现语料词向量的相关度分析
    语料：我喜欢可爱的。我喜欢小姐姐。我年轻啊。
@author: sunxu
"""
import numpy as np
import matplotlib.pyplot as plt
from pylab import *

la = np.linalg
words = ["I","like","enjoy","deep","learning","NLP","flying","."]

#矩阵记录上下文出现的次数
X = np.array([
[0,2,1,0,0,0,0,0],
[2,0,0,1,0,1,0,0],
[1,0,0,0,0,0,1,0],
[0,1,0,0,1,0,0,0],
[0,0,0,1,0,0,0,1],
[0,1,0,0,0,0,0,1],
[0,0,1,0,0,0,0,1],
[0,0,0,0,1,1,1,0]])

mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False

U, s, Vh = la.svd(X, full_matrices=False)

for i in range(len(words)):
    plt.text(U[i,0],U[i,1],words[i])

plt.title("通过SVD分解算法生成词向量并计算相关度")
plt.xlim(-1, 1)
plt.ylim(-1, 1)
plt.show()

# ticks = time.time()
# print (time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()) )