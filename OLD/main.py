import pandas as pd
import statsmodels.api as sm
import pylab as pl
import numpy as np

test = pd.read_csv("D://pre/test.csv")
train = pd.read_csv("D://pre/train.csv")
user = pd.read_csv("D://pre/user.csv")
create = pd.read_csv("D://pre/ad.csv")
position = pd.read_csv("D://pre/position.csv")

train = pd.merge(train,user, on='userID')
train = pd.merge(train,create,on='creativeID')
train = pd.merge(train,position,on='positionID')
del train['userID']
#del train['clickTime']
del train['positionID']
del train['conversionTime']
#del train['hometown']
#del train['residence']
#del train['advertiserID']
del train['adID']
#del train['camgaignID']
#del train['appID']
del train['creativeID']
#train['intercept'] = 1.0

dummy_con = pd.get_dummies(train['connectionType'], prefix='con')
dummy_tele = pd.get_dummies(train['telecomsOperator'], prefix='tele')
dummy_gen = pd.get_dummies(train['gender'], prefix='gen')
dummy_baby = pd.get_dummies(train['haveBaby'], prefix='baby')
dummy_edu = pd.get_dummies(train['education'], prefix='edu')
dummy_mar = pd.get_dummies(train['marriageStatus'], prefix='mar')
dummy_pla = pd.get_dummies(train['appPlatform'], prefix='pla')
dummy_sit = pd.get_dummies(train['sitesetID'], prefix='sit')
dummy_pos = pd.get_dummies(train['positionType'], prefix='pos')

train = train.join(dummy_con.ix[:,'con_2':])
train = train.join(dummy_tele.ix[:,'tele_2':])
train = train.join(dummy_gen.ix[:,'gen_1':])
train = train.join(dummy_baby.ix[:,'baby_1':])
train = train.join(dummy_edu.ix[:,'edu_1':])
train = train.join(dummy_mar.ix[:,'mar_1':])
train = train.join(dummy_pla.ix[:,'pla_1':])
train = train.join(dummy_sit.ix[:,'sit_1':])
train = train.join(dummy_pos.ix[:,'pos_1':])

del train['connectionType']
del train['telecomsOperator']
del train['gender']
del train['haveBaby']
del train['education']
del train['marriageStatus']
del train['appPlatform']
del train['sitesetID']
del train['positionType']

train_cols = train.columns[1:]

logit = sm.Logit(train['label'], train[train_cols])

result = logit.fit()

#train['pre'] = result.predict(train[train_cols])

#print (train.head())

'''
import scipy as sp
def logloss(act, pred):
  epsilon = 1e-15
  pred = sp.maximum(epsilon, pred)
  pred = sp.minimum(1-epsilon, pred)
  ll = sum(act*sp.log(pred) + sp.subtract(1,act)*sp.log(sp.subtract(1,pred)))
  ll = ll * -1.0/len(act)
  return ll

print (logloss(train['label'],train['pre']))
'''