from sklearn.metrics import accuracy_score

from sklearn.datasets import load_iris
iris = load_iris()
X = iris.data
y = iris.target

# KNN-Model
from sklearn.neighbors import KNeighborsClassifier
model = KNeighborsClassifier(n_neighbors=1)

# # predict
# model.fit(X, y)
# y_model = model.predict(X)

# from sklearn.metrics import accuracy_score
# accuracy_score(y, y_model)

# from sklearn.cross_validation import train_test_split
# # 对数据集进行划分，一半作为训练集，另一半作为验证集
# X1, X2, y1, y2 = train_test_split(X, y, random_state=0, train_size=0.5)

# # 运用训练集拟合模型
# model.fit(X1, y1)

# # 运用验证集评价模型准确度

# y2_model = model.predict(X2)
# print(accuracy_score(y2, y2_model))

# # 交叉验证
# y2_model = model.fit(X1, y1).predict(X2)
# y1_model = model.fit(X2, y2).predict(X1)
# print(accuracy_score(y1, y1_model), accuracy_score(y2, y2_model))

# # CV交叉验证
# from sklearn.cross_validation import cross_val_score
# print(cross_val_score(model, X, y, cv=5))

# # 每次单独提取一个
# from sklearn.cross_validation import LeaveOneOut
# from sklearn.cross_validation import cross_val_score
# scores = cross_val_score(model, X, y, cv=LeaveOneOut(len(X)))
# print(scores.mean())

# pipline模型
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline

def PolynomialRegression(degree=2, **kwargs):
    return make_pipeline(PolynomialFeatures(degree), LinearRegression(**kwargs))

import numpy as np

# 对数据进行随机取样
def make_data(N, err=1.0, rseed=1):
    rng = np.random.RandomState(rseed)
    X = rng.rand(N, 1) ** 2
    y = 10 - 1. / (X.ravel() + 0.1)
    if err > 0:
        y += err * rng.randn(N)
    return X, y

X, y = make_data(40)


import matplotlib.pyplot as plt
import seaborn; seaborn.set()  # 设置图表的样式

X_test = np.linspace(-0.1, 1.1, 500)[:, None]

# plt.scatter(X.ravel(), y, color='black')
# axis = plt.axis()
# for degree in [1, 3, 5]:
#     y_test = PolynomialRegression(degree).fit(X, y).predict(X_test)
#     plt.plot(X_test.ravel(), y_test, label='degree={0}'.format(degree))
# plt.xlim(-0.1, 1.0)
# plt.ylim(-2, 12)
# plt.legend(loc='best')
# plt.show()

from sklearn.learning_curve import validation_curve
degree = np.arange(0, 21)
train_score, val_score = validation_curve(PolynomialRegression(), X, y, 'polynomialfeatures__degree', degree, cv=7)

# plt.plot(degree, np.median(train_score, 1), color='blue', label='training score')
# plt.plot(degree, np.median(val_score, 1), color='red', label='validation score')
# plt.legend(loc='best')
# plt.ylim(0, 1)
# plt.xlabel('degree')
# plt.ylabel('score');
# plt.show()

# plt.scatter(X.ravel(), y)
# lim = plt.axis()
# y_test = PolynomialRegression(3).fit(X, y).predict(X_test)
# plt.plot(X_test.ravel(), y_test)
# plt.axis(lim)
# plt.show()

X2, y2 = make_data(200)
# plt.scatter(X2.ravel(), y2);

degree = np.arange(21)
train_score2, val_score2 = validation_curve(PolynomialRegression(), X2, y2, 'polynomialfeatures__degree', degree, cv=7)

# plt.plot(degree, np.median(train_score2, 1), color='blue', label='training score')
# plt.plot(degree, np.median(val_score2, 1), color='red', label='validation score')
# plt.plot(degree, np.median(train_score, 1), color='blue', alpha=0.3, linestyle='dashed')
# plt.plot(degree, np.median(val_score, 1), color='red', alpha=0.3, linestyle='dashed')
# plt.legend(loc='lower center')
# plt.ylim(0, 1)
# plt.xlabel('degree')
# plt.ylabel('score')
# plt.show()

# from sklearn.learning_curve import learning_curve

# fig, ax = plt.subplots(1, 2, figsize=(16, 6))
# fig.subplots_adjust(left=0.0625, right=0.95, wspace=0.1)

# for i, degree in enumerate([2, 9]):
#     N, train_lc, val_lc = learning_curve(PolynomialRegression(degree), X, y, cv=7,
#                                          train_sizes=np.linspace(0.3, 1, 25))

#     ax[i].plot(N, np.mean(train_lc, 1), color='blue', label='training score')
#     ax[i].plot(N, np.mean(val_lc, 1), color='red', label='validation score')
#     ax[i].hlines(np.mean([train_lc[-1], val_lc[-1]]), N[0], N[-1], color='gray', linestyle='dashed')

#     ax[i].set_ylim(0, 1)
#     ax[i].set_xlim(N[0], N[-1])
#     ax[i].set_xlabel('training size')
#     ax[i].set_ylabel('score')
#     ax[i].set_title('degree = {0}'.format(degree), size=14)
#     ax[i].legend(loc='best')

# plt.show()

from sklearn.grid_search import GridSearchCV

param_grid = {'polynomialfeatures__degree': np.arange(21),
              'linearregression__fit_intercept': [True, False],
              'linearregression__normalize': [True, False]}

grid = GridSearchCV(PolynomialRegression(), param_grid, cv=7)

grid.fit(X, y)

print(grid.best_params_)

model = grid.best_estimator_

plt.scatter(X.ravel(), y)
lim = plt.axis()
y_test = model.fit(X, y).predict(X_test)
plt.plot(X_test.ravel(), y_test, hold=True);
plt.axis(lim)
plt.show()