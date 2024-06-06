# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pulumi/language.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from .codegen import hcl_pb2 as pulumi_dot_codegen_dot_hcl__pb2
from . import plugin_pb2 as pulumi_dot_plugin__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15pulumi/language.proto\x12\tpulumirpc\x1a\x18pulumi/codegen/hcl.proto\x1a\x13pulumi/plugin.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1cgoogle/protobuf/struct.proto\"\x7f\n\x0bProgramInfo\x12\x16\n\x0eroot_directory\x18\x01 \x01(\t\x12\x19\n\x11program_directory\x18\x02 \x01(\t\x12\x13\n\x0b\x65ntry_point\x18\x03 \x01(\t\x12(\n\x07options\x18\x04 \x01(\x0b\x32\x17.google.protobuf.Struct\"4\n\x0c\x41\x62outRequest\x12$\n\x04info\x18\x01 \x01(\x0b\x32\x16.pulumirpc.ProgramInfo\"\x9f\x01\n\rAboutResponse\x12\x12\n\nexecutable\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\x12\x38\n\x08metadata\x18\x03 \x03(\x0b\x32&.pulumirpc.AboutResponse.MetadataEntry\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xa0\x01\n\x1dGetProgramDependenciesRequest\x12\x13\n\x07project\x18\x01 \x01(\tB\x02\x18\x01\x12\x0f\n\x03pwd\x18\x02 \x01(\tB\x02\x18\x01\x12\x13\n\x07program\x18\x03 \x01(\tB\x02\x18\x01\x12\x1e\n\x16transitiveDependencies\x18\x04 \x01(\x08\x12$\n\x04info\x18\x05 \x01(\x0b\x32\x16.pulumirpc.ProgramInfo\"/\n\x0e\x44\x65pendencyInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\"Q\n\x1eGetProgramDependenciesResponse\x12/\n\x0c\x64\x65pendencies\x18\x01 \x03(\x0b\x32\x19.pulumirpc.DependencyInfo\"|\n\x19GetRequiredPluginsRequest\x12\x13\n\x07project\x18\x01 \x01(\tB\x02\x18\x01\x12\x0f\n\x03pwd\x18\x02 \x01(\tB\x02\x18\x01\x12\x13\n\x07program\x18\x03 \x01(\tB\x02\x18\x01\x12$\n\x04info\x18\x04 \x01(\x0b\x32\x16.pulumirpc.ProgramInfo\"J\n\x1aGetRequiredPluginsResponse\x12,\n\x07plugins\x18\x01 \x03(\x0b\x32\x1b.pulumirpc.PluginDependency\"\x96\x03\n\nRunRequest\x12\x0f\n\x07project\x18\x01 \x01(\t\x12\r\n\x05stack\x18\x02 \x01(\t\x12\x0b\n\x03pwd\x18\x03 \x01(\t\x12\x13\n\x07program\x18\x04 \x01(\tB\x02\x18\x01\x12\x0c\n\x04\x61rgs\x18\x05 \x03(\t\x12\x31\n\x06\x63onfig\x18\x06 \x03(\x0b\x32!.pulumirpc.RunRequest.ConfigEntry\x12\x0e\n\x06\x64ryRun\x18\x07 \x01(\x08\x12\x10\n\x08parallel\x18\x08 \x01(\x05\x12\x17\n\x0fmonitor_address\x18\t \x01(\t\x12\x11\n\tqueryMode\x18\n \x01(\x08\x12\x18\n\x10\x63onfigSecretKeys\x18\x0b \x03(\t\x12\x14\n\x0corganization\x18\x0c \x01(\t\x12\x32\n\x11\x63onfigPropertyMap\x18\r \x01(\x0b\x32\x17.google.protobuf.Struct\x12$\n\x04info\x18\x0e \x01(\x0b\x32\x16.pulumirpc.ProgramInfo\x1a-\n\x0b\x43onfigEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"*\n\x0bRunResponse\x12\r\n\x05\x65rror\x18\x01 \x01(\t\x12\x0c\n\x04\x62\x61il\x18\x02 \x01(\x08\"n\n\x1aInstallDependenciesRequest\x12\x15\n\tdirectory\x18\x01 \x01(\tB\x02\x18\x01\x12\x13\n\x0bis_terminal\x18\x02 \x01(\x08\x12$\n\x04info\x18\x03 \x01(\x0b\x32\x16.pulumirpc.ProgramInfo\"=\n\x1bInstallDependenciesResponse\x12\x0e\n\x06stdout\x18\x01 \x01(\x0c\x12\x0e\n\x06stderr\x18\x02 \x01(\x0c\"u\n\x10RunPluginRequest\x12\x0b\n\x03pwd\x18\x01 \x01(\t\x12\x13\n\x07program\x18\x02 \x01(\tB\x02\x18\x01\x12\x0c\n\x04\x61rgs\x18\x03 \x03(\t\x12\x0b\n\x03\x65nv\x18\x04 \x03(\t\x12$\n\x04info\x18\x05 \x01(\x0b\x32\x16.pulumirpc.ProgramInfo\"U\n\x11RunPluginResponse\x12\x10\n\x06stdout\x18\x01 \x01(\x0cH\x00\x12\x10\n\x06stderr\x18\x02 \x01(\x0cH\x00\x12\x12\n\x08\x65xitcode\x18\x03 \x01(\x05H\x00\x42\x08\n\x06output\"\x9d\x01\n\x16GenerateProgramRequest\x12=\n\x06source\x18\x01 \x03(\x0b\x32-.pulumirpc.GenerateProgramRequest.SourceEntry\x12\x15\n\rloader_target\x18\x02 \x01(\t\x1a-\n\x0bSourceEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xbc\x01\n\x17GenerateProgramResponse\x12\x32\n\x0b\x64iagnostics\x18\x01 \x03(\x0b\x32\x1d.pulumirpc.codegen.Diagnostic\x12>\n\x06source\x18\x02 \x03(\x0b\x32..pulumirpc.GenerateProgramResponse.SourceEntry\x1a-\n\x0bSourceEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x0c:\x02\x38\x01\"\x94\x02\n\x16GenerateProjectRequest\x12\x18\n\x10source_directory\x18\x01 \x01(\t\x12\x18\n\x10target_directory\x18\x02 \x01(\t\x12\x0f\n\x07project\x18\x03 \x01(\t\x12\x0e\n\x06strict\x18\x04 \x01(\x08\x12\x15\n\rloader_target\x18\x05 \x01(\t\x12T\n\x12local_dependencies\x18\x06 \x03(\x0b\x32\x38.pulumirpc.GenerateProjectRequest.LocalDependenciesEntry\x1a\x38\n\x16LocalDependenciesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"M\n\x17GenerateProjectResponse\x12\x32\n\x0b\x64iagnostics\x18\x01 \x03(\x0b\x32\x1d.pulumirpc.codegen.Diagnostic\"\xdd\x02\n\x16GeneratePackageRequest\x12\x11\n\tdirectory\x18\x01 \x01(\t\x12\x0e\n\x06schema\x18\x02 \x01(\t\x12\x46\n\x0b\x65xtra_files\x18\x03 \x03(\x0b\x32\x31.pulumirpc.GeneratePackageRequest.ExtraFilesEntry\x12\x15\n\rloader_target\x18\x04 \x01(\t\x12T\n\x12local_dependencies\x18\x05 \x03(\x0b\x32\x38.pulumirpc.GeneratePackageRequest.LocalDependenciesEntry\x1a\x31\n\x0f\x45xtraFilesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x0c:\x02\x38\x01\x1a\x38\n\x16LocalDependenciesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"M\n\x17GeneratePackageResponse\x12\x32\n\x0b\x64iagnostics\x18\x01 \x03(\x0b\x32\x1d.pulumirpc.codegen.Diagnostic\"G\n\x0bPackRequest\x12\x19\n\x11package_directory\x18\x01 \x01(\t\x12\x1d\n\x15\x64\x65stination_directory\x18\x02 \x01(\t\"%\n\x0cPackResponse\x12\x15\n\rartifact_path\x18\x01 \x01(\t2\xa4\x07\n\x0fLanguageRuntime\x12\x63\n\x12GetRequiredPlugins\x12$.pulumirpc.GetRequiredPluginsRequest\x1a%.pulumirpc.GetRequiredPluginsResponse\"\x00\x12\x36\n\x03Run\x12\x15.pulumirpc.RunRequest\x1a\x16.pulumirpc.RunResponse\"\x00\x12@\n\rGetPluginInfo\x12\x16.google.protobuf.Empty\x1a\x15.pulumirpc.PluginInfo\"\x00\x12h\n\x13InstallDependencies\x12%.pulumirpc.InstallDependenciesRequest\x1a&.pulumirpc.InstallDependenciesResponse\"\x00\x30\x01\x12<\n\x05\x41\x62out\x12\x17.pulumirpc.AboutRequest\x1a\x18.pulumirpc.AboutResponse\"\x00\x12o\n\x16GetProgramDependencies\x12(.pulumirpc.GetProgramDependenciesRequest\x1a).pulumirpc.GetProgramDependenciesResponse\"\x00\x12J\n\tRunPlugin\x12\x1b.pulumirpc.RunPluginRequest\x1a\x1c.pulumirpc.RunPluginResponse\"\x00\x30\x01\x12Z\n\x0fGenerateProgram\x12!.pulumirpc.GenerateProgramRequest\x1a\".pulumirpc.GenerateProgramResponse\"\x00\x12Z\n\x0fGenerateProject\x12!.pulumirpc.GenerateProjectRequest\x1a\".pulumirpc.GenerateProjectResponse\"\x00\x12Z\n\x0fGeneratePackage\x12!.pulumirpc.GeneratePackageRequest\x1a\".pulumirpc.GeneratePackageResponse\"\x00\x12\x39\n\x04Pack\x12\x16.pulumirpc.PackRequest\x1a\x17.pulumirpc.PackResponse\"\x00\x42\x34Z2github.com/pulumi/pulumi/sdk/v3/proto/go;pulumirpcb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'pulumi.language_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z2github.com/pulumi/pulumi/sdk/v3/proto/go;pulumirpc'
  _ABOUTRESPONSE_METADATAENTRY._options = None
  _ABOUTRESPONSE_METADATAENTRY._serialized_options = b'8\001'
  _GETPROGRAMDEPENDENCIESREQUEST.fields_by_name['project']._options = None
  _GETPROGRAMDEPENDENCIESREQUEST.fields_by_name['project']._serialized_options = b'\030\001'
  _GETPROGRAMDEPENDENCIESREQUEST.fields_by_name['pwd']._options = None
  _GETPROGRAMDEPENDENCIESREQUEST.fields_by_name['pwd']._serialized_options = b'\030\001'
  _GETPROGRAMDEPENDENCIESREQUEST.fields_by_name['program']._options = None
  _GETPROGRAMDEPENDENCIESREQUEST.fields_by_name['program']._serialized_options = b'\030\001'
  _GETREQUIREDPLUGINSREQUEST.fields_by_name['project']._options = None
  _GETREQUIREDPLUGINSREQUEST.fields_by_name['project']._serialized_options = b'\030\001'
  _GETREQUIREDPLUGINSREQUEST.fields_by_name['pwd']._options = None
  _GETREQUIREDPLUGINSREQUEST.fields_by_name['pwd']._serialized_options = b'\030\001'
  _GETREQUIREDPLUGINSREQUEST.fields_by_name['program']._options = None
  _GETREQUIREDPLUGINSREQUEST.fields_by_name['program']._serialized_options = b'\030\001'
  _RUNREQUEST_CONFIGENTRY._options = None
  _RUNREQUEST_CONFIGENTRY._serialized_options = b'8\001'
  _RUNREQUEST.fields_by_name['program']._options = None
  _RUNREQUEST.fields_by_name['program']._serialized_options = b'\030\001'
  _INSTALLDEPENDENCIESREQUEST.fields_by_name['directory']._options = None
  _INSTALLDEPENDENCIESREQUEST.fields_by_name['directory']._serialized_options = b'\030\001'
  _RUNPLUGINREQUEST.fields_by_name['program']._options = None
  _RUNPLUGINREQUEST.fields_by_name['program']._serialized_options = b'\030\001'
  _GENERATEPROGRAMREQUEST_SOURCEENTRY._options = None
  _GENERATEPROGRAMREQUEST_SOURCEENTRY._serialized_options = b'8\001'
  _GENERATEPROGRAMRESPONSE_SOURCEENTRY._options = None
  _GENERATEPROGRAMRESPONSE_SOURCEENTRY._serialized_options = b'8\001'
  _GENERATEPROJECTREQUEST_LOCALDEPENDENCIESENTRY._options = None
  _GENERATEPROJECTREQUEST_LOCALDEPENDENCIESENTRY._serialized_options = b'8\001'
  _GENERATEPACKAGEREQUEST_EXTRAFILESENTRY._options = None
  _GENERATEPACKAGEREQUEST_EXTRAFILESENTRY._serialized_options = b'8\001'
  _GENERATEPACKAGEREQUEST_LOCALDEPENDENCIESENTRY._options = None
  _GENERATEPACKAGEREQUEST_LOCALDEPENDENCIESENTRY._serialized_options = b'8\001'
  _PROGRAMINFO._serialized_start=142
  _PROGRAMINFO._serialized_end=269
  _ABOUTREQUEST._serialized_start=271
  _ABOUTREQUEST._serialized_end=323
  _ABOUTRESPONSE._serialized_start=326
  _ABOUTRESPONSE._serialized_end=485
  _ABOUTRESPONSE_METADATAENTRY._serialized_start=438
  _ABOUTRESPONSE_METADATAENTRY._serialized_end=485
  _GETPROGRAMDEPENDENCIESREQUEST._serialized_start=488
  _GETPROGRAMDEPENDENCIESREQUEST._serialized_end=648
  _DEPENDENCYINFO._serialized_start=650
  _DEPENDENCYINFO._serialized_end=697
  _GETPROGRAMDEPENDENCIESRESPONSE._serialized_start=699
  _GETPROGRAMDEPENDENCIESRESPONSE._serialized_end=780
  _GETREQUIREDPLUGINSREQUEST._serialized_start=782
  _GETREQUIREDPLUGINSREQUEST._serialized_end=906
  _GETREQUIREDPLUGINSRESPONSE._serialized_start=908
  _GETREQUIREDPLUGINSRESPONSE._serialized_end=982
  _RUNREQUEST._serialized_start=985
  _RUNREQUEST._serialized_end=1391
  _RUNREQUEST_CONFIGENTRY._serialized_start=1346
  _RUNREQUEST_CONFIGENTRY._serialized_end=1391
  _RUNRESPONSE._serialized_start=1393
  _RUNRESPONSE._serialized_end=1435
  _INSTALLDEPENDENCIESREQUEST._serialized_start=1437
  _INSTALLDEPENDENCIESREQUEST._serialized_end=1547
  _INSTALLDEPENDENCIESRESPONSE._serialized_start=1549
  _INSTALLDEPENDENCIESRESPONSE._serialized_end=1610
  _RUNPLUGINREQUEST._serialized_start=1612
  _RUNPLUGINREQUEST._serialized_end=1729
  _RUNPLUGINRESPONSE._serialized_start=1731
  _RUNPLUGINRESPONSE._serialized_end=1816
  _GENERATEPROGRAMREQUEST._serialized_start=1819
  _GENERATEPROGRAMREQUEST._serialized_end=1976
  _GENERATEPROGRAMREQUEST_SOURCEENTRY._serialized_start=1931
  _GENERATEPROGRAMREQUEST_SOURCEENTRY._serialized_end=1976
  _GENERATEPROGRAMRESPONSE._serialized_start=1979
  _GENERATEPROGRAMRESPONSE._serialized_end=2167
  _GENERATEPROGRAMRESPONSE_SOURCEENTRY._serialized_start=2122
  _GENERATEPROGRAMRESPONSE_SOURCEENTRY._serialized_end=2167
  _GENERATEPROJECTREQUEST._serialized_start=2170
  _GENERATEPROJECTREQUEST._serialized_end=2446
  _GENERATEPROJECTREQUEST_LOCALDEPENDENCIESENTRY._serialized_start=2390
  _GENERATEPROJECTREQUEST_LOCALDEPENDENCIESENTRY._serialized_end=2446
  _GENERATEPROJECTRESPONSE._serialized_start=2448
  _GENERATEPROJECTRESPONSE._serialized_end=2525
  _GENERATEPACKAGEREQUEST._serialized_start=2528
  _GENERATEPACKAGEREQUEST._serialized_end=2877
  _GENERATEPACKAGEREQUEST_EXTRAFILESENTRY._serialized_start=2770
  _GENERATEPACKAGEREQUEST_EXTRAFILESENTRY._serialized_end=2819
  _GENERATEPACKAGEREQUEST_LOCALDEPENDENCIESENTRY._serialized_start=2390
  _GENERATEPACKAGEREQUEST_LOCALDEPENDENCIESENTRY._serialized_end=2446
  _GENERATEPACKAGERESPONSE._serialized_start=2879
  _GENERATEPACKAGERESPONSE._serialized_end=2956
  _PACKREQUEST._serialized_start=2958
  _PACKREQUEST._serialized_end=3029
  _PACKRESPONSE._serialized_start=3031
  _PACKRESPONSE._serialized_end=3068
  _LANGUAGERUNTIME._serialized_start=3071
  _LANGUAGERUNTIME._serialized_end=4003
# @@protoc_insertion_point(module_scope)
