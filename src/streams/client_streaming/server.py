import logging
import typing
from concurrent import futures

import grpc
import sum_stream_pb2
import sum_stream_pb2_grpc


class SumService(sum_stream_pb2_grpc.SumServiceServicer):
    def Sum(
        self,
        request_iterator: typing.Iterator[sum_stream_pb2.Request],
        context: grpc.ServicerContext,
    ) -> sum_stream_pb2.Response:
        result = 0
        logging.info("Started processing")
        for request in request_iterator:
            result += request.value
        logging.info("Finished processing")
        return sum_stream_pb2.Response(result=result)


def serve() -> None:
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    sum_stream_pb2_grpc.add_SumServiceServicer_to_server(SumService(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s.%(msecs)03d %(message)s", datefmt="%m/%d/%Y %H:%M:%S")
    serve()
