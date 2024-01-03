# gRPC (Python)

This repo contains basic implementation of gRPC in python.

### Compiling Protocol buffer files

```properties
python -m grpc_tools.protoc -I./ --python_out=. --pyi_out=. --grpc_python_out=. ./hello_world.proto
```

### Run the server

```properties
python server.py
```

### Run the client

```properties
python client.py
```
