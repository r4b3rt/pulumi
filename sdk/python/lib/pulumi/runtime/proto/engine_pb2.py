# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pulumi/engine.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13pulumi/engine.proto\x12\tpulumirpc\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1cgoogle/protobuf/struct.proto\"y\n\nLogRequest\x12(\n\x08severity\x18\x01 \x01(\x0e\x32\x16.pulumirpc.LogSeverity\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x0b\n\x03urn\x18\x03 \x01(\t\x12\x10\n\x08streamId\x18\x04 \x01(\x05\x12\x11\n\tephemeral\x18\x05 \x01(\x08\"\x18\n\x16GetRootResourceRequest\"&\n\x17GetRootResourceResponse\x12\x0b\n\x03urn\x18\x01 \x01(\t\"%\n\x16SetRootResourceRequest\x12\x0b\n\x03urn\x18\x01 \x01(\t\"\x19\n\x17SetRootResourceResponse\"Q\n\x15StartDebuggingRequest\x12\'\n\x06\x63onfig\x18\x01 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x0f\n\x07message\x18\x02 \x01(\t*:\n\x0bLogSeverity\x12\t\n\x05\x44\x45\x42UG\x10\x00\x12\x08\n\x04INFO\x10\x01\x12\x0b\n\x07WARNING\x10\x02\x12\t\n\x05\x45RROR\x10\x03\x32\xc6\x02\n\x06\x45ngine\x12\x36\n\x03Log\x12\x15.pulumirpc.LogRequest\x1a\x16.google.protobuf.Empty\"\x00\x12Z\n\x0fGetRootResource\x12!.pulumirpc.GetRootResourceRequest\x1a\".pulumirpc.GetRootResourceResponse\"\x00\x12Z\n\x0fSetRootResource\x12!.pulumirpc.SetRootResourceRequest\x1a\".pulumirpc.SetRootResourceResponse\"\x00\x12L\n\x0eStartDebugging\x12 .pulumirpc.StartDebuggingRequest\x1a\x16.google.protobuf.Empty\"\x00\x42\x34Z2github.com/pulumi/pulumi/sdk/v3/proto/go;pulumirpcb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'pulumi.engine_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z2github.com/pulumi/pulumi/sdk/v3/proto/go;pulumirpc'
  _LOGSEVERITY._serialized_start=431
  _LOGSEVERITY._serialized_end=489
  _LOGREQUEST._serialized_start=93
  _LOGREQUEST._serialized_end=214
  _GETROOTRESOURCEREQUEST._serialized_start=216
  _GETROOTRESOURCEREQUEST._serialized_end=240
  _GETROOTRESOURCERESPONSE._serialized_start=242
  _GETROOTRESOURCERESPONSE._serialized_end=280
  _SETROOTRESOURCEREQUEST._serialized_start=282
  _SETROOTRESOURCEREQUEST._serialized_end=319
  _SETROOTRESOURCERESPONSE._serialized_start=321
  _SETROOTRESOURCERESPONSE._serialized_end=346
  _STARTDEBUGGINGREQUEST._serialized_start=348
  _STARTDEBUGGINGREQUEST._serialized_end=429
  _ENGINE._serialized_start=492
  _ENGINE._serialized_end=818
# @@protoc_insertion_point(module_scope)
