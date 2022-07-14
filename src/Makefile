.PHONY: protoc-example
protoc-example:
	python -m grpc_tools.protoc -Iprotos --python_out=message protos/message.proto
	python -m grpc_tools.protoc -Iprotos --grpc_python_out=streams/unary --python_out=streams/unary protos/sum.proto
