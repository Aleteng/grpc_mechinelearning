# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: svm.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='svm.proto',
  package='svm',
  syntax='proto3',
  serialized_options=_b('\n\024io.grpc.examples.svmB\010SVMProtoP\001\242\002\003SVM'),
  serialized_pb=_b('\n\tsvm.proto\x12\x03svm\" \n\rFlowerFeature\x12\x0f\n\x07\x66\x65\x61ture\x18\x01 \x03(\x02\"\x1d\n\x0b\x46lowerClass\x12\x0e\n\x06result\x18\x01 \x01(\t2?\n\x07Predict\x12\x34\n\nPrediction\x12\x12.svm.FlowerFeature\x1a\x10.svm.FlowerClass\"\x00\x42(\n\x14io.grpc.examples.svmB\x08SVMProtoP\x01\xa2\x02\x03SVMb\x06proto3')
)




_FLOWERFEATURE = _descriptor.Descriptor(
  name='FlowerFeature',
  full_name='svm.FlowerFeature',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='feature', full_name='svm.FlowerFeature.feature', index=0,
      number=1, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=18,
  serialized_end=50,
)


_FLOWERCLASS = _descriptor.Descriptor(
  name='FlowerClass',
  full_name='svm.FlowerClass',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='svm.FlowerClass.result', index=0,
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
  serialized_start=52,
  serialized_end=81,
)

DESCRIPTOR.message_types_by_name['FlowerFeature'] = _FLOWERFEATURE
DESCRIPTOR.message_types_by_name['FlowerClass'] = _FLOWERCLASS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FlowerFeature = _reflection.GeneratedProtocolMessageType('FlowerFeature', (_message.Message,), dict(
  DESCRIPTOR = _FLOWERFEATURE,
  __module__ = 'svm_pb2'
  # @@protoc_insertion_point(class_scope:svm.FlowerFeature)
  ))
_sym_db.RegisterMessage(FlowerFeature)

FlowerClass = _reflection.GeneratedProtocolMessageType('FlowerClass', (_message.Message,), dict(
  DESCRIPTOR = _FLOWERCLASS,
  __module__ = 'svm_pb2'
  # @@protoc_insertion_point(class_scope:svm.FlowerClass)
  ))
_sym_db.RegisterMessage(FlowerClass)


DESCRIPTOR._options = None

_PREDICT = _descriptor.ServiceDescriptor(
  name='Predict',
  full_name='svm.Predict',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=83,
  serialized_end=146,
  methods=[
  _descriptor.MethodDescriptor(
    name='Prediction',
    full_name='svm.Predict.Prediction',
    index=0,
    containing_service=None,
    input_type=_FLOWERFEATURE,
    output_type=_FLOWERCLASS,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_PREDICT)

DESCRIPTOR.services_by_name['Predict'] = _PREDICT

# @@protoc_insertion_point(module_scope)