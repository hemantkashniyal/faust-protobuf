from faust.serializers import codecs
from typing import Any

from google.protobuf import json_format
from google.protobuf.json_format import MessageToJson
from google.protobuf.json_format import MessageToDict
from google.protobuf import text_format
from google.protobuf.text_format import MessageToString
from google.protobuf.text_format import MessageToBytes

class ProtobufSerializer(codecs.Codec):
    def __init__(self, pb_type: Any):
        self.pb_type = pb_type
        super(self.__class__, self).__init__()

    def _dumps(self, pb: Any) -> bytes:
        return pb.SerializeToString()

    def _loads(self, s: bytes) -> Any:
        pb = self.pb_type()
        pb.ParseFromString(s)
        return pb

