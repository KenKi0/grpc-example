import logging

import grpc
import range_generator_pb2
import range_generator_pb2_grpc


def run() -> None:
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = range_generator_pb2_grpc.RangeServiceStub(channel)
        result_iterator = stub.Range(range_generator_pb2.Request(start=0, stop=100_000, step=1))
        logging.info("Started iteration")
        for _ in result_iterator:
            ...
        logging.info("Finished iteration")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s.%(msecs)03d %(message)s", datefmt="%m/%d/%Y %H:%M:%S")
    run()
