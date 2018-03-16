import pandas as pd
import statsmodels.api as sm
import pylab as pl
import numpy as np

def dataClean(myName):
    user = pd.read_csv("D://JData/JData_User.csv")
    del user['user_reg_tm']
    dataCsv = pd.read_csv("D://JData/" + myName + ".csv")
    dataCsv = pd.merge(dataCsv,user, on='user_id')
    return dataCsv

def dataSel(myName):
    data = pd.read_csv("D://JData/" + myName + ".csv")
    data = data[data.cate==8]
    #data = data[(data.type==2) | (data.type==4)]
    del data['time']
    del data['model_id']
    return data

def dataPro(myName):
    product = pd.read_csv("D://JData/JData_Product.csv")
    del product['cate']
    del product['brand']

    data = pd.read_csv("D://JData/" + myName + ".csv")
    data.drop(data.columns[[0,1,5]],axis=1,inplace=True)
    data = pd.merge(data,product,on='sku_id')
    return data

def dataCom(myName):
    comment = pd.read_csv("D://JData/NewComment.csv")
    del comment['dt']

    data = pd.read_csv("D://JData/" + myName + ".csv")
    data.drop(data.columns[[0]],axis=1,inplace=True)
    data = pd.merge(data,comment,on='sku_id')
    return data
'''
dataSel("JData_Action_201602").to_csv("D://JData/JData02.csv")
dataSel("JData_Action_201603").to_csv("D://JData/JData03.csv")
dataSel("JData_Action_201604").to_csv("D://JData/JData04.csv")
'''
'''
dataClean("JData02").to_csv("D://JData/JData02WithUser.csv")
dataClean("JData03").to_csv("D://JData/JData03WithUser.csv")
dataClean("JData04").to_csv("D://JData/JData04WithUser.csv")
'''
#dataCombo("JData02WithUser").to_csv("D://JData/JData02.csv")
#dataCombo("JData03WithUser").to_csv("D://JData/JData03.csv")
#dataCombo("JData04WithUser").to_csv("D://JData/JData04.csv")
'''
dataPro("JData02WithUser").to_csv("D://JData/ProData02.csv")
dataPro("JData03WithUser").to_csv("D://JData/ProData03.csv")
dataPro("JData04WithUser").to_csv("D://JData/ProData04.csv")
'''
dataCom("ProData02").to_csv("D://JData/ComData02.csv")
dataCom("ProData03").to_csv("D://JData/ComData03.csv")
dataCom("ProData04").to_csv("D://JData/ComData04.csv")