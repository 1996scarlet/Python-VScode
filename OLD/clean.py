# -*- coding: utf-8 -*-

import pandas as pd
from scipy import sparse
from sklearn.linear_model import BayesianRidge
from sklearn.preprocessing import OneHotEncoder
from sklearn.naive_bayes import MultinomialNB,GaussianNB,BernoulliNB
from sklearn.tree import DecisionTreeRegressor

# load data
data_root = "D:\pre"
dfTrain = pd.read_csv("%s/train.csv"%data_root)
dfAd = pd.read_csv("%s/ad.csv"%data_root)
dfUser = pd.read_csv("%s/user.csv"%data_root)
dfPosition = pd.read_csv("%s/position.csv"%data_root)

# process data
dfTrain = pd.merge(dfTrain, dfAd, on="creativeID")
dfTrain = pd.merge(dfTrain, dfUser, on="userID")
dfTrain = pd.merge(dfTrain, dfPosition, on="positionID")

# clean data
dfTrain = dfTrain[dfTrain.clickTime<270000]
dfTrain.clickTime //= 10000
dfTrain["age"].replace(0,20,inplace=True)

y_train = dfTrain["label"].values

# feature engineering/encoding
enc = OneHotEncoder()
# feats = ["creativeID", "adID", "camgaignID", "advertiserID", "appID",\
#  "appPlatform","userID","positionID","connectionType","telecomsOperator",\
#  "age","gender","education","sitesetID","positionType","clickTime","haveBaby",\
#  "hometown"]

feats = ["creativeID", "adID", "camgaignID", "advertiserID", "appID",\
"userID","positionID","age","sitesetID","positionType"]

# feature engineering/encoding
for i,feat in enumerate(feats):
    x_train = enc.fit_transform(dfTrain[feat].values.reshape(-1, 1))
    if i == 0:
        X_train = x_train
    else:
        X_train = sparse.hstack((X_train, x_train))

# model training
gnb = GaussianNB()
gnb.fit(X_train, y_train)

mnb = MultinomialNB()
mnb.fit(X_train, y_train)

bnb = BernoulliNB()
bnb.fit(X_train, y_train)

from sklearn.metrics import roc_curve, auc
fpr, tpr, _ = roc_curve(y_train, gnb.predict_proba(X_train)[:,1])
roc_auc = auc(fpr, tpr)

fpr2, tpr2, _ = roc_curve(y_train, mnb.predict_proba(X_train)[:,1])
roc_auc2 = auc(fpr2, tpr2)

fpr3, tpr3, _ = roc_curve(y_train, bnb.predict_proba(X_train)[:,1])
roc_auc3 = auc(fpr3, tpr3)

# image drawing
import matplotlib.pyplot as plt
plt.figure()
plt.title('Classifier')
plt.plot(fpr, tpr, label = 'GaussianNB AUC = %0.9f' % roc_auc)
plt.plot(fpr2, tpr2, label = 'MultinomialNB AUC = %0.9f' % roc_auc2)
plt.plot(fpr3, tpr3, label = 'BernoulliNB AUC = %0.9f' % roc_auc3)
plt.legend(loc = 'lower right')
plt.plot([0, 1], [0, 1],'r--')
plt.xlim([0, 1])
plt.ylim([0, 1])
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.show()