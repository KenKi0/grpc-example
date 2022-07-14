import logging
import random

import grpc
import sum_pb2
import sum_pb2_grpc


def random_list_ints(size: int = 5, min_int: int = 0, max_int: int = 10) -> list[int]:
    return [random.randint(min_int, max_int) for _ in range(size)]


def run() -> None:
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = sum_pb2_grpc.SumServiceStub(channel)
        operands = random_list_ints()
        result = stub.Sum(sum_pb2.Request(operands=operands))
        logging.info("Sum of %s is %s", operands, result)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    run()
