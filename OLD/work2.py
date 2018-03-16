import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def showPictures(x):
    fig,(ax0,ax1) = plt.subplots(nrows=2,figsize=(9,6))
    #第二个参数是柱子宽一些还是窄一些，越大越窄越密
    ax0.hist(x,40,normed=1,histtype='bar',facecolor='yellowgreen',alpha=0.75)
    ##pdf概率分布图，一万个数落在某个区间内的数有多少个
    ax0.set_title('pdf')
    ax1.hist(x,20,normed=1,histtype='bar',facecolor='pink',alpha=0.75,cumulative=True,rwidth=0.8)
    #cdf累计概率函数，cumulative累计。其实就是分位数图的柱形表示
    ax1.set_title("cdf")
    fig.subplots_adjust(hspace=0.4)
    plt.show()

xa = [19,18,18,15,18,11,16,19,17,17,20,17,19,20,20,15,15,16]
xb = [19,15,20,20,17,18,18,15,16,18,15,19,20,19,19,16,17,13,15]
showPictures(xa)
showPictures(xb)
showPictures(xa+xb)
