import logging
import random
import typing

import grpc
import sum_stream_pb2
import sum_stream_pb2_grpc


def random_iterator_ints(size: int = 5, min_int: int = 0, max_int: int = 10) -> typing.Iterator[int]:
    logging.info("Started generation")
    for _ in range(size):
        yield random.randint(min_int, max_int)
    logging.info("Finished generation")


def pack(values: typing.Iterator[int]) -> typing.Iterator[sum_stream_pb2.Request]:
    for value in values:
        yield sum_stream_pb2.Request(value=value)


def run() -> None:
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = sum_stream_pb2_grpc.SumServiceStub(channel)
        value_iterator = random_iterator_ints(10_000)
        request_iterator = pack(value_iterator)
        logging.info("Sum is %s", stub.Sum(request_iterator))


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s.%(msecs)03d %(message)s", datefmt="%m/%d/%Y %H:%M:%S")
    run()
