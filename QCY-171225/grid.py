import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline

import seaborn as sns; sns.set()

class QCY_GRID:

    def PolynomialRegression(degree=2, **kwargs):
        return make_pipeline(PolynomialFeatures(degree), LinearRegression(**kwargs))

    def make_data(N, err=1.0, rseed=1):
        # 对数据进行随机取样
        rng = np.random.RandomState(rseed)
        X = rng.rand(N, 1) ** 2
        y = 10 - 1. / (X.ravel() + 0.1)
        if err > 0:
            y += err * rng.randn(N)
        return X, y

    @classmethod
    def show_base(cls):
        X, y = cls.make_data(40)
        X_test = np.linspace(-0.1, 1.1, 500)[:, None]

        plt.scatter(X.ravel(), y, color='black')
        axis = plt.axis()
        for degree in [1, 3, 5]:
            y_test = cls.PolynomialRegression(degree).fit(X, y).predict(X_test)
            plt.plot(X_test.ravel(), y_test, label='degree={0}'.format(degree))
        plt.xlim(-0.1, 1.0)
        plt.ylim(-2, 12)
        plt.legend(loc='best')

        plt.show()
    
    @classmethod
    def show_curve(cls):
        X, y = cls.make_data(40)
        from sklearn.learning_curve import validation_curve
        degree = np.arange(0, 21)
        train_score, val_score = validation_curve(cls.PolynomialRegression(), X, y,
                                                'polynomialfeatures__degree', degree, cv=7)

        plt.plot(degree, np.median(train_score, 1), color='blue', label='training score')
        plt.plot(degree, np.median(val_score, 1), color='red', label='validation score')
        plt.legend(loc='best')
        plt.ylim(0, 1)
        plt.xlabel('degree')
        plt.ylabel('score')

        plt.show()

    @classmethod
    def show_best(cls):
        X, y = cls.make_data(40)
        
        X_test = np.linspace(-0.1, 1.1, 500)[:, None]
        plt.scatter(X.ravel(), y)
        lim = plt.axis()
        y_test = cls.PolynomialRegression(3).fit(X, y).predict(X_test)
        plt.plot(X_test.ravel(), y_test);
        plt.axis(lim)

        plt.show()

    @classmethod
    def show_search(cls):
        X, y = cls.make_data(40)
        X_test = np.linspace(-0.1, 1.1, 500)[:, None]
        from sklearn.grid_search import GridSearchCV

        param_grid = {'polynomialfeatures__degree': np.arange(21),
                    'linearregression__fit_intercept': [True, False],
                    'linearregression__normalize': [True, False]}

        grid = GridSearchCV(cls.PolynomialRegression(), param_grid, cv=7)
        grid.fit(X, y)
        model = grid.best_estimator_

        plt.scatter(X.ravel(), y)
        lim = plt.axis()
        y_test = model.fit(X, y).predict(X_test)
        plt.plot(X_test.ravel(), y_test, hold=True);
        plt.axis(lim)

        plt.show()