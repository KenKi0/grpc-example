from concurrent import futures

import grpc
import sum_pb2
import sum_pb2_grpc


class SumService(sum_pb2_grpc.SumServiceServicer):
    def Sum(self, request: sum_pb2.Request, context: grpc.ServicerContext) -> sum_pb2.Response:
        return sum_pb2.Response(result=sum(request.operands))


def serve() -> None:
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    sum_pb2_grpc.add_SumServiceServicer_to_server(SumService(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
