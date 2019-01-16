"""The Python implementation of the GRPC svm.Greeter server."""

from concurrent import futures
import time

import grpc

import svm_pb2
import svm_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class Greeter(svm_pb2_grpc.GreeterServicer):

    def SayHello(self, request, context):
        return svm_pb2.HelloReply(message='Hello, %s!' % request.name)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    svm_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
