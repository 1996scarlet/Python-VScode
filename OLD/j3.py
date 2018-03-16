from bus import do_with_train
import numpy as np
import pandas as pd

train = pd.read_csv("D://pre/train.csv")
train = do_with_train(train)

train_cols = train.columns[1:]
#train = train[train_cols]

train_type0 = train[train.label==0]
train_type1 = train[train.label==1]

file_object = open('D://first.txt', 'w')

#M = len(train.columns)

def getJ3(train_cols):
    N = len(train.index)
    U = train[train_cols].mean()
    U0 = train_type0[train_cols].mean()
    U1 = train_type1[train_cols].mean()

    Sw = np.matrix(train_type0[train_cols]-U0).T * np.matrix(train_type0[train_cols]-U0)\
     + np.matrix(train_type1[train_cols]-U1).T * np.matrix(train_type1[train_cols]-U1)
    Sw /= N

    Sb = np.matrix(U0-U).T * np.matrix(U0-U) + np.matrix(U1-U).T * np.matrix(U1-U)
    Sm = Sw + Sb
    J3 = np.trace(Sw.I * Sm)
    
    file_object.write(str(train_cols) + '\n' + str(J3))

#first 7 adID
#train_cols = np.concatenate((train_cols[0:7],train_cols[(7+1):]))
#second hometown edu mar

for i in range(len(train_cols)):
    getJ3(np.concatenate((train_cols[0:i],train_cols[(i+1):])))
file_object.close()