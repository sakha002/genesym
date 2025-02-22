# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: asset_groups.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import intervals_pb2 as intervals__pb2
import assets_pb2 as assets__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='asset_groups.proto',
  package='genesys',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x12\x61sset_groups.proto\x12\x07genesys\x1a\x0fintervals.proto\x1a\x0c\x61ssets.proto\"\xae\x02\n\nAssetGroup\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12%\n\x04type\x18\x04 \x01(\x0e\x32\x17.genesys.AssetGroupType\x12\x1e\n\x06\x61ssets\x18\x05 \x03(\x0b\x32\x0e.genesys.Asset\x12\x11\n\tasset_ids\x18\x06 \x03(\x05\x12\x35\n\x12resource_economics\x18\t \x03(\x0b\x32\x19.genesys.ResourceEconomic\x12\x39\n\x14\x61sset_group_economic\x18\x0c \x01(\x0b\x32\x1b.genesys.AssetGroupEconomic\x12:\n\x0foperation_limit\x18\x0f \x01(\x0b\x32!.genesys.AssetGroupOperationLimit\"\x82\x03\n\x18\x41ssetGroupOperationLimit\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x38\n\x10import_max_power\x18\x05 \x01(\x0b\x32\x1e.genesys.IntervalQuantityGroup\x12\x38\n\x10\x65xport_max_power\x18\x06 \x01(\x0b\x32\x1e.genesys.IntervalQuantityGroup\x12\x38\n\x10import_min_power\x18\x07 \x01(\x0b\x32\x1e.genesys.IntervalQuantityGroup\x12\x38\n\x10\x65xport_min_power\x18\x08 \x01(\x0b\x32\x1e.genesys.IntervalQuantityGroup\x12\x31\n\x11import_max_energy\x18\t \x01(\x0b\x32\x16.genesys.BasicQuantity\x12\x31\n\x11\x65xport_max_energy\x18\n \x01(\x0b\x32\x16.genesys.BasicQuantity\"~\n\x12\x41ssetGroupEconomic\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x31\n\x10\x65\x63onomics_prices\x18\x05 \x03(\x0b\x32\x17.genesys.EconomicsPrice\x12\x1b\n\x13\x65\x63onomics_price_ids\x18\x06 \x03(\x05\"\x8f\x01\n\x10ResourceEconomic\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x11\n\tasset_ids\x18\x04 \x03(\x05\x12\x31\n\x10\x65\x63onomics_prices\x18\x05 \x03(\x0b\x32\x17.genesys.EconomicsPrice\x12\x1b\n\x13\x65\x63onomics_price_ids\x18\x06 \x03(\x05*7\n\x0e\x41ssetGroupType\x12\x0c\n\x08PHYSICAL\x10\x00\x12\r\n\tFINANCIAL\x10\x01\x12\x08\n\x04ROOT\x10\x02\x62\x06proto3'
  ,
  dependencies=[intervals__pb2.DESCRIPTOR,assets__pb2.DESCRIPTOR,])

_ASSETGROUPTYPE = _descriptor.EnumDescriptor(
  name='AssetGroupType',
  full_name='genesys.AssetGroupType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PHYSICAL', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FINANCIAL', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ROOT', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1030,
  serialized_end=1085,
)
_sym_db.RegisterEnumDescriptor(_ASSETGROUPTYPE)

AssetGroupType = enum_type_wrapper.EnumTypeWrapper(_ASSETGROUPTYPE)
PHYSICAL = 0
FINANCIAL = 1
ROOT = 2



_ASSETGROUP = _descriptor.Descriptor(
  name='AssetGroup',
  full_name='genesys.AssetGroup',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='genesys.AssetGroup.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='genesys.AssetGroup.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='genesys.AssetGroup.type', index=2,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='assets', full_name='genesys.AssetGroup.assets', index=3,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='asset_ids', full_name='genesys.AssetGroup.asset_ids', index=4,
      number=6, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='resource_economics', full_name='genesys.AssetGroup.resource_economics', index=5,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='asset_group_economic', full_name='genesys.AssetGroup.asset_group_economic', index=6,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='operation_limit', full_name='genesys.AssetGroup.operation_limit', index=7,
      number=15, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=63,
  serialized_end=365,
)


_ASSETGROUPOPERATIONLIMIT = _descriptor.Descriptor(
  name='AssetGroupOperationLimit',
  full_name='genesys.AssetGroupOperationLimit',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='genesys.AssetGroupOperationLimit.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='genesys.AssetGroupOperationLimit.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='import_max_power', full_name='genesys.AssetGroupOperationLimit.import_max_power', index=2,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='export_max_power', full_name='genesys.AssetGroupOperationLimit.export_max_power', index=3,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='import_min_power', full_name='genesys.AssetGroupOperationLimit.import_min_power', index=4,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='export_min_power', full_name='genesys.AssetGroupOperationLimit.export_min_power', index=5,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='import_max_energy', full_name='genesys.AssetGroupOperationLimit.import_max_energy', index=6,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='export_max_energy', full_name='genesys.AssetGroupOperationLimit.export_max_energy', index=7,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=368,
  serialized_end=754,
)


_ASSETGROUPECONOMIC = _descriptor.Descriptor(
  name='AssetGroupEconomic',
  full_name='genesys.AssetGroupEconomic',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='genesys.AssetGroupEconomic.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='genesys.AssetGroupEconomic.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='economics_prices', full_name='genesys.AssetGroupEconomic.economics_prices', index=2,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='economics_price_ids', full_name='genesys.AssetGroupEconomic.economics_price_ids', index=3,
      number=6, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=756,
  serialized_end=882,
)


_RESOURCEECONOMIC = _descriptor.Descriptor(
  name='ResourceEconomic',
  full_name='genesys.ResourceEconomic',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='genesys.ResourceEconomic.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='genesys.ResourceEconomic.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='asset_ids', full_name='genesys.ResourceEconomic.asset_ids', index=2,
      number=4, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='economics_prices', full_name='genesys.ResourceEconomic.economics_prices', index=3,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='economics_price_ids', full_name='genesys.ResourceEconomic.economics_price_ids', index=4,
      number=6, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=885,
  serialized_end=1028,
)

_ASSETGROUP.fields_by_name['type'].enum_type = _ASSETGROUPTYPE
_ASSETGROUP.fields_by_name['assets'].message_type = assets__pb2._ASSET
_ASSETGROUP.fields_by_name['resource_economics'].message_type = _RESOURCEECONOMIC
_ASSETGROUP.fields_by_name['asset_group_economic'].message_type = _ASSETGROUPECONOMIC
_ASSETGROUP.fields_by_name['operation_limit'].message_type = _ASSETGROUPOPERATIONLIMIT
_ASSETGROUPOPERATIONLIMIT.fields_by_name['import_max_power'].message_type = intervals__pb2._INTERVALQUANTITYGROUP
_ASSETGROUPOPERATIONLIMIT.fields_by_name['export_max_power'].message_type = intervals__pb2._INTERVALQUANTITYGROUP
_ASSETGROUPOPERATIONLIMIT.fields_by_name['import_min_power'].message_type = intervals__pb2._INTERVALQUANTITYGROUP
_ASSETGROUPOPERATIONLIMIT.fields_by_name['export_min_power'].message_type = intervals__pb2._INTERVALQUANTITYGROUP
_ASSETGROUPOPERATIONLIMIT.fields_by_name['import_max_energy'].message_type = intervals__pb2._BASICQUANTITY
_ASSETGROUPOPERATIONLIMIT.fields_by_name['export_max_energy'].message_type = intervals__pb2._BASICQUANTITY
_ASSETGROUPECONOMIC.fields_by_name['economics_prices'].message_type = assets__pb2._ECONOMICSPRICE
_RESOURCEECONOMIC.fields_by_name['economics_prices'].message_type = assets__pb2._ECONOMICSPRICE
DESCRIPTOR.message_types_by_name['AssetGroup'] = _ASSETGROUP
DESCRIPTOR.message_types_by_name['AssetGroupOperationLimit'] = _ASSETGROUPOPERATIONLIMIT
DESCRIPTOR.message_types_by_name['AssetGroupEconomic'] = _ASSETGROUPECONOMIC
DESCRIPTOR.message_types_by_name['ResourceEconomic'] = _RESOURCEECONOMIC
DESCRIPTOR.enum_types_by_name['AssetGroupType'] = _ASSETGROUPTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AssetGroup = _reflection.GeneratedProtocolMessageType('AssetGroup', (_message.Message,), {
  'DESCRIPTOR' : _ASSETGROUP,
  '__module__' : 'asset_groups_pb2'
  # @@protoc_insertion_point(class_scope:genesys.AssetGroup)
  })
_sym_db.RegisterMessage(AssetGroup)

AssetGroupOperationLimit = _reflection.GeneratedProtocolMessageType('AssetGroupOperationLimit', (_message.Message,), {
  'DESCRIPTOR' : _ASSETGROUPOPERATIONLIMIT,
  '__module__' : 'asset_groups_pb2'
  # @@protoc_insertion_point(class_scope:genesys.AssetGroupOperationLimit)
  })
_sym_db.RegisterMessage(AssetGroupOperationLimit)

AssetGroupEconomic = _reflection.GeneratedProtocolMessageType('AssetGroupEconomic', (_message.Message,), {
  'DESCRIPTOR' : _ASSETGROUPECONOMIC,
  '__module__' : 'asset_groups_pb2'
  # @@protoc_insertion_point(class_scope:genesys.AssetGroupEconomic)
  })
_sym_db.RegisterMessage(AssetGroupEconomic)

ResourceEconomic = _reflection.GeneratedProtocolMessageType('ResourceEconomic', (_message.Message,), {
  'DESCRIPTOR' : _RESOURCEECONOMIC,
  '__module__' : 'asset_groups_pb2'
  # @@protoc_insertion_point(class_scope:genesys.ResourceEconomic)
  })
_sym_db.RegisterMessage(ResourceEconomic)


# @@protoc_insertion_point(module_scope)
