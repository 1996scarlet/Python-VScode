from bus import do_with_train
from bus import logloss
import pandas as pd
from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import BernoulliNB
from sklearn import linear_model

train = pd.read_csv("D://pre/train.csv")
test = pd.read_csv("D://pre/test.csv")

test = do_with_train(test)
train = do_with_train(train)

train_cols = train.columns[1:]

clf = linear_model.LogisticRegressionCV(solver='lbfgs')

#clf = BernoulliNB()
#clf = grid_search.GridSearchCV(linear_model.LogisticRegression(solver='lbfgs'))
clf.fit(train[train_cols], train['label'])

def outRes():
    res = pd.DataFrame()
    res['instanceID'] = test['instanceID']
    proba = clf.predict_proba(test[train_cols])
    res['prob'] = proba[:,1]
    res.to_csv("D://pre/submission.csv")
    return

def outNum():
    proba = clf.predict_proba(train[train_cols])
    #train['prob'] =clf.predict_proba(train[train_cols])
    print (logloss(train['label'],proba[:,1]))
    return

outNum()
#outRes()