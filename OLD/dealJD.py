import pandas as pd
import statsmodels.api as sm
import pylab as pl
import numpy as np

data = pd.read_csv("D://JData/train.csv")

dummy_age = pd.get_dummies(data['age'], prefix='age')
data = data.join(dummy_age.ix[:,'age_16-25岁':])
del data['age']

dummy_sex = pd.get_dummies(data['sex'], prefix='sex')
data = data.join(dummy_sex.ix[:,'sex_1':])
del data['sex']

dummy_lv = pd.get_dummies(data['user_lv_cd'], prefix='lv')
data = data.join(dummy_lv.ix[:,'lv_2':])
del data['user_lv_cd']

dummy_a1 = pd.get_dummies(data['a1'], prefix='a1')
data = data.join(dummy_a1.ix[:,'a1_0':])
del data['a1']

dummy_a2 = pd.get_dummies(data['a2'], prefix='a2')
data = data.join(dummy_a2.ix[:,'a2_0':])
del data['a2']

dummy_a3 = pd.get_dummies(data['a3'], prefix='a3')
data = data.join(dummy_a3.ix[:,'a3_0':])
del data['a3']

dummy_com = pd.get_dummies(data['comment_num'], prefix='com')
data = data.join(dummy_com.ix[:,'com_1':])
del data['comment_num']

dummy_bad = pd.get_dummies(data['has_bad_comment'], prefix='bad')
data = data.join(dummy_bad.ix[:,'bad_1':])
del data['has_bad_comment']

train_cols = data.columns[1:]

logit = sm.Logit(data['type'], data[train_cols])
result = logit.fit()
data['pre'] = result.predict(data[train_cols])

newData = data.loc[:,['user_id','sku_id','pre']]
newData.sort_values(by='pre',ascending = False, inplace=True)

newData.head(10000).to_csv("D://JData/result.csv")