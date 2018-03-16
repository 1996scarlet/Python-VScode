import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

import seaborn as sns; sns.set()

class QCY_SVM:

    @staticmethod
    def make_data():
        from sklearn.datasets.samples_generator import make_blobs
        X, y = make_blobs(n_samples=50, centers=2, random_state=0, cluster_std=0.60)
        plt.scatter(X[:, 0], X[:, 1], c=y, s=50, cmap='autumn')
        plt.show()

    @staticmethod
    def line_split():
        from sklearn.datasets.samples_generator import make_blobs
        X, y = make_blobs(n_samples=50, centers=2, random_state=0, cluster_std=0.60)
        plt.scatter(X[:, 0], X[:, 1], c=y, s=50, cmap='autumn')
        xfit = np.linspace(-1, 3.5)
        # plt.scatter(X[:, 0], X[:, 1], c=y, s=50, cmap='autumn')
        plt.plot([0.6], [2.1], 'x', color='red', markeredgewidth=2, markersize=10)

        for m, b in [(1, 0.65), (0.5, 1.6), (-0.2, 2.9)]:
             plt.plot(xfit, m * xfit + b, '-k')

        plt.xlim(-1, 3.5)
        plt.show()

    @staticmethod
    def line_space():
        from sklearn.datasets.samples_generator import make_blobs
        X, y = make_blobs(n_samples=50, centers=2, random_state=0, cluster_std=0.60)
        plt.scatter(X[:, 0], X[:, 1], c=y, s=50, cmap='autumn')
        xfit = np.linspace(-1, 3.5)
        # plt.scatter(X[:, 0], X[:, 1], c=y, s=50, cmap='autumn')

        for m, b, d in [(1, 0.65, 0.33), (0.5, 1.6, 0.55), (-0.2, 2.9, 0.2)]:
            yfit = m * xfit + b
            plt.plot(xfit, yfit, '-k')
            plt.fill_between(xfit, yfit - d, yfit + d, 
            edgecolor='none', color='#AAAAAA', alpha=0.4)
        
        plt.xlim(-1, 3.5)
        plt.show()

    def plot_svc_decision_function(model, ax=None, plot_support=True):
        """绘制一个二维支持向量分类器的分类边界"""
        if ax is None:
            ax = plt.gca()
        xlim = ax.get_xlim()
        ylim = ax.get_ylim()
        
        # create grid to evaluate model
        x = np.linspace(xlim[0], xlim[1], 30)
        y = np.linspace(ylim[0], ylim[1], 30)
        Y, X = np.meshgrid(y, x)
        xy = np.vstack([X.ravel(), Y.ravel()]).T
        P = model.decision_function(xy).reshape(X.shape)
        
        # 绘制 decision boundary 和 decision margins
        ax.contour(X, Y, P, colors='k',
                levels=[-1, 0, 1], alpha=0.5,
                linestyles=['--', '-', '--'])
        
        # 绘制支持向量
        if plot_support:
            ax.scatter(model.support_vectors_[:, 0],
                    model.support_vectors_[:, 1],
                    s=300, linewidth=1, facecolors='none');
        ax.set_xlim(xlim)
        ax.set_ylim(ylim)

    @classmethod
    def support_vectors(cls):
        from sklearn.datasets.samples_generator import make_blobs
        X, y = make_blobs(n_samples=50, centers=2, random_state=0, cluster_std=0.60)
        from sklearn.svm import SVC # "支持向量分类器"
        model = SVC(kernel='linear', C=1E10)
        model.fit(X, y)
        plt.scatter(X[:, 0], X[:, 1], c=y, s=50, cmap='autumn')
        cls.plot_svc_decision_function(model)
        plt.show()
    
    @classmethod
    def plot_svm(cls, N=10, ax=None):
        from sklearn.datasets.samples_generator import make_blobs
        X, y = make_blobs(n_samples=200, centers=2,
                        random_state=0, cluster_std=0.60)
        X = X[:N]
        y = y[:N]
        from sklearn.svm import SVC # "支持向量分类器"
        model = SVC(kernel='linear', C=1E10)
        model.fit(X, y)
        
        ax = ax or plt.gca()
        ax.scatter(X[:, 0], X[:, 1], c=y, s=50, cmap='autumn')
        ax.set_xlim(-1, 4)
        ax.set_ylim(-1, 6)
        cls.plot_svc_decision_function(model, ax)
    
    @classmethod
    def compare(cls):
        fig, ax = plt.subplots(1, 4, figsize=(16, 6))
        fig.subplots_adjust(left=0.0625, right=0.95, wspace=0.1)
        for axi, N in zip(ax, [60, 120, 180, 240]):
            cls.plot_svm(N, axi)
            axi.set_title('N = {0}'.format(N))
        plt.show()

    @classmethod
    def make_circle(cls):
        from sklearn.datasets.samples_generator import make_circles
        X, y = make_circles(100, factor=.1, noise=.1)

        from sklearn.svm import SVC # "支持向量分类器"
        clf = SVC(kernel='linear').fit(X, y)

        plt.scatter(X[:, 0], X[:, 1], c=y, s=50, cmap='autumn')
        cls.plot_svc_decision_function(clf, plot_support=False)
        plt.show()
    
    @classmethod
    def plot_circle_svm(cls):
        from sklearn.datasets.samples_generator import make_circles
        X, y = make_circles(100, factor=.1, noise=.1)

        from sklearn.svm import SVC # "支持向量分类器"
        clf = SVC(kernel='rbf').fit(X, y)

        plt.scatter(X[:, 0], X[:, 1], c=y, s=50, cmap='autumn')
        cls.plot_svc_decision_function(clf, plot_support=False)
        plt.show()

    @staticmethod
    def make_dense_data():
        from sklearn.datasets.samples_generator import make_blobs        
        X, y = make_blobs(n_samples=100, centers=2, random_state=0, cluster_std=1.2)
        plt.scatter(X[:, 0], X[:, 1], c=y, s=50, cmap='autumn')
        plt.show()

    @classmethod
    def plot_cr(cls):
        from sklearn.datasets.samples_generator import make_blobs                
        X, y = make_blobs(n_samples=100, centers=2, random_state=0, cluster_std=0.8)

        fig, ax = plt.subplots(1, 4, figsize=(16, 6))
        fig.subplots_adjust(left=0.0625, right=0.95, wspace=0.1)

        from sklearn.svm import SVC # "支持向量分类器"        

        for axi, C in zip(ax, [10.0, 5.0, 1, 0.1]):
            model = SVC(kernel='linear', C=C).fit(X, y)
            axi.scatter(X[:, 0], X[:, 1], c=y, s=50, cmap='autumn')
            cls.plot_svc_decision_function(model, axi)
            axi.scatter(model.support_vectors_[:, 0], model.support_vectors_[:, 1], s=300, lw=1, facecolors='none')
            axi.set_title('C = {0:.1f}'.format(C), size=14)
        plt.show()