# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: message.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rmessage.proto\"*\n\nInnerModel\x12\x12\n\x05value\x18\x01 \x01(\tH\x00\x88\x01\x01\x42\x08\n\x06_value\"\xa6\x01\n\x07Message\x12\x10\n\x03str\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x10\n\x03int\x18\x02 \x01(\x03H\x01\x88\x01\x01\x12\x11\n\x04\x62ool\x18\x03 \x01(\x08H\x02\x88\x01\x01\x12%\n\x0binner_model\x18\x04 \x01(\x0b\x32\x0b.InnerModelH\x03\x88\x01\x01\x12\x14\n\x0crepeated_str\x18\x05 \x03(\tB\x06\n\x04_strB\x06\n\x04_intB\x07\n\x05_boolB\x0e\n\x0c_inner_modelb\x06proto3')



_INNERMODEL = DESCRIPTOR.message_types_by_name['InnerModel']
_MESSAGE = DESCRIPTOR.message_types_by_name['Message']
InnerModel = _reflection.GeneratedProtocolMessageType('InnerModel', (_message.Message,), {
  'DESCRIPTOR' : _INNERMODEL,
  '__module__' : 'message_pb2'
  # @@protoc_insertion_point(class_scope:InnerModel)
  })
_sym_db.RegisterMessage(InnerModel)

Message = _reflection.GeneratedProtocolMessageType('Message', (_message.Message,), {
  'DESCRIPTOR' : _MESSAGE,
  '__module__' : 'message_pb2'
  # @@protoc_insertion_point(class_scope:Message)
  })
_sym_db.RegisterMessage(Message)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _INNERMODEL._serialized_start=17
  _INNERMODEL._serialized_end=59
  _MESSAGE._serialized_start=62
  _MESSAGE._serialized_end=228
# @@protoc_insertion_point(module_scope)