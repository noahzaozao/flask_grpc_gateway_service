from flask import Flask
app = Flask(__name__)

import grpc

import demo_pb2
import demo_pb2_grpc


@app.route('/grpc')
def hello_world_grpc():
    with grpc.insecure_channel('127.0.0.1:9090') as channel:
        client = demo_pb2_grpc.DemoServiceStub(channel)

        response = client.CreateOne(demo_pb2.RequestData(
            data="call create one from client",
        ))
        print(response.return_code, response.message, response.data)
    return 'Hello, World grpc!'


@app.route('/')
def hello_world():
    return 'Hello, World!'


