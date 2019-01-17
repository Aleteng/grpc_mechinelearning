import numpy as np
from sklearn import svm, datasets


# import data
iris = datasets.load_iris()
X = iris.data
y = iris.target

# we create an instance of SVM and fit out data.
C = 1.0  # SVM regularization parameter, learn more about C: https://blog.csdn.net/mingtian715/article/details/54574700
model = svm.LinearSVC(C=C)
model.fit(X, y)
# test, generate an array
test_result_array = model.predict([[5.9 3. 5.1 1.8]])
# from array to list
test_result = test_result_array.tolist()[0]
