.PHONY: protoc-example
protoc-example:
	python -m grpc_tools.protoc -Iprotos --python_out=message protos/message.proto
	python -m grpc_tools.protoc -Iprotos --grpc_python_out=streams/unary --python_out=streams/unary protos/sum.proto
	python -m grpc_tools.protoc -Iprotos --grpc_python_out=streams/client_streaming --python_out=streams/client_streaming protos/sum_stream.proto
	python -m grpc_tools.protoc -Iprotos --grpc_python_out=streams/server_streaming --python_out=streams/server_streaming protos/range_generator.proto
	python -m grpc_tools.protoc -Iprotos --grpc_python_out=streams/bidirectional_streaming --python_out=streams/bidirectional_streaming protos/square.proto
