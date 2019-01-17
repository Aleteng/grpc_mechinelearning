# grpc_machinelearning
## svm与grpc结合。
svm_server.py在server端运行，svm_client.py在client端运行。
首先在svm目录下执行svm.proto 命令：python3 -m grpc_tools.protoc -I../proto --python_out=. --grpc_python_out=. ../proto/svm.proto
之后在server端和client端分别执行.py脚本。

server端首先训练iris数据集，之后client发起请求，server返回预测结果。
