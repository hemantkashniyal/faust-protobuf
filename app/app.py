import faust
from google.protobuf.json_format import MessageToJson

from .proto.greetings_pb2 import Greeting

from .proto_serializer import ProtobufSerializer

app = faust.App(
    'faust-consumer',
    broker='kafka://', # TODO: update kafka endpoint
    store="memory://",
    cache="memory://",
)

greetings_schema = faust.Schema(
    key_serializer=ProtobufSerializer(pb_type=Greeting),
    value_serializer=ProtobufSerializer(pb_type=Greeting),
)

topic = app.topic(
    'greetings',
    schema=greetings_schema
)

@app.agent(topic)
async def consume(topic):
    async for event in topic:
        print(MessageToJson(event))

@app.timer(5)
async def produce():
    for i in range(10):
        data = Greeting(hello="world", message=i)
        await consume.send(value=data)

if __name__ == "__main__":
    app.main()