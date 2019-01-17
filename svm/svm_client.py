"""The Python implementation of the GRPC svm.Greeter client."""

from __future__ import print_function

import grpc

import svm_pb2
import svm_pb2_grpc

FEATURE = [5.9 3. 5.1 1.8]
FEATURE_str = str(FEATURE)

def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = svm_pb2_grpc.PredictStub(channel)
        response = stub.Prediction(svm_pb2.FlowerFeature(feature=FEATURE_str))
    print("Greeter client received: " + response.message)


if __name__ == '__main__':
    run()
