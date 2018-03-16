import pandas as pd
import statsmodels.api as sm
import pylab as pl
import numpy as np
import matplotlib.pyplot as plt

while True:
    number = int(input("输入1/4/6/7，-1退出:"))

    print (number)

    res = pd.DataFrame()

    if number==1:
        res = pd.read_csv("D://IIP-ML-DATA/ENB2012_data.csv")
    elif number==3:
        res = pd.read_csv("D://IIP-ML-DATA/german.csv")
    elif number==6:
        res = pd.read_csv("D://IIP-ML-DATA/lenses.csv")
    elif number==7:
        temp1 = pd.read_csv("D://IIP-ML-DATA/7/20121110035412.csv")
        temp2 = pd.read_csv("D://IIP-ML-DATA/7/20121110035631.csv")
        temp3 = pd.read_csv("D://IIP-ML-DATA/7/20121110035852.csv")
        temp4 = pd.read_csv("D://IIP-ML-DATA/7/20121110040111.csv")
        temp5 = pd.read_csv("D://IIP-ML-DATA/7/20121110040331.csv")
        res = pd.concat([temp1,temp2,temp3,temp4,temp5])
    elif number==-1:
        break
    else:
        continue
    
    res.hist()
    pl.show()
    print (res)