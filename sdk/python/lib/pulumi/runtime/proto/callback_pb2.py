# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pulumi/callback.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15pulumi/callback.proto\x12\tpulumirpc\")\n\x08\x43\x61llback\x12\x0e\n\x06target\x18\x01 \x01(\t\x12\r\n\x05token\x18\x02 \x01(\t\"7\n\x15\x43\x61llbackInvokeRequest\x12\r\n\x05token\x18\x01 \x01(\t\x12\x0f\n\x07request\x18\x02 \x01(\x0c\"*\n\x16\x43\x61llbackInvokeResponse\x12\x10\n\x08response\x18\x01 \x01(\x0c\x32\\\n\tCallbacks\x12O\n\x06Invoke\x12 .pulumirpc.CallbackInvokeRequest\x1a!.pulumirpc.CallbackInvokeResponse\"\x00\x42\x34Z2github.com/pulumi/pulumi/sdk/v3/proto/go;pulumirpcb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'pulumi.callback_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z2github.com/pulumi/pulumi/sdk/v3/proto/go;pulumirpc'
  _CALLBACK._serialized_start=36
  _CALLBACK._serialized_end=77
  _CALLBACKINVOKEREQUEST._serialized_start=79
  _CALLBACKINVOKEREQUEST._serialized_end=134
  _CALLBACKINVOKERESPONSE._serialized_start=136
  _CALLBACKINVOKERESPONSE._serialized_end=178
  _CALLBACKS._serialized_start=180
  _CALLBACKS._serialized_end=272
# @@protoc_insertion_point(module_scope)
