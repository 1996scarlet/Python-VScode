# import os

from tkinter import *
import os
from decomp_model import start
from rnomr import ZHX_RNOMR
from IIPWork import ZHX_ROC
from j3 import ZHX_J3
from finial import ZHX_finial

class App:
    def __init__(self,master):

        frame = Frame(master)
        frame.pack()

        #时间序列分割测试
        self.btn_svm_1 = Button(frame, text="time_data_split", command=ZHX_RNOMR.make_plot)
        self.btn_svm_1.pack(side=LEFT)

        #分类器效果测试
        self.btn_svm_2 = Button(frame, text="classifier_ROC", command=ZHX_ROC.make_roc)
        self.btn_svm_2.pack(side=LEFT)

        # J3算法特征选择测试
        self.btn_svm_3 = Button(frame, text="J3", command=ZHX_J3.make_j3)
        self.btn_svm_3.pack(side=LEFT)

        # 时间序列预测DEMO
        self.btn_svm_4 = Button(frame, text="time_demo", command=start)
        self.btn_svm_4.pack(side=LEFT)

        # 最终演示
        self.btn_svm_5 = Button(frame, text="finial", command=ZHX_finial.make_roc)
        self.btn_svm_5.pack(side=LEFT)

root = Tk()
my_app = App(root)
root.mainloop()