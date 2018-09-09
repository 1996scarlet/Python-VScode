# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
from scipy import sparse
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, auc
from sklearn.preprocessing import OneHotEncoder
from sklearn.neural_network import MLPClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB,GaussianNB,BernoulliNB

class ZHX_finial:

    @staticmethod
    def make_roc():
        # load data
        data_root = "D:\pre"
        dfAppAction = pd.read_csv("%s/user_app_actions.csv"%data_root)
        dfTrain = pd.read_csv("%s/train.csv"%data_root)
        dfAd = pd.read_csv("%s/ad.csv"%data_root)
        dfUser = pd.read_csv("%s/user.csv"%data_root)
        dfPosition = pd.read_csv("%s/position.csv"%data_root)

        # process data
        dfTrain = pd.merge(dfTrain, dfAd, on="creativeID")
        dfTrain = pd.merge(dfTrain, dfUser, on="userID")
        dfTrain = pd.merge(dfTrain, dfPosition, on="positionID")
        y_train = dfTrain["label"].values

        train1=train2=train3=dfTrain
        train1["education"].replace(7,method='bfill',inplace=True)
        train2["education"].replace(7,2,inplace=True)
        train3["education"].replace(7,method='ffill',inplace=True)
        # feature engineering/encoding
        enc = OneHotEncoder()

        feats = ["creativeID", "adID", "camgaignID", "advertiserID", "appID" ,\
        "appPlatform","education"]

        feats2 = ["creativeID", "adID", "camgaignID", "advertiserID", "appID" ,\
        "appPlatform","userID","positionID","connectionType"]

        for i,feat in enumerate(feats):
            x_train = enc.fit_transform(dfTrain[feat].values.reshape(-1, 1))
            if i == 0:
                X_train = x_train
            else:
                X_train = sparse.hstack((X_train, x_train))

        for i,feat in enumerate(feats2):
            x_train = enc.fit_transform(train1[feat].values.reshape(-1, 1))
            if i == 0:
                X_train1 = x_train
            else:
                X_train1 = sparse.hstack((X_train1, x_train))

        for i,feat in enumerate(feats):
            x_train = enc.fit_transform(train2[feat].values.reshape(-1, 1))
            if i == 0:
                X_train2 = x_train
            else:
                X_train2 = sparse.hstack((X_train2, x_train))

        for i,feat in enumerate(feats):
            x_train = enc.fit_transform(train3[feat].values.reshape(-1, 1))
            if i == 0:
                X_train3 = x_train
            else:
                X_train3 = sparse.hstack((X_train3, x_train))

        # model training
        lr = LogisticRegression(max_iter=10)
        lr.fit(X_train, y_train)

        lr1 = LogisticRegression(max_iter=10)
        lr1.fit(X_train1, y_train)

        mnb = MultinomialNB()
        mnb.fit(X_train2, y_train)

        mnb2 = MultinomialNB()
        mnb2.fit(X_train1, y_train)

        bnb = BernoulliNB()
        bnb.fit(X_train3, y_train)

        bnb2 = BernoulliNB()
        bnb2.fit(X_train1, y_train)

        fpr, tpr, _ = roc_curve(y_train, lr.predict_proba(X_train)[:,1])
        roc_auc = auc(fpr, tpr)
        fpr1, tpr1, _ = roc_curve(y_train, lr1.predict_proba(X_train1)[:,1])
        roc_auc1 = auc(fpr1, tpr1)
        fpr2, tpr2, _ = roc_curve(y_train, mnb.predict_proba(X_train2)[:,1])
        roc_auc2 = auc(fpr2, tpr2)
        fpr3, tpr3, _ = roc_curve(y_train, bnb.predict_proba(X_train3)[:,1])
        roc_auc3 = auc(fpr3, tpr3)
        fpr4, tpr4, _ = roc_curve(y_train, bnb2.predict_proba(X_train1)[:,1])
        roc_auc4 = auc(fpr4, tpr4)

        fpr5, tpr5, _ = roc_curve(y_train, mnb2.predict_proba(X_train1)[:,1])
        roc_auc5 = auc(fpr5, tpr5)

        # image drawing
        plt.figure()
        plt.title('Receiver Operating Characteristic %d iter' %10)
        plt.plot(fpr, tpr, label = 'default LR AUC = %0.9f' % roc_auc)
        plt.plot(fpr1, tpr1, label = 'cleaned LR AUC = %0.9f' % roc_auc1)
        plt.plot(fpr2, tpr2, label = 'default MLP AUC = %0.9f' % roc_auc2)
        plt.plot(fpr3, tpr3, label = 'default BNB AUC = %0.9f' % roc_auc3)
        plt.plot(fpr4, tpr4, label = 'cleaned BNB AUC = %0.9f' % roc_auc4)
        plt.plot(fpr5, tpr5, label = 'cleaned MLP AUC = %0.9f' % roc_auc5)        
        plt.legend(loc = 'lower right')
        plt.plot([0, 1], [0, 1],'r--')
        plt.xlim([0, 1])
        plt.ylim([0, 1])
        plt.ylabel('True Positive Rate')
        plt.xlabel('False Positive Rate')
        plt.show()