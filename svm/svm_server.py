"""The Python implementation of the GRPC svm.Greeter server."""

from concurrent import futures
import time

import grpc

import svm_pb2
import svm_pb2_grpc

import numpy as np
from sklearn import svm, datasets

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class Predict(svm_pb2_grpc.PredictServicer):

    def __init__(self):
        # import data
        iris = datasets.load_iris()
        X = iris.data
        y = iris.target

        # we create an instance of SVM and fit out data.
        C = 1.0  # SVM regularization parameter, learn more about C: https://blog.csdn.net/mingtian715/article/details/54574700
        self.model = svm.LinearSVC(C=C)
        t = self.model.fit(X, y)
        print(type(t))

    def Prediction(self, request, context):
        # test, generate an array
        test_result_array = self.model.predict([request.feature])
        # from array to list
        test_result = test_result_array.tolist()[0]
        return test_result

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    svm_pb2_grpc.add_PredictServicer_to_server(Predict(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
