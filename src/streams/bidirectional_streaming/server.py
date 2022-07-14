import logging
import typing
from concurrent import futures

import grpc
import square_pb2
import square_pb2_grpc


def unpack(request_iterator: typing.Iterator[square_pb2.Request]) -> typing.Iterator[int]:
    return (request.value for request in request_iterator)


def square(values: typing.Iterator[int]) -> typing.Iterator[int]:
    for value in values:
        logging.info("Received value %s", value)
        yield value * value


def pack(values: typing.Iterator[int]) -> typing.Iterator[square_pb2.Response]:
    return (square_pb2.Response(value=value) for value in values)


class SquareService(square_pb2_grpc.SquareServiceServicer):
    def Square(
        self,
        request_iterator: typing.Iterator[square_pb2.Request],
        context: grpc.ServicerContext,
    ) -> typing.Iterator[square_pb2.Response]:
        values = unpack(request_iterator)
        squared_values = square(values)
        return pack(squared_values)


def serve() -> None:
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    square_pb2_grpc.add_SquareServiceServicer_to_server(SquareService(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s.%(msecs)03d %(message)s", datefmt="%m/%d/%Y %H:%M:%S")
    serve()
