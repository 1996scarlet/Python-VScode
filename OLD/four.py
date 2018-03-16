import pandas as pd
from scipy import sparse
from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import Perceptron,LogisticRegression
from sklearn.naive_bayes import MultinomialNB,BernoulliNB
from sklearn.tree import DecisionTreeRegressor
from sklearn import svm
from sklearn.neural_network import MLPClassifier
from bus import logloss

# # load data
# data_root = "D:\pre"
# dfTrain = pd.read_csv("%s/train.csv"%data_root)
# dfAd = pd.read_csv("%s/ad.csv"%data_root)
# dfUser = pd.read_csv("%s/user.csv"%data_root)
# dfPosition = pd.read_csv("%s/position.csv"%data_root)

# # process data
# dfTrain = pd.merge(dfTrain, dfAd, on="creativeID")
# dfTrain = pd.merge(dfTrain, dfUser, on="userID")
# dfTrain = pd.merge(dfTrain, dfPosition, on="positionID")

# dfTrain = dfTrain[0::100]
# # clean data
# dfTrain = dfTrain[dfTrain.clickTime<270000]
# dfTrain.clickTime //= 10000
# dfTrain["age"].replace(0,20,inplace=True)

# y_train = dfTrain["label"].values

# # feature engineering/encoding
# enc = OneHotEncoder()

# feats = ["creativeID", "adID", "camgaignID", "advertiserID", "appID",\
# "userID","positionID","age","sitesetID","positionType"]

# # feature engineering/encoding
# for i,feat in enumerate(feats):
#     x_train = enc.fit_transform(dfTrain[feat].values.reshape(-1, 1))
#     if i == 0:
#         X_train = x_train
#     else:
#         X_train = sparse.hstack((X_train, x_train))

# # model training
# lr = LogisticRegression(max_iter=5)
# lr.fit(X_train, y_train)

# mnb = MultinomialNB()
# mnb.fit(X_train, y_train)

# bnb = BernoulliNB()
# bnb.fit(X_train, y_train)

# sm = svm.SVC(probability=True)
# sm.fit(X_train, y_train)

# dt = DecisionTreeRegressor(max_depth=5)
# dt.fit(X_train, y_train)

# pr = Perceptron()
# pr.fit(X_train, y_train)

# sr = svm.SVR()
# sr.fit(X_train, y_train)

# mlp = MLPClassifier(max_iter=2)
# mlp.fit(X_train, y_train)

# print(logloss(y_train,lr.predict(X_train)))
# print(logloss(y_train,mnb.predict_proba(X_train)[:,1]))
# print(logloss(y_train,bnb.predict_proba(X_train)[:,1]))
# print(logloss(y_train,sm.predict_proba(X_train)[:,0]))
# print(logloss(y_train,dt.predict(X_train)))
# print(logloss(y_train,pr.predict(X_train)))
# print(logloss(y_train,sr.predict(X_train)))
# print(logloss(y_train,mlp.predict_proba(X_train)[:,1]))


# from sklearn.metrics import roc_curve, auc
# fpr, tpr, _ = roc_curve(y_train, lr.predict_proba(X_train)[:,1])
# roc_auc = auc(fpr, tpr)

# fpr2, tpr2, _ = roc_curve(y_train, mnb.predict_proba(X_train)[:,1])
# roc_auc2 = auc(fpr2, tpr2)

# fpr3, tpr3, _ = roc_curve(y_train, bnb.predict_proba(X_train)[:,1])
# roc_auc3 = auc(fpr3, tpr3)

# fpr4, tpr4, _ = roc_curve(y_train, sm.predict_proba(X_train)[:,0])
# roc_auc4 = auc(fpr4, tpr4)

# fpr5, tpr5, _ = roc_curve(y_train, dt.predict(X_train))
# roc_auc5 = auc(fpr5, tpr5)

# fpr6, tpr6, _ = roc_curve(y_train, pr.predict(X_train))
# roc_auc6 = auc(fpr6, tpr6)

# fpr7, tpr7, _ = roc_curve(y_train, sr.predict(X_train))
# roc_auc7 = auc(fpr7, tpr7)

# fpr8, tpr8, _ = roc_curve(y_train, mlp.predict_proba(X_train)[:,1])
# roc_auc8 = auc(fpr8, tpr8)

# # image drawing
# import matplotlib.pyplot as plt
# plt.figure()
# plt.title('Classifier')

# plt.plot(fpr, tpr, label = 'LogisticRegression AUC = %0.5f' % roc_auc)
# plt.plot(fpr2, tpr2, label = 'MultinomialNB AUC = %0.5f' % roc_auc2)
# plt.plot(fpr3, tpr3, label = 'BernoulliNB AUC = %0.5f' % roc_auc3)
# plt.plot(fpr4, tpr4, label = 'SVC AUC = %0.5f' % roc_auc4)
# plt.plot(fpr5, tpr5, label = 'DecisionTreeRegressor AUC = %0.5f' % roc_auc5)
# plt.plot(fpr6, tpr6, label = 'Perceptron AUC = %0.5f' % roc_auc6)
# plt.plot(fpr7, tpr7, label = 'SVR AUC = %0.5f' % roc_auc7)
# plt.plot(fpr8, tpr8, label = 'MLPClassifier AUC = %0.5f' % roc_auc8)

# plt.legend(loc = 'lower right')
# plt.plot([0, 1], [0, 1],'r--')
# plt.xlim([0, 1])
# plt.ylim([0, 1])
# plt.ylabel('True Positive Rate')
# plt.xlabel('False Positive Rate')
# plt.show()
import matplotlib.pyplot as plt
import numpy as np
xx=np.arange(5)
xxx = [0.101836371677,0.115236356366,0.14732355057,0.124056544514,0.100090151582]
plt.title("Logloss lower is better")
plt.bar(xx,xxx)
plt.xticks(xx,("LSTM","MNN","RNN","GRU","DGR"))
plt.show()