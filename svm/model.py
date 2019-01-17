import numpy as np
from sklearn imprt svm, datasets

class Model(object):
    def __init__(self,model):
       iris = datasets.load_iris()
       X = iris.data
       y = iris.target
       # we create an instance of SVM and fit out data.
       C = 1.0  # SVM regularization parameter, learn more about C: https://blog.csdn.net/mingtian715/article/details/54574700
       model = svm.LinearSVC(C=C)
       self.model = model.fit(X, y)

