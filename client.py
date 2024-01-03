import grpc
import hello_world_pb2_grpc
from hello_world_pb2 import RequestPayload

if __name__ == "__main__":
  channel = grpc.insecure_channel('localhost:50051')
  stub = hello_world_pb2_grpc.HelloWorldStub(channel)
  payload = RequestPayload(name='Het')
  greeting = stub.Greeting(payload)
  print(greeting.message)