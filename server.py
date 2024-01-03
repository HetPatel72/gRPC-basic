from concurrent import futures
import grpc
import hello_world_pb2_grpc


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    hello_world_pb2_grpc.add_HelloWorldServicer_to_server(hello_world_pb2_grpc.HelloWorldServicer(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()