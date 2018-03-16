import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier

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

# model training
neigh = KNeighborsClassifier(n_neighbors=2, n_jobs=-1)
neigh.fit(X_train, y_train)
fpr, tpr, threshold = metrics.roc_curve(y_test, neigh.predict_proba(X_test)[:,1])
roc_auc = metrics.auc(fpr, tpr)

print (fpr ,tpr)

# image drawing
plt.title('Receiver Operating Characteristic KNC')
plt.plot(fpr, tpr, label = 'AUC = %0.2f' % roc_auc)
plt.legend(loc = 'lower right')
plt.plot([0, 1], [0, 1],'r--')
plt.xlim([0, 1])
plt.ylim([0, 1])
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.show()