# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: databricks_uc_registry_messages.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from .scalapb import scalapb_pb2 as scalapb_dot_scalapb__pb2
from . import databricks_pb2 as databricks__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%databricks_uc_registry_messages.proto\x12\x16mlflow.ucmodelregistry\x1a\x15scalapb/scalapb.proto\x1a\x10\x64\x61tabricks.proto\"\xc0\x01\n\x0fRegisteredModel\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x1a\n\x12\x63reation_timestamp\x18\x02 \x01(\x03\x12\x1e\n\x16last_updated_timestamp\x18\x03 \x01(\x03\x12\x0f\n\x07user_id\x18\x04 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x12=\n\x07\x61liases\x18\x06 \x03(\x0b\x32,.mlflow.ucmodelregistry.RegisteredModelAlias\"6\n\x14RegisteredModelAlias\x12\r\n\x05\x61lias\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\"\x97\x03\n\x0cModelVersion\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\x12\x1a\n\x12\x63reation_timestamp\x18\x03 \x01(\x03\x12\x1e\n\x16last_updated_timestamp\x18\x04 \x01(\x03\x12\x0f\n\x07user_id\x18\x05 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x06 \x01(\t\x12\x0e\n\x06source\x18\x07 \x01(\t\x12\x0e\n\x06run_id\x18\x08 \x01(\t\x12\x19\n\x11run_experiment_id\x18\t \x01(\t\x12\x1e\n\x16run_tracking_server_id\x18\n \x01(\t\x12:\n\x06status\x18\x0b \x01(\x0e\x32*.mlflow.ucmodelregistry.ModelVersionStatus\x12\x16\n\x0estatus_message\x18\x0c \x01(\t\x12\x18\n\x10storage_location\x18\r \x01(\t\x12=\n\x07\x61liases\x18\x0e \x03(\x0b\x32,.mlflow.ucmodelregistry.RegisteredModelAlias\"\x9d\x02\n\x14TemporaryCredentials\x12\x46\n\x14\x61ws_temp_credentials\x18\x02 \x01(\x0b\x32&.mlflow.ucmodelregistry.AwsCredentialsH\x00\x12S\n\x19\x61zure_user_delegation_sas\x18\x03 \x01(\x0b\x32..mlflow.ucmodelregistry.AzureUserDelegationSASH\x00\x12@\n\x0fgcp_oauth_token\x18\x04 \x01(\x0b\x32%.mlflow.ucmodelregistry.GcpOauthTokenH\x00\x12\x17\n\x0f\x65xpiration_time\x18\x01 \x01(\x03\x42\r\n\x0b\x63redentials\"Y\n\x0e\x41wsCredentials\x12\x15\n\raccess_key_id\x18\x01 \x01(\t\x12\x19\n\x11secret_access_key\x18\x02 \x01(\t\x12\x15\n\rsession_token\x18\x03 \x01(\t\"+\n\x16\x41zureUserDelegationSAS\x12\x11\n\tsas_token\x18\x01 \x01(\t\"$\n\rGcpOauthToken\x12\x13\n\x0boauth_token\x18\x01 \x01(\t\"\x83\x01\n\x1c\x43reateRegisteredModelRequest\x12\x12\n\x04name\x18\x01 \x01(\tB\x04\xf8\x86\x19\x01\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t::\xe2?7\n5com.databricks.rpc.RPC[CreateRegisteredModelResponse]\"b\n\x1d\x43reateRegisteredModelResponse\x12\x41\n\x10registered_model\x18\x01 \x01(\x0b\x32\'.mlflow.ucmodelregistry.RegisteredModel\"\x83\x01\n\x1cUpdateRegisteredModelRequest\x12\x12\n\x04name\x18\x01 \x01(\tB\x04\xf8\x86\x19\x01\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t::\xe2?7\n5com.databricks.rpc.RPC[UpdateRegisteredModelResponse]\"b\n\x1dUpdateRegisteredModelResponse\x12\x41\n\x10registered_model\x18\x01 \x01(\x0b\x32\'.mlflow.ucmodelregistry.RegisteredModel\"n\n\x1c\x44\x65leteRegisteredModelRequest\x12\x12\n\x04name\x18\x01 \x01(\tB\x04\xf8\x86\x19\x01::\xe2?7\n5com.databricks.rpc.RPC[DeleteRegisteredModelResponse]\"\x1f\n\x1d\x44\x65leteRegisteredModelResponse\"h\n\x19GetRegisteredModelRequest\x12\x12\n\x04name\x18\x01 \x01(\tB\x04\xf8\x86\x19\x01:7\xe2?4\n2com.databricks.rpc.RPC[GetRegisteredModelResponse]\"_\n\x1aGetRegisteredModelResponse\x12\x41\n\x10registered_model\x18\x01 \x01(\x0b\x32\'.mlflow.ucmodelregistry.RegisteredModel\"\x8a\x01\n\x1dSearchRegisteredModelsRequest\x12\x18\n\x0bmax_results\x18\x01 \x01(\x03:\x03\x31\x30\x30\x12\x12\n\npage_token\x18\x02 \x01(\t:;\xe2?8\n6com.databricks.rpc.RPC[SearchRegisteredModelsResponse]\"}\n\x1eSearchRegisteredModelsResponse\x12\x42\n\x11registered_models\x18\x01 \x03(\x0b\x32\'.mlflow.ucmodelregistry.RegisteredModel\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\xc3\x01\n\x19\x43reateModelVersionRequest\x12\x12\n\x04name\x18\x01 \x01(\tB\x04\xf8\x86\x19\x01\x12\x14\n\x06source\x18\x02 \x01(\tB\x04\xf8\x86\x19\x01\x12\x0e\n\x06run_id\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12\x1e\n\x16run_tracking_server_id\x18\x05 \x01(\t:7\xe2?4\n2com.databricks.rpc.RPC[CreateModelVersionResponse]\"Y\n\x1a\x43reateModelVersionResponse\x12;\n\rmodel_version\x18\x01 \x01(\x0b\x32$.mlflow.ucmodelregistry.ModelVersion\"\x94\x01\n\x19UpdateModelVersionRequest\x12\x12\n\x04name\x18\x01 \x01(\tB\x04\xf8\x86\x19\x01\x12\x15\n\x07version\x18\x02 \x01(\tB\x04\xf8\x86\x19\x01\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t:7\xe2?4\n2com.databricks.rpc.RPC[UpdateModelVersionResponse]\"Y\n\x1aUpdateModelVersionResponse\x12;\n\rmodel_version\x18\x01 \x01(\x0b\x32$.mlflow.ucmodelregistry.ModelVersion\"\x7f\n\x19\x44\x65leteModelVersionRequest\x12\x12\n\x04name\x18\x01 \x01(\tB\x04\xf8\x86\x19\x01\x12\x15\n\x07version\x18\x02 \x01(\tB\x04\xf8\x86\x19\x01:7\xe2?4\n2com.databricks.rpc.RPC[DeleteModelVersionResponse]\"\x1c\n\x1a\x44\x65leteModelVersionResponse\"y\n\x16GetModelVersionRequest\x12\x12\n\x04name\x18\x01 \x01(\tB\x04\xf8\x86\x19\x01\x12\x15\n\x07version\x18\x02 \x01(\tB\x04\xf8\x86\x19\x01:4\xe2?1\n/com.databricks.rpc.RPC[GetModelVersionResponse]\"V\n\x17GetModelVersionResponse\x12;\n\rmodel_version\x18\x01 \x01(\x0b\x32$.mlflow.ucmodelregistry.ModelVersion\"\x96\x01\n\x1aSearchModelVersionsRequest\x12\x0e\n\x06\x66ilter\x18\x01 \x01(\t\x12\x1a\n\x0bmax_results\x18\x02 \x01(\x03:\x05\x31\x30\x30\x30\x30\x12\x12\n\npage_token\x18\x03 \x01(\t:8\xe2?5\n3com.databricks.rpc.RPC[SearchModelVersionsResponse]\"t\n\x1bSearchModelVersionsResponse\x12<\n\x0emodel_versions\x18\x01 \x03(\x0b\x32$.mlflow.ucmodelregistry.ModelVersion\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\xf3\x01\n/GenerateTemporaryModelVersionCredentialsRequest\x12\x12\n\x04name\x18\x01 \x01(\tB\x04\xf8\x86\x19\x01\x12\x15\n\x07version\x18\x02 \x01(\tB\x04\xf8\x86\x19\x01\x12\x46\n\toperation\x18\x03 \x01(\x0e\x32-.mlflow.ucmodelregistry.ModelVersionOperationB\x04\xf8\x86\x19\x01:M\xe2?J\nHcom.databricks.rpc.RPC[GenerateTemporaryModelVersionCredentialsResponse]\"u\n0GenerateTemporaryModelVersionCredentialsResponse\x12\x41\n\x0b\x63redentials\x18\x01 \x01(\x0b\x32,.mlflow.ucmodelregistry.TemporaryCredentials\"\x8f\x01\n!GetModelVersionDownloadUriRequest\x12\x12\n\x04name\x18\x01 \x01(\tB\x04\xf8\x86\x19\x01\x12\x15\n\x07version\x18\x02 \x01(\tB\x04\xf8\x86\x19\x01:?\xe2?<\n:com.databricks.rpc.RPC[GetModelVersionDownloadUriResponse]\":\n\"GetModelVersionDownloadUriResponse\x12\x14\n\x0c\x61rtifact_uri\x18\x01 \x01(\t\"\x83\x01\n\x1b\x46inalizeModelVersionRequest\x12\x12\n\x04name\x18\x01 \x01(\tB\x04\xf8\x86\x19\x01\x12\x15\n\x07version\x18\x02 \x01(\tB\x04\xf8\x86\x19\x01:9\xe2?6\n4com.databricks.rpc.RPC[FinalizeModelVersionResponse]\"[\n\x1c\x46inalizeModelVersionResponse\x12;\n\rmodel_version\x18\x01 \x01(\x0b\x32$.mlflow.ucmodelregistry.ModelVersion\"\x9e\x01\n\x1eSetRegisteredModelAliasRequest\x12\x12\n\x04name\x18\x01 \x01(\tB\x04\xf8\x86\x19\x01\x12\x13\n\x05\x61lias\x18\x02 \x01(\tB\x04\xf8\x86\x19\x01\x12\x15\n\x07version\x18\x03 \x01(\tB\x04\xf8\x86\x19\x01:<\xe2?9\n7com.databricks.rpc.RPC[SetRegisteredModelAliasResponse]\"!\n\x1fSetRegisteredModelAliasResponse\"\x8d\x01\n!DeleteRegisteredModelAliasRequest\x12\x12\n\x04name\x18\x01 \x01(\tB\x04\xf8\x86\x19\x01\x12\x13\n\x05\x61lias\x18\x02 \x01(\tB\x04\xf8\x86\x19\x01:?\xe2?<\n:com.databricks.rpc.RPC[DeleteRegisteredModelAliasResponse]\"$\n\"DeleteRegisteredModelAliasResponse\"\x85\x01\n\x1dGetModelVersionByAliasRequest\x12\x12\n\x04name\x18\x01 \x01(\tB\x04\xf8\x86\x19\x01\x12\x13\n\x05\x61lias\x18\x02 \x01(\tB\x04\xf8\x86\x19\x01:;\xe2?8\n6com.databricks.rpc.RPC[GetModelVersionByAliasResponse]\"]\n\x1eGetModelVersionByAliasResponse\x12;\n\rmodel_version\x18\x01 \x01(\x0b\x32$.mlflow.ucmodelregistry.ModelVersion*c\n\x12ModelVersionStatus\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x18\n\x14PENDING_REGISTRATION\x10\x01\x12\x17\n\x13\x46\x41ILED_REGISTRATION\x10\x02\x12\t\n\x05READY\x10\x03*\x8a\x01\n\x15ModelVersionOperation\x12\'\n#MODEL_VERSION_OPERATION_UNSPECIFIED\x10\x00\x12 \n\x1cMODEL_VERSION_OPERATION_READ\x10\x01\x12&\n\"MODEL_VERSION_OPERATION_READ_WRITE\x10\x02\x42\x32\n(com.databricks.api.proto.ucmodelregistry\xa0\x01\x01\xe2?\x02\x10\x01')

_MODELVERSIONSTATUS = DESCRIPTOR.enum_types_by_name['ModelVersionStatus']
ModelVersionStatus = enum_type_wrapper.EnumTypeWrapper(_MODELVERSIONSTATUS)
_MODELVERSIONOPERATION = DESCRIPTOR.enum_types_by_name['ModelVersionOperation']
ModelVersionOperation = enum_type_wrapper.EnumTypeWrapper(_MODELVERSIONOPERATION)
UNSPECIFIED = 0
PENDING_REGISTRATION = 1
FAILED_REGISTRATION = 2
READY = 3
MODEL_VERSION_OPERATION_UNSPECIFIED = 0
MODEL_VERSION_OPERATION_READ = 1
MODEL_VERSION_OPERATION_READ_WRITE = 2


_REGISTEREDMODEL = DESCRIPTOR.message_types_by_name['RegisteredModel']
_REGISTEREDMODELALIAS = DESCRIPTOR.message_types_by_name['RegisteredModelAlias']
_MODELVERSION = DESCRIPTOR.message_types_by_name['ModelVersion']
_TEMPORARYCREDENTIALS = DESCRIPTOR.message_types_by_name['TemporaryCredentials']
_AWSCREDENTIALS = DESCRIPTOR.message_types_by_name['AwsCredentials']
_AZUREUSERDELEGATIONSAS = DESCRIPTOR.message_types_by_name['AzureUserDelegationSAS']
_GCPOAUTHTOKEN = DESCRIPTOR.message_types_by_name['GcpOauthToken']
_CREATEREGISTEREDMODELREQUEST = DESCRIPTOR.message_types_by_name['CreateRegisteredModelRequest']
_CREATEREGISTEREDMODELRESPONSE = DESCRIPTOR.message_types_by_name['CreateRegisteredModelResponse']
_UPDATEREGISTEREDMODELREQUEST = DESCRIPTOR.message_types_by_name['UpdateRegisteredModelRequest']
_UPDATEREGISTEREDMODELRESPONSE = DESCRIPTOR.message_types_by_name['UpdateRegisteredModelResponse']
_DELETEREGISTEREDMODELREQUEST = DESCRIPTOR.message_types_by_name['DeleteRegisteredModelRequest']
_DELETEREGISTEREDMODELRESPONSE = DESCRIPTOR.message_types_by_name['DeleteRegisteredModelResponse']
_GETREGISTEREDMODELREQUEST = DESCRIPTOR.message_types_by_name['GetRegisteredModelRequest']
_GETREGISTEREDMODELRESPONSE = DESCRIPTOR.message_types_by_name['GetRegisteredModelResponse']
_SEARCHREGISTEREDMODELSREQUEST = DESCRIPTOR.message_types_by_name['SearchRegisteredModelsRequest']
_SEARCHREGISTEREDMODELSRESPONSE = DESCRIPTOR.message_types_by_name['SearchRegisteredModelsResponse']
_CREATEMODELVERSIONREQUEST = DESCRIPTOR.message_types_by_name['CreateModelVersionRequest']
_CREATEMODELVERSIONRESPONSE = DESCRIPTOR.message_types_by_name['CreateModelVersionResponse']
_UPDATEMODELVERSIONREQUEST = DESCRIPTOR.message_types_by_name['UpdateModelVersionRequest']
_UPDATEMODELVERSIONRESPONSE = DESCRIPTOR.message_types_by_name['UpdateModelVersionResponse']
_DELETEMODELVERSIONREQUEST = DESCRIPTOR.message_types_by_name['DeleteModelVersionRequest']
_DELETEMODELVERSIONRESPONSE = DESCRIPTOR.message_types_by_name['DeleteModelVersionResponse']
_GETMODELVERSIONREQUEST = DESCRIPTOR.message_types_by_name['GetModelVersionRequest']
_GETMODELVERSIONRESPONSE = DESCRIPTOR.message_types_by_name['GetModelVersionResponse']
_SEARCHMODELVERSIONSREQUEST = DESCRIPTOR.message_types_by_name['SearchModelVersionsRequest']
_SEARCHMODELVERSIONSRESPONSE = DESCRIPTOR.message_types_by_name['SearchModelVersionsResponse']
_GENERATETEMPORARYMODELVERSIONCREDENTIALSREQUEST = DESCRIPTOR.message_types_by_name['GenerateTemporaryModelVersionCredentialsRequest']
_GENERATETEMPORARYMODELVERSIONCREDENTIALSRESPONSE = DESCRIPTOR.message_types_by_name['GenerateTemporaryModelVersionCredentialsResponse']
_GETMODELVERSIONDOWNLOADURIREQUEST = DESCRIPTOR.message_types_by_name['GetModelVersionDownloadUriRequest']
_GETMODELVERSIONDOWNLOADURIRESPONSE = DESCRIPTOR.message_types_by_name['GetModelVersionDownloadUriResponse']
_FINALIZEMODELVERSIONREQUEST = DESCRIPTOR.message_types_by_name['FinalizeModelVersionRequest']
_FINALIZEMODELVERSIONRESPONSE = DESCRIPTOR.message_types_by_name['FinalizeModelVersionResponse']
_SETREGISTEREDMODELALIASREQUEST = DESCRIPTOR.message_types_by_name['SetRegisteredModelAliasRequest']
_SETREGISTEREDMODELALIASRESPONSE = DESCRIPTOR.message_types_by_name['SetRegisteredModelAliasResponse']
_DELETEREGISTEREDMODELALIASREQUEST = DESCRIPTOR.message_types_by_name['DeleteRegisteredModelAliasRequest']
_DELETEREGISTEREDMODELALIASRESPONSE = DESCRIPTOR.message_types_by_name['DeleteRegisteredModelAliasResponse']
_GETMODELVERSIONBYALIASREQUEST = DESCRIPTOR.message_types_by_name['GetModelVersionByAliasRequest']
_GETMODELVERSIONBYALIASRESPONSE = DESCRIPTOR.message_types_by_name['GetModelVersionByAliasResponse']
RegisteredModel = _reflection.GeneratedProtocolMessageType('RegisteredModel', (_message.Message,), {
  'DESCRIPTOR' : _REGISTEREDMODEL,
  '__module__' : 'databricks_uc_registry_messages_pb2'
  # @@protoc_insertion_point(class_scope:mlflow.ucmodelregistry.RegisteredModel)
  })
_sym_db.RegisterMessage(RegisteredModel)

RegisteredModelAlias = _reflection.GeneratedProtocolMessageType('RegisteredModelAlias', (_message.Message,), {
  'DESCRIPTOR' : _REGISTEREDMODELALIAS,
  '__module__' : 'databricks_uc_registry_messages_pb2'
  # @@protoc_insertion_point(class_scope:mlflow.ucmodelregistry.RegisteredModelAlias)
  })
_sym_db.RegisterMessage(RegisteredModelAlias)

ModelVersion = _reflection.GeneratedProtocolMessageType('ModelVersion', (_message.Message,), {
  'DESCRIPTOR' : _MODELVERSION,
  '__module__' : 'databricks_uc_registry_messages_pb2'
  # @@protoc_insertion_point(class_scope:mlflow.ucmodelregistry.ModelVersion)
  })
_sym_db.RegisterMessage(ModelVersion)

TemporaryCredentials = _reflection.GeneratedProtocolMessageType('TemporaryCredentials', (_message.Message,), {
  'DESCRIPTOR' : _TEMPORARYCREDENTIALS,
  '__module__' : 'databricks_uc_registry_messages_pb2'
  # @@protoc_insertion_point(class_scope:mlflow.ucmodelregistry.TemporaryCredentials)
  })
_sym_db.RegisterMessage(TemporaryCredentials)

AwsCredentials = _reflection.GeneratedProtocolMessageType('AwsCredentials', (_message.Message,), {
  'DESCRIPTOR' : _AWSCREDENTIALS,
  '__module__' : 'databricks_uc_registry_messages_pb2'
  # @@protoc_insertion_point(class_scope:mlflow.ucmodelregistry.AwsCredentials)
  })
_sym_db.RegisterMessage(AwsCredentials)

AzureUserDelegationSAS = _reflection.GeneratedProtocolMessageType('AzureUserDelegationSAS', (_message.Message,), {
  'DESCRIPTOR' : _AZUREUSERDELEGATIONSAS,
  '__module__' : 'databricks_uc_registry_messages_pb2'
  # @@protoc_insertion_point(class_scope:mlflow.ucmodelregistry.AzureUserDelegationSAS)
  })
_sym_db.RegisterMessage(AzureUserDelegationSAS)

GcpOauthToken = _reflection.GeneratedProtocolMessageType('GcpOauthToken', (_message.Message,), {
  'DESCRIPTOR' : _GCPOAUTHTOKEN,
  '__module__' : 'databricks_uc_registry_messages_pb2'
  # @@protoc_insertion_point(class_scope:mlflow.ucmodelregistry.GcpOauthToken)
  })
_sym_db.RegisterMessage(GcpOauthToken)

CreateRegisteredModelRequest = _reflection.GeneratedProtocolMessageType('CreateRegisteredModelRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEREGISTEREDMODELREQUEST,
  '__module__' : 'databricks_uc_registry_messages_pb2'
  # @@protoc_insertion_point(class_scope:mlflow.ucmodelregistry.CreateRegisteredModelRequest)
  })
_sym_db.RegisterMessage(CreateRegisteredModelRequest)

CreateRegisteredModelResponse = _reflection.GeneratedProtocolMessageType('CreateRegisteredModelResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATEREGISTEREDMODELRESPONSE,
  '__module__' : 'databricks_uc_registry_messages_pb2'
  # @@protoc_insertion_point(class_scope:mlflow.ucmodelregistry.CreateRegisteredModelResponse)
  })
_sym_db.RegisterMessage(CreateRegisteredModelResponse)

UpdateRegisteredModelRequest = _reflection.GeneratedProtocolMessageType('UpdateRegisteredModelRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEREGISTEREDMODELREQUEST,
  '__module__' : 'databricks_uc_registry_messages_pb2'
  # @@protoc_insertion_point(class_scope:mlflow.ucmodelregistry.UpdateRegisteredModelRequest)
  })
_sym_db.RegisterMessage(UpdateRegisteredModelRequest)

UpdateRegisteredModelResponse = _reflection.GeneratedProtocolMessageType('UpdateRegisteredModelResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEREGISTEREDMODELRESPONSE,
  '__module__' : 'databricks_uc_registry_messages_pb2'
  # @@protoc_insertion_point(class_scope:mlflow.ucmodelregistry.UpdateRegisteredModelResponse)
  })
_sym_db.RegisterMessage(UpdateRegisteredModelResponse)

DeleteRegisteredModelRequest = _reflection.GeneratedProtocolMessageType('DeleteRegisteredModelRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEREGISTEREDMODELREQUEST,
  '__module__' : 'databricks_uc_registry_messages_pb2'
  # @@protoc_insertion_point(class_scope:mlflow.ucmodelregistry.DeleteRegisteredModelRequest)
  })
_sym_db.RegisterMessage(DeleteRegisteredModelRequest)

DeleteRegisteredModelResponse = _reflection.GeneratedProtocolMessageType('DeleteRegisteredModelResponse', (_message.Message,), {
  'DESCRIPTOR' : _DELETEREGISTEREDMODELRESPONSE,
  '__module__' : 'databricks_uc_registry_messages_pb2'
  # @@protoc_insertion_point(class_scope:mlflow.ucmodelregistry.DeleteRegisteredModelResponse)
  })
_sym_db.RegisterMessage(DeleteRegisteredModelResponse)

GetRegisteredModelRequest = _reflection.GeneratedProtocolMessageType('GetRegisteredModelRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETREGISTEREDMODELREQUEST,
  '__module__' : 'databricks_uc_registry_messages_pb2'
  # @@protoc_insertion_point(class_scope:mlflow.ucmodelregistry.GetRegisteredModelRequest)
  })
_sym_db.RegisterMessage(GetRegisteredModelRequest)

GetRegisteredModelResponse = _reflection.GeneratedProtocolMessageType('GetRegisteredModelResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETREGISTEREDMODELRESPONSE,
  '__module__' : 'databricks_uc_registry_messages_pb2'
  # @@protoc_insertion_point(class_scope:mlflow.ucmodelregistry.GetRegisteredModelResponse)
  })
_sym_db.RegisterMessage(GetRegisteredModelResponse)

SearchRegisteredModelsRequest = _reflection.GeneratedProtocolMessageType('SearchRegisteredModelsRequest', (_message.Message,), {
  'DESCRIPTOR' : _SEARCHREGISTEREDMODELSREQUEST,
  '__module__' : 'databricks_uc_registry_messages_pb2'
  # @@protoc_insertion_point(class_scope:mlflow.ucmodelregistry.SearchRegisteredModelsRequest)
  })
_sym_db.RegisterMessage(SearchRegisteredModelsRequest)

SearchRegisteredModelsResponse = _reflection.GeneratedProtocolMessageType('SearchRegisteredModelsResponse', (_message.Message,), {
  'DESCRIPTOR' : _SEARCHREGISTEREDMODELSRESPONSE,
  '__module__' : 'databricks_uc_registry_messages_pb2'
  # @@protoc_insertion_point(class_scope:mlflow.ucmodelregistry.SearchRegisteredModelsResponse)
  })
_sym_db.RegisterMessage(SearchRegisteredModelsResponse)

CreateModelVersionRequest = _reflection.GeneratedProtocolMessageType('CreateModelVersionRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEMODELVERSIONREQUEST,
  '__module__' : 'databricks_uc_registry_messages_pb2'
  # @@protoc_insertion_point(class_scope:mlflow.ucmodelregistry.CreateModelVersionRequest)
  })
_sym_db.RegisterMessage(CreateModelVersionRequest)

CreateModelVersionResponse = _reflection.GeneratedProtocolMessageType('CreateModelVersionResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATEMODELVERSIONRESPONSE,
  '__module__' : 'databricks_uc_registry_messages_pb2'
  # @@protoc_insertion_point(class_scope:mlflow.ucmodelregistry.CreateModelVersionResponse)
  })
_sym_db.RegisterMessage(CreateModelVersionResponse)

UpdateModelVersionRequest = _reflection.GeneratedProtocolMessageType('UpdateModelVersionRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEMODELVERSIONREQUEST,
  '__module__' : 'databricks_uc_registry_messages_pb2'
  # @@protoc_insertion_point(class_scope:mlflow.ucmodelregistry.UpdateModelVersionRequest)
  })
_sym_db.RegisterMessage(UpdateModelVersionRequest)

UpdateModelVersionResponse = _reflection.GeneratedProtocolMessageType('UpdateModelVersionResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEMODELVERSIONRESPONSE,
  '__module__' : 'databricks_uc_registry_messages_pb2'
  # @@protoc_insertion_point(class_scope:mlflow.ucmodelregistry.UpdateModelVersionResponse)
  })
_sym_db.RegisterMessage(UpdateModelVersionResponse)

DeleteModelVersionRequest = _reflection.GeneratedProtocolMessageType('DeleteModelVersionRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEMODELVERSIONREQUEST,
  '__module__' : 'databricks_uc_registry_messages_pb2'
  # @@protoc_insertion_point(class_scope:mlflow.ucmodelregistry.DeleteModelVersionRequest)
  })
_sym_db.RegisterMessage(DeleteModelVersionRequest)

DeleteModelVersionResponse = _reflection.GeneratedProtocolMessageType('DeleteModelVersionResponse', (_message.Message,), {
  'DESCRIPTOR' : _DELETEMODELVERSIONRESPONSE,
  '__module__' : 'databricks_uc_registry_messages_pb2'
  # @@protoc_insertion_point(class_scope:mlflow.ucmodelregistry.DeleteModelVersionResponse)
  })
_sym_db.RegisterMessage(DeleteModelVersionResponse)

GetModelVersionRequest = _reflection.GeneratedProtocolMessageType('GetModelVersionRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETMODELVERSIONREQUEST,
  '__module__' : 'databricks_uc_registry_messages_pb2'
  # @@protoc_insertion_point(class_scope:mlflow.ucmodelregistry.GetModelVersionRequest)
  })
_sym_db.RegisterMessage(GetModelVersionRequest)

GetModelVersionResponse = _reflection.GeneratedProtocolMessageType('GetModelVersionResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETMODELVERSIONRESPONSE,
  '__module__' : 'databricks_uc_registry_messages_pb2'
  # @@protoc_insertion_point(class_scope:mlflow.ucmodelregistry.GetModelVersionResponse)
  })
_sym_db.RegisterMessage(GetModelVersionResponse)

SearchModelVersionsRequest = _reflection.GeneratedProtocolMessageType('SearchModelVersionsRequest', (_message.Message,), {
  'DESCRIPTOR' : _SEARCHMODELVERSIONSREQUEST,
  '__module__' : 'databricks_uc_registry_messages_pb2'
  # @@protoc_insertion_point(class_scope:mlflow.ucmodelregistry.SearchModelVersionsRequest)
  })
_sym_db.RegisterMessage(SearchModelVersionsRequest)

SearchModelVersionsResponse = _reflection.GeneratedProtocolMessageType('SearchModelVersionsResponse', (_message.Message,), {
  'DESCRIPTOR' : _SEARCHMODELVERSIONSRESPONSE,
  '__module__' : 'databricks_uc_registry_messages_pb2'
  # @@protoc_insertion_point(class_scope:mlflow.ucmodelregistry.SearchModelVersionsResponse)
  })
_sym_db.RegisterMessage(SearchModelVersionsResponse)

GenerateTemporaryModelVersionCredentialsRequest = _reflection.GeneratedProtocolMessageType('GenerateTemporaryModelVersionCredentialsRequest', (_message.Message,), {
  'DESCRIPTOR' : _GENERATETEMPORARYMODELVERSIONCREDENTIALSREQUEST,
  '__module__' : 'databricks_uc_registry_messages_pb2'
  # @@protoc_insertion_point(class_scope:mlflow.ucmodelregistry.GenerateTemporaryModelVersionCredentialsRequest)
  })
_sym_db.RegisterMessage(GenerateTemporaryModelVersionCredentialsRequest)

GenerateTemporaryModelVersionCredentialsResponse = _reflection.GeneratedProtocolMessageType('GenerateTemporaryModelVersionCredentialsResponse', (_message.Message,), {
  'DESCRIPTOR' : _GENERATETEMPORARYMODELVERSIONCREDENTIALSRESPONSE,
  '__module__' : 'databricks_uc_registry_messages_pb2'
  # @@protoc_insertion_point(class_scope:mlflow.ucmodelregistry.GenerateTemporaryModelVersionCredentialsResponse)
  })
_sym_db.RegisterMessage(GenerateTemporaryModelVersionCredentialsResponse)

GetModelVersionDownloadUriRequest = _reflection.GeneratedProtocolMessageType('GetModelVersionDownloadUriRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETMODELVERSIONDOWNLOADURIREQUEST,
  '__module__' : 'databricks_uc_registry_messages_pb2'
  # @@protoc_insertion_point(class_scope:mlflow.ucmodelregistry.GetModelVersionDownloadUriRequest)
  })
_sym_db.RegisterMessage(GetModelVersionDownloadUriRequest)

GetModelVersionDownloadUriResponse = _reflection.GeneratedProtocolMessageType('GetModelVersionDownloadUriResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETMODELVERSIONDOWNLOADURIRESPONSE,
  '__module__' : 'databricks_uc_registry_messages_pb2'
  # @@protoc_insertion_point(class_scope:mlflow.ucmodelregistry.GetModelVersionDownloadUriResponse)
  })
_sym_db.RegisterMessage(GetModelVersionDownloadUriResponse)

FinalizeModelVersionRequest = _reflection.GeneratedProtocolMessageType('FinalizeModelVersionRequest', (_message.Message,), {
  'DESCRIPTOR' : _FINALIZEMODELVERSIONREQUEST,
  '__module__' : 'databricks_uc_registry_messages_pb2'
  # @@protoc_insertion_point(class_scope:mlflow.ucmodelregistry.FinalizeModelVersionRequest)
  })
_sym_db.RegisterMessage(FinalizeModelVersionRequest)

FinalizeModelVersionResponse = _reflection.GeneratedProtocolMessageType('FinalizeModelVersionResponse', (_message.Message,), {
  'DESCRIPTOR' : _FINALIZEMODELVERSIONRESPONSE,
  '__module__' : 'databricks_uc_registry_messages_pb2'
  # @@protoc_insertion_point(class_scope:mlflow.ucmodelregistry.FinalizeModelVersionResponse)
  })
_sym_db.RegisterMessage(FinalizeModelVersionResponse)

SetRegisteredModelAliasRequest = _reflection.GeneratedProtocolMessageType('SetRegisteredModelAliasRequest', (_message.Message,), {
  'DESCRIPTOR' : _SETREGISTEREDMODELALIASREQUEST,
  '__module__' : 'databricks_uc_registry_messages_pb2'
  # @@protoc_insertion_point(class_scope:mlflow.ucmodelregistry.SetRegisteredModelAliasRequest)
  })
_sym_db.RegisterMessage(SetRegisteredModelAliasRequest)

SetRegisteredModelAliasResponse = _reflection.GeneratedProtocolMessageType('SetRegisteredModelAliasResponse', (_message.Message,), {
  'DESCRIPTOR' : _SETREGISTEREDMODELALIASRESPONSE,
  '__module__' : 'databricks_uc_registry_messages_pb2'
  # @@protoc_insertion_point(class_scope:mlflow.ucmodelregistry.SetRegisteredModelAliasResponse)
  })
_sym_db.RegisterMessage(SetRegisteredModelAliasResponse)

DeleteRegisteredModelAliasRequest = _reflection.GeneratedProtocolMessageType('DeleteRegisteredModelAliasRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEREGISTEREDMODELALIASREQUEST,
  '__module__' : 'databricks_uc_registry_messages_pb2'
  # @@protoc_insertion_point(class_scope:mlflow.ucmodelregistry.DeleteRegisteredModelAliasRequest)
  })
_sym_db.RegisterMessage(DeleteRegisteredModelAliasRequest)

DeleteRegisteredModelAliasResponse = _reflection.GeneratedProtocolMessageType('DeleteRegisteredModelAliasResponse', (_message.Message,), {
  'DESCRIPTOR' : _DELETEREGISTEREDMODELALIASRESPONSE,
  '__module__' : 'databricks_uc_registry_messages_pb2'
  # @@protoc_insertion_point(class_scope:mlflow.ucmodelregistry.DeleteRegisteredModelAliasResponse)
  })
_sym_db.RegisterMessage(DeleteRegisteredModelAliasResponse)

GetModelVersionByAliasRequest = _reflection.GeneratedProtocolMessageType('GetModelVersionByAliasRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETMODELVERSIONBYALIASREQUEST,
  '__module__' : 'databricks_uc_registry_messages_pb2'
  # @@protoc_insertion_point(class_scope:mlflow.ucmodelregistry.GetModelVersionByAliasRequest)
  })
_sym_db.RegisterMessage(GetModelVersionByAliasRequest)

GetModelVersionByAliasResponse = _reflection.GeneratedProtocolMessageType('GetModelVersionByAliasResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETMODELVERSIONBYALIASRESPONSE,
  '__module__' : 'databricks_uc_registry_messages_pb2'
  # @@protoc_insertion_point(class_scope:mlflow.ucmodelregistry.GetModelVersionByAliasResponse)
  })
_sym_db.RegisterMessage(GetModelVersionByAliasResponse)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n(com.databricks.api.proto.ucmodelregistry\240\001\001\342?\002\020\001'
  _CREATEREGISTEREDMODELREQUEST.fields_by_name['name']._options = None
  _CREATEREGISTEREDMODELREQUEST.fields_by_name['name']._serialized_options = b'\370\206\031\001'
  _CREATEREGISTEREDMODELREQUEST._options = None
  _CREATEREGISTEREDMODELREQUEST._serialized_options = b'\342?7\n5com.databricks.rpc.RPC[CreateRegisteredModelResponse]'
  _UPDATEREGISTEREDMODELREQUEST.fields_by_name['name']._options = None
  _UPDATEREGISTEREDMODELREQUEST.fields_by_name['name']._serialized_options = b'\370\206\031\001'
  _UPDATEREGISTEREDMODELREQUEST._options = None
  _UPDATEREGISTEREDMODELREQUEST._serialized_options = b'\342?7\n5com.databricks.rpc.RPC[UpdateRegisteredModelResponse]'
  _DELETEREGISTEREDMODELREQUEST.fields_by_name['name']._options = None
  _DELETEREGISTEREDMODELREQUEST.fields_by_name['name']._serialized_options = b'\370\206\031\001'
  _DELETEREGISTEREDMODELREQUEST._options = None
  _DELETEREGISTEREDMODELREQUEST._serialized_options = b'\342?7\n5com.databricks.rpc.RPC[DeleteRegisteredModelResponse]'
  _GETREGISTEREDMODELREQUEST.fields_by_name['name']._options = None
  _GETREGISTEREDMODELREQUEST.fields_by_name['name']._serialized_options = b'\370\206\031\001'
  _GETREGISTEREDMODELREQUEST._options = None
  _GETREGISTEREDMODELREQUEST._serialized_options = b'\342?4\n2com.databricks.rpc.RPC[GetRegisteredModelResponse]'
  _SEARCHREGISTEREDMODELSREQUEST._options = None
  _SEARCHREGISTEREDMODELSREQUEST._serialized_options = b'\342?8\n6com.databricks.rpc.RPC[SearchRegisteredModelsResponse]'
  _CREATEMODELVERSIONREQUEST.fields_by_name['name']._options = None
  _CREATEMODELVERSIONREQUEST.fields_by_name['name']._serialized_options = b'\370\206\031\001'
  _CREATEMODELVERSIONREQUEST.fields_by_name['source']._options = None
  _CREATEMODELVERSIONREQUEST.fields_by_name['source']._serialized_options = b'\370\206\031\001'
  _CREATEMODELVERSIONREQUEST._options = None
  _CREATEMODELVERSIONREQUEST._serialized_options = b'\342?4\n2com.databricks.rpc.RPC[CreateModelVersionResponse]'
  _UPDATEMODELVERSIONREQUEST.fields_by_name['name']._options = None
  _UPDATEMODELVERSIONREQUEST.fields_by_name['name']._serialized_options = b'\370\206\031\001'
  _UPDATEMODELVERSIONREQUEST.fields_by_name['version']._options = None
  _UPDATEMODELVERSIONREQUEST.fields_by_name['version']._serialized_options = b'\370\206\031\001'
  _UPDATEMODELVERSIONREQUEST._options = None
  _UPDATEMODELVERSIONREQUEST._serialized_options = b'\342?4\n2com.databricks.rpc.RPC[UpdateModelVersionResponse]'
  _DELETEMODELVERSIONREQUEST.fields_by_name['name']._options = None
  _DELETEMODELVERSIONREQUEST.fields_by_name['name']._serialized_options = b'\370\206\031\001'
  _DELETEMODELVERSIONREQUEST.fields_by_name['version']._options = None
  _DELETEMODELVERSIONREQUEST.fields_by_name['version']._serialized_options = b'\370\206\031\001'
  _DELETEMODELVERSIONREQUEST._options = None
  _DELETEMODELVERSIONREQUEST._serialized_options = b'\342?4\n2com.databricks.rpc.RPC[DeleteModelVersionResponse]'
  _GETMODELVERSIONREQUEST.fields_by_name['name']._options = None
  _GETMODELVERSIONREQUEST.fields_by_name['name']._serialized_options = b'\370\206\031\001'
  _GETMODELVERSIONREQUEST.fields_by_name['version']._options = None
  _GETMODELVERSIONREQUEST.fields_by_name['version']._serialized_options = b'\370\206\031\001'
  _GETMODELVERSIONREQUEST._options = None
  _GETMODELVERSIONREQUEST._serialized_options = b'\342?1\n/com.databricks.rpc.RPC[GetModelVersionResponse]'
  _SEARCHMODELVERSIONSREQUEST._options = None
  _SEARCHMODELVERSIONSREQUEST._serialized_options = b'\342?5\n3com.databricks.rpc.RPC[SearchModelVersionsResponse]'
  _GENERATETEMPORARYMODELVERSIONCREDENTIALSREQUEST.fields_by_name['name']._options = None
  _GENERATETEMPORARYMODELVERSIONCREDENTIALSREQUEST.fields_by_name['name']._serialized_options = b'\370\206\031\001'
  _GENERATETEMPORARYMODELVERSIONCREDENTIALSREQUEST.fields_by_name['version']._options = None
  _GENERATETEMPORARYMODELVERSIONCREDENTIALSREQUEST.fields_by_name['version']._serialized_options = b'\370\206\031\001'
  _GENERATETEMPORARYMODELVERSIONCREDENTIALSREQUEST.fields_by_name['operation']._options = None
  _GENERATETEMPORARYMODELVERSIONCREDENTIALSREQUEST.fields_by_name['operation']._serialized_options = b'\370\206\031\001'
  _GENERATETEMPORARYMODELVERSIONCREDENTIALSREQUEST._options = None
  _GENERATETEMPORARYMODELVERSIONCREDENTIALSREQUEST._serialized_options = b'\342?J\nHcom.databricks.rpc.RPC[GenerateTemporaryModelVersionCredentialsResponse]'
  _GETMODELVERSIONDOWNLOADURIREQUEST.fields_by_name['name']._options = None
  _GETMODELVERSIONDOWNLOADURIREQUEST.fields_by_name['name']._serialized_options = b'\370\206\031\001'
  _GETMODELVERSIONDOWNLOADURIREQUEST.fields_by_name['version']._options = None
  _GETMODELVERSIONDOWNLOADURIREQUEST.fields_by_name['version']._serialized_options = b'\370\206\031\001'
  _GETMODELVERSIONDOWNLOADURIREQUEST._options = None
  _GETMODELVERSIONDOWNLOADURIREQUEST._serialized_options = b'\342?<\n:com.databricks.rpc.RPC[GetModelVersionDownloadUriResponse]'
  _FINALIZEMODELVERSIONREQUEST.fields_by_name['name']._options = None
  _FINALIZEMODELVERSIONREQUEST.fields_by_name['name']._serialized_options = b'\370\206\031\001'
  _FINALIZEMODELVERSIONREQUEST.fields_by_name['version']._options = None
  _FINALIZEMODELVERSIONREQUEST.fields_by_name['version']._serialized_options = b'\370\206\031\001'
  _FINALIZEMODELVERSIONREQUEST._options = None
  _FINALIZEMODELVERSIONREQUEST._serialized_options = b'\342?6\n4com.databricks.rpc.RPC[FinalizeModelVersionResponse]'
  _SETREGISTEREDMODELALIASREQUEST.fields_by_name['name']._options = None
  _SETREGISTEREDMODELALIASREQUEST.fields_by_name['name']._serialized_options = b'\370\206\031\001'
  _SETREGISTEREDMODELALIASREQUEST.fields_by_name['alias']._options = None
  _SETREGISTEREDMODELALIASREQUEST.fields_by_name['alias']._serialized_options = b'\370\206\031\001'
  _SETREGISTEREDMODELALIASREQUEST.fields_by_name['version']._options = None
  _SETREGISTEREDMODELALIASREQUEST.fields_by_name['version']._serialized_options = b'\370\206\031\001'
  _SETREGISTEREDMODELALIASREQUEST._options = None
  _SETREGISTEREDMODELALIASREQUEST._serialized_options = b'\342?9\n7com.databricks.rpc.RPC[SetRegisteredModelAliasResponse]'
  _DELETEREGISTEREDMODELALIASREQUEST.fields_by_name['name']._options = None
  _DELETEREGISTEREDMODELALIASREQUEST.fields_by_name['name']._serialized_options = b'\370\206\031\001'
  _DELETEREGISTEREDMODELALIASREQUEST.fields_by_name['alias']._options = None
  _DELETEREGISTEREDMODELALIASREQUEST.fields_by_name['alias']._serialized_options = b'\370\206\031\001'
  _DELETEREGISTEREDMODELALIASREQUEST._options = None
  _DELETEREGISTEREDMODELALIASREQUEST._serialized_options = b'\342?<\n:com.databricks.rpc.RPC[DeleteRegisteredModelAliasResponse]'
  _GETMODELVERSIONBYALIASREQUEST.fields_by_name['name']._options = None
  _GETMODELVERSIONBYALIASREQUEST.fields_by_name['name']._serialized_options = b'\370\206\031\001'
  _GETMODELVERSIONBYALIASREQUEST.fields_by_name['alias']._options = None
  _GETMODELVERSIONBYALIASREQUEST.fields_by_name['alias']._serialized_options = b'\370\206\031\001'
  _GETMODELVERSIONBYALIASREQUEST._options = None
  _GETMODELVERSIONBYALIASREQUEST._serialized_options = b'\342?8\n6com.databricks.rpc.RPC[GetModelVersionByAliasResponse]'
  _MODELVERSIONSTATUS._serialized_start=4892
  _MODELVERSIONSTATUS._serialized_end=4991
  _MODELVERSIONOPERATION._serialized_start=4994
  _MODELVERSIONOPERATION._serialized_end=5132
  _REGISTEREDMODEL._serialized_start=107
  _REGISTEREDMODEL._serialized_end=299
  _REGISTEREDMODELALIAS._serialized_start=301
  _REGISTEREDMODELALIAS._serialized_end=355
  _MODELVERSION._serialized_start=358
  _MODELVERSION._serialized_end=765
  _TEMPORARYCREDENTIALS._serialized_start=768
  _TEMPORARYCREDENTIALS._serialized_end=1053
  _AWSCREDENTIALS._serialized_start=1055
  _AWSCREDENTIALS._serialized_end=1144
  _AZUREUSERDELEGATIONSAS._serialized_start=1146
  _AZUREUSERDELEGATIONSAS._serialized_end=1189
  _GCPOAUTHTOKEN._serialized_start=1191
  _GCPOAUTHTOKEN._serialized_end=1227
  _CREATEREGISTEREDMODELREQUEST._serialized_start=1230
  _CREATEREGISTEREDMODELREQUEST._serialized_end=1361
  _CREATEREGISTEREDMODELRESPONSE._serialized_start=1363
  _CREATEREGISTEREDMODELRESPONSE._serialized_end=1461
  _UPDATEREGISTEREDMODELREQUEST._serialized_start=1464
  _UPDATEREGISTEREDMODELREQUEST._serialized_end=1595
  _UPDATEREGISTEREDMODELRESPONSE._serialized_start=1597
  _UPDATEREGISTEREDMODELRESPONSE._serialized_end=1695
  _DELETEREGISTEREDMODELREQUEST._serialized_start=1697
  _DELETEREGISTEREDMODELREQUEST._serialized_end=1807
  _DELETEREGISTEREDMODELRESPONSE._serialized_start=1809
  _DELETEREGISTEREDMODELRESPONSE._serialized_end=1840
  _GETREGISTEREDMODELREQUEST._serialized_start=1842
  _GETREGISTEREDMODELREQUEST._serialized_end=1946
  _GETREGISTEREDMODELRESPONSE._serialized_start=1948
  _GETREGISTEREDMODELRESPONSE._serialized_end=2043
  _SEARCHREGISTEREDMODELSREQUEST._serialized_start=2046
  _SEARCHREGISTEREDMODELSREQUEST._serialized_end=2184
  _SEARCHREGISTEREDMODELSRESPONSE._serialized_start=2186
  _SEARCHREGISTEREDMODELSRESPONSE._serialized_end=2311
  _CREATEMODELVERSIONREQUEST._serialized_start=2314
  _CREATEMODELVERSIONREQUEST._serialized_end=2509
  _CREATEMODELVERSIONRESPONSE._serialized_start=2511
  _CREATEMODELVERSIONRESPONSE._serialized_end=2600
  _UPDATEMODELVERSIONREQUEST._serialized_start=2603
  _UPDATEMODELVERSIONREQUEST._serialized_end=2751
  _UPDATEMODELVERSIONRESPONSE._serialized_start=2753
  _UPDATEMODELVERSIONRESPONSE._serialized_end=2842
  _DELETEMODELVERSIONREQUEST._serialized_start=2844
  _DELETEMODELVERSIONREQUEST._serialized_end=2971
  _DELETEMODELVERSIONRESPONSE._serialized_start=2973
  _DELETEMODELVERSIONRESPONSE._serialized_end=3001
  _GETMODELVERSIONREQUEST._serialized_start=3003
  _GETMODELVERSIONREQUEST._serialized_end=3124
  _GETMODELVERSIONRESPONSE._serialized_start=3126
  _GETMODELVERSIONRESPONSE._serialized_end=3212
  _SEARCHMODELVERSIONSREQUEST._serialized_start=3215
  _SEARCHMODELVERSIONSREQUEST._serialized_end=3365
  _SEARCHMODELVERSIONSRESPONSE._serialized_start=3367
  _SEARCHMODELVERSIONSRESPONSE._serialized_end=3483
  _GENERATETEMPORARYMODELVERSIONCREDENTIALSREQUEST._serialized_start=3486
  _GENERATETEMPORARYMODELVERSIONCREDENTIALSREQUEST._serialized_end=3729
  _GENERATETEMPORARYMODELVERSIONCREDENTIALSRESPONSE._serialized_start=3731
  _GENERATETEMPORARYMODELVERSIONCREDENTIALSRESPONSE._serialized_end=3848
  _GETMODELVERSIONDOWNLOADURIREQUEST._serialized_start=3851
  _GETMODELVERSIONDOWNLOADURIREQUEST._serialized_end=3994
  _GETMODELVERSIONDOWNLOADURIRESPONSE._serialized_start=3996
  _GETMODELVERSIONDOWNLOADURIRESPONSE._serialized_end=4054
  _FINALIZEMODELVERSIONREQUEST._serialized_start=4057
  _FINALIZEMODELVERSIONREQUEST._serialized_end=4188
  _FINALIZEMODELVERSIONRESPONSE._serialized_start=4190
  _FINALIZEMODELVERSIONRESPONSE._serialized_end=4281
  _SETREGISTEREDMODELALIASREQUEST._serialized_start=4284
  _SETREGISTEREDMODELALIASREQUEST._serialized_end=4442
  _SETREGISTEREDMODELALIASRESPONSE._serialized_start=4444
  _SETREGISTEREDMODELALIASRESPONSE._serialized_end=4477
  _DELETEREGISTEREDMODELALIASREQUEST._serialized_start=4480
  _DELETEREGISTEREDMODELALIASREQUEST._serialized_end=4621
  _DELETEREGISTEREDMODELALIASRESPONSE._serialized_start=4623
  _DELETEREGISTEREDMODELALIASRESPONSE._serialized_end=4659
  _GETMODELVERSIONBYALIASREQUEST._serialized_start=4662
  _GETMODELVERSIONBYALIASREQUEST._serialized_end=4795
  _GETMODELVERSIONBYALIASRESPONSE._serialized_start=4797
  _GETMODELVERSIONBYALIASRESPONSE._serialized_end=4890
# @@protoc_insertion_point(module_scope)
