import pandas as pd
import numpy as np
from sklearn.linear_model import Perceptron
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, auc

# load data
data_root = "D:\IIP-ML-DATA"
dfTrain = pd.read_csv("%s/trnOverTraj30K.csv"%data_root, header=None)
dfTest = pd.read_csv("%s/tstOverTraj10K.csv"%data_root, header=None)

# process data
train_colums = dfTrain.columns[:22]
y_train = dfTrain[22]
X_train = dfTrain[train_colums]
X_test = dfTest[train_colums]
y_test = dfTest[22]

iter = 50

for i in range(1,100):
    lp = Perceptron(n_iter = i, n_jobs=-1)
    lp.fit(X_train, y_train)
    lp.fit(X_train, y_train)
    fpr, tpr, threshold = roc_curve(y_test, lp.predict(X_test))
    print ("iter times: %d, fpr: %f, tpr: %f"%(i,fpr[1],tpr[1]))

# model training
lp = Perceptron(n_iter = iter, n_jobs=-1, class_weight="balanced")
lp.fit(X_train, y_train)
fpr, tpr, threshold = roc_curve(y_test, lp.predict(X_test))
roc_auc = auc(fpr, tpr)

lp = Perceptron(n_iter = iter, n_jobs=-1, class_weight=None)
lp.fit(X_train, y_train)
fpr2, tpr2, threshold = roc_curve(y_test, lp.predict(X_test))
roc_auc2 = auc(fpr2, tpr2)

print (fpr ,tpr)
# image drawing
plt.figure()
plt.title('Receiver Operating Characteristic %d iter' %iter)
plt.plot(fpr, tpr, label = 'balanced AUC = %0.2f' % roc_auc)
plt.plot(fpr2, tpr2, label = 'None AUC = %0.2f' % roc_auc2)
plt.legend(loc = 'lower right')
plt.plot([0, 1], [0, 1],'r--')
plt.xlim([0, 1])
plt.ylim([0, 1])
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.show()