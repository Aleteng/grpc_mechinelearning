"""The Python implementation of the GRPC svm.Greeter client."""

from __future__ import print_function

import grpc

import svm_pb2
import svm_pb2_grpc

FEATURE = [5.9,3.,5.1,1.8]

def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = svm_pb2_grpc.PredictStub(channel)
        features = svm_pb2.FlowerFeature()
        features.feature.extend(FEATURE)
        print(type(features))
        response = stub.Prediction(features)
    print("Greeter client received: %s" %response.result)


if __name__ == '__main__':
    run()
