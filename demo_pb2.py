# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: demo.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='demo.proto',
  package='demo',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\ndemo.proto\x12\x04\x64\x65mo\"\x1b\n\x0bRequestData\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\t\"B\n\x0cResponseData\x12\x13\n\x0breturn_code\x18\x01 \x01(\x03\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\t2\xed\x01\n\x0b\x44\x65moService\x12\x34\n\tCreateOne\x12\x11.demo.RequestData\x1a\x12.demo.ResponseData\"\x00\x12\x34\n\tDeleteOne\x12\x11.demo.RequestData\x1a\x12.demo.ResponseData\"\x00\x12\x36\n\x0bTransferOne\x12\x11.demo.RequestData\x1a\x12.demo.ResponseData\"\x00\x12:\n\x0fGetCreateNotify\x12\x11.demo.RequestData\x1a\x12.demo.ResponseData\"\x00\x62\x06proto3')
)




_REQUESTDATA = _descriptor.Descriptor(
  name='RequestData',
  full_name='demo.RequestData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='demo.RequestData.data', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=20,
  serialized_end=47,
)


_RESPONSEDATA = _descriptor.Descriptor(
  name='ResponseData',
  full_name='demo.ResponseData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='return_code', full_name='demo.ResponseData.return_code', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='demo.ResponseData.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='demo.ResponseData.data', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=49,
  serialized_end=115,
)

DESCRIPTOR.message_types_by_name['RequestData'] = _REQUESTDATA
DESCRIPTOR.message_types_by_name['ResponseData'] = _RESPONSEDATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RequestData = _reflection.GeneratedProtocolMessageType('RequestData', (_message.Message,), dict(
  DESCRIPTOR = _REQUESTDATA,
  __module__ = 'demo_pb2'
  # @@protoc_insertion_point(class_scope:demo.RequestData)
  ))
_sym_db.RegisterMessage(RequestData)

ResponseData = _reflection.GeneratedProtocolMessageType('ResponseData', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSEDATA,
  __module__ = 'demo_pb2'
  # @@protoc_insertion_point(class_scope:demo.ResponseData)
  ))
_sym_db.RegisterMessage(ResponseData)



_DEMOSERVICE = _descriptor.ServiceDescriptor(
  name='DemoService',
  full_name='demo.DemoService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=118,
  serialized_end=355,
  methods=[
  _descriptor.MethodDescriptor(
    name='CreateOne',
    full_name='demo.DemoService.CreateOne',
    index=0,
    containing_service=None,
    input_type=_REQUESTDATA,
    output_type=_RESPONSEDATA,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='DeleteOne',
    full_name='demo.DemoService.DeleteOne',
    index=1,
    containing_service=None,
    input_type=_REQUESTDATA,
    output_type=_RESPONSEDATA,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='TransferOne',
    full_name='demo.DemoService.TransferOne',
    index=2,
    containing_service=None,
    input_type=_REQUESTDATA,
    output_type=_RESPONSEDATA,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetCreateNotify',
    full_name='demo.DemoService.GetCreateNotify',
    index=3,
    containing_service=None,
    input_type=_REQUESTDATA,
    output_type=_RESPONSEDATA,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_DEMOSERVICE)

DESCRIPTOR.services_by_name['DemoService'] = _DEMOSERVICE

# @@protoc_insertion_point(module_scope)
