import logging
import typing
from concurrent import futures

import grpc
import range_generator_pb2
import range_generator_pb2_grpc


class RangeService(range_generator_pb2_grpc.RangeServiceServicer):
    def Range(
        self,
        request: range_generator_pb2.Request,
        context: grpc.ServicerContext,
    ) -> typing.Iterator[range_generator_pb2.Response]:
        logging.info("Started generation")
        for value in range(request.start, request.stop, request.step):
            yield range_generator_pb2.Response(value=value)
        logging.info("Finished generation")


def serve() -> None:
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    range_generator_pb2_grpc.add_RangeServiceServicer_to_server(RangeService(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s.%(msecs)03d %(message)s", datefmt="%m/%d/%Y %H:%M:%S")
    serve()
