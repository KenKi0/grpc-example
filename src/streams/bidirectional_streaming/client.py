import logging
import typing

import grpc
import square_pb2
import square_pb2_grpc


def pack(values: typing.Iterator[int]) -> typing.Iterator[square_pb2.Request]:
    return (square_pb2.Request(value=value) for value in values)


def run() -> None:
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = square_pb2_grpc.SquareServiceStub(channel)
        request_iterator = pack(i for i in range(10_000))
        response_iterator: typing.Iterator[square_pb2.Response] = stub.Square(request_iterator)
        for response in response_iterator:
            logging.info("Received value %s", response.value)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s.%(msecs)03d %(message)s", datefmt="%m/%d/%Y %H:%M:%S")
    run()
