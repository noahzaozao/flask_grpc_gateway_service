
python -m grpc_tools.protoc -I/usr/local/include -I. \
    --grpc_python_out=. \
    --python_out=. \
    -I./proto/ demo.proto