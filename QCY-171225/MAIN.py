# import os
# os.system("python d:\Code\PythonSource\QCY-171225\SVM.py")

from tkinter import *
import os
from SVM import QCY_SVM
from face import QCY_FACE
from feature import QCY_FEATURE
from grid import QCY_GRID

# your_path = "python d:\Code\PythonSource\QCY-171225"

class App:
    def __init__(self,master):

        frame = Frame(master)
        frame.pack()

        self.btn_svm_1 = Button(frame, text="SVM-1", command=QCY_SVM.make_data)
        self.btn_svm_1.pack(side=LEFT)

        self.btn_svm_2 = Button(frame, text="SVM-2", command=QCY_SVM.line_split)
        self.btn_svm_2.pack(side=LEFT)

        self.btn_svm_3 = Button(frame, text="SVM-3", command=QCY_SVM.line_space)
        self.btn_svm_3.pack(side=LEFT)

        self.btn_svm_4 = Button(frame, text="SVM-4", command=QCY_SVM.support_vectors)
        self.btn_svm_4.pack(side=LEFT)

        self.btn_svm_5 = Button(frame, text="SVM-5", command=QCY_SVM.compare)
        self.btn_svm_5.pack(side=LEFT)

        self.btn_svm_6 = Button(frame, text="SVM-6", command=QCY_SVM.make_circle)
        self.btn_svm_6.pack(side=LEFT)

        self.btn_svm_7 = Button(frame, text="SVM-7", command=QCY_SVM.plot_circle_svm)
        self.btn_svm_7.pack(side=LEFT)

        self.btn_svm_8 = Button(frame, text="SVM-8", command=QCY_SVM.make_dense_data)
        self.btn_svm_8.pack(side=LEFT)

        self.btn_svm_9 = Button(frame, text="SVM-9", command=QCY_SVM.plot_cr)
        self.btn_svm_9.pack(side=LEFT)

        self.btn_face_1 = Button(frame, text="FACE-1", command=QCY_FACE.make_face)
        self.btn_face_1.pack(side=LEFT)

        self.btn_face_2 = Button(frame, text="FACE-2", command=QCY_FACE.get_model)
        self.btn_face_2.pack(side=LEFT)

        self.btn_face_3 = Button(frame, text="FACE-3", command=QCY_FACE.get_params)
        self.btn_face_3.pack(side=LEFT)

        self.btn_face_4 = Button(frame, text="FACE-4", command=QCY_FACE.get_report)
        self.btn_face_4.pack(side=LEFT)

        self.btn_face_5 = Button(frame, text="FACE-5", command=QCY_FACE.get_matrix)
        self.btn_face_5.pack(side=LEFT)

        self.btn_feature_1 = Button(frame, text="FEATURE-1", command=QCY_FEATURE.get_hog)
        self.btn_feature_1.pack(side=LEFT)

        self.btn_feature_2 = Button(frame, text="FEATURE-2", command=QCY_FEATURE.get_select)
        self.btn_feature_2.pack(side=LEFT)

        self.btn_feature_3 = Button(frame, text="FEATURE-3", command=QCY_FEATURE.get_result)
        self.btn_feature_3.pack(side=LEFT)

        self.btn_grid_1 = Button(frame, text="GRID-1", command=QCY_GRID.show_base)
        self.btn_grid_1.pack(side=LEFT)

        self.btn_grid_2 = Button(frame, text="GRID-2", command=QCY_GRID.show_curve)
        self.btn_grid_2.pack(side=LEFT)

        self.btn_grid_3 = Button(frame, text="GRID-3", command=QCY_GRID.show_best)
        self.btn_grid_3.pack(side=LEFT)

        self.btn_grid_4 = Button(frame, text="GRID-4", command=QCY_GRID.show_search)
        self.btn_grid_4.pack(side=LEFT)
    # def click_svm_1(self):
    #     os.system(your_path + "\SVM-1.py")


root = Tk()
my_app = App(root)
root.mainloop()