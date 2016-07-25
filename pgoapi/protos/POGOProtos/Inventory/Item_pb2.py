# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: POGOProtos.Inventory.Item.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='POGOProtos.Inventory.Item.proto',
  package='POGOProtos.Inventory.Item',
  syntax='proto3',
  serialized_pb=_b('\n\x1fPOGOProtos.Inventory.Item.proto\x12\x19POGOProtos.Inventory.Item\"S\n\tItemAward\x12\x32\n\x07item_id\x18\x01 \x01(\x0e\x32!.POGOProtos.Inventory.Item.ItemId\x12\x12\n\nitem_count\x18\x02 \x01(\x05\"]\n\x08ItemData\x12\x32\n\x07item_id\x18\x01 \x01(\x0e\x32!.POGOProtos.Inventory.Item.ItemId\x12\r\n\x05\x63ount\x18\x02 \x01(\x05\x12\x0e\n\x06unseen\x18\x03 \x01(\x08*\xb2\x02\n\x08ItemType\x12\x12\n\x0eITEM_TYPE_NONE\x10\x00\x12\x16\n\x12ITEM_TYPE_POKEBALL\x10\x01\x12\x14\n\x10ITEM_TYPE_POTION\x10\x02\x12\x14\n\x10ITEM_TYPE_REVIVE\x10\x03\x12\x11\n\rITEM_TYPE_MAP\x10\x04\x12\x14\n\x10ITEM_TYPE_BATTLE\x10\x05\x12\x12\n\x0eITEM_TYPE_FOOD\x10\x06\x12\x14\n\x10ITEM_TYPE_CAMERA\x10\x07\x12\x12\n\x0eITEM_TYPE_DISK\x10\x08\x12\x17\n\x13ITEM_TYPE_INCUBATOR\x10\t\x12\x15\n\x11ITEM_TYPE_INCENSE\x10\n\x12\x16\n\x12ITEM_TYPE_XP_BOOST\x10\x0b\x12\x1f\n\x1bITEM_TYPE_INVENTORY_UPGRADE\x10\x0c*\xc7\x05\n\x06ItemId\x12\x10\n\x0cITEM_UNKNOWN\x10\x00\x12\x12\n\x0eITEM_POKE_BALL\x10\x01\x12\x13\n\x0fITEM_GREAT_BALL\x10\x02\x12\x13\n\x0fITEM_ULTRA_BALL\x10\x03\x12\x14\n\x10ITEM_MASTER_BALL\x10\x04\x12\x0f\n\x0bITEM_POTION\x10\x65\x12\x15\n\x11ITEM_SUPER_POTION\x10\x66\x12\x15\n\x11ITEM_HYPER_POTION\x10g\x12\x13\n\x0fITEM_MAX_POTION\x10h\x12\x10\n\x0bITEM_REVIVE\x10\xc9\x01\x12\x14\n\x0fITEM_MAX_REVIVE\x10\xca\x01\x12\x13\n\x0eITEM_LUCKY_EGG\x10\xad\x02\x12\x1a\n\x15ITEM_INCENSE_ORDINARY\x10\x91\x03\x12\x17\n\x12ITEM_INCENSE_SPICY\x10\x92\x03\x12\x16\n\x11ITEM_INCENSE_COOL\x10\x93\x03\x12\x18\n\x13ITEM_INCENSE_FLORAL\x10\x94\x03\x12\x13\n\x0eITEM_TROY_DISK\x10\xf5\x03\x12\x12\n\rITEM_X_ATTACK\x10\xda\x04\x12\x13\n\x0eITEM_X_DEFENSE\x10\xdb\x04\x12\x13\n\x0eITEM_X_MIRACLE\x10\xdc\x04\x12\x14\n\x0fITEM_RAZZ_BERRY\x10\xbd\x05\x12\x14\n\x0fITEM_BLUK_BERRY\x10\xbe\x05\x12\x15\n\x10ITEM_NANAB_BERRY\x10\xbf\x05\x12\x15\n\x10ITEM_WEPAR_BERRY\x10\xc0\x05\x12\x15\n\x10ITEM_PINAP_BERRY\x10\xc1\x05\x12\x18\n\x13ITEM_SPECIAL_CAMERA\x10\xa1\x06\x12#\n\x1eITEM_INCUBATOR_BASIC_UNLIMITED\x10\x85\x07\x12\x19\n\x14ITEM_INCUBATOR_BASIC\x10\x86\x07\x12!\n\x1cITEM_POKEMON_STORAGE_UPGRADE\x10\xe9\x07\x12\x1e\n\x19ITEM_ITEM_STORAGE_UPGRADE\x10\xea\x07\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_ITEMTYPE = _descriptor.EnumDescriptor(
  name='ItemType',
  full_name='POGOProtos.Inventory.Item.ItemType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ITEM_TYPE_NONE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_TYPE_POKEBALL', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_TYPE_POTION', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_TYPE_REVIVE', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_TYPE_MAP', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_TYPE_BATTLE', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_TYPE_FOOD', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_TYPE_CAMERA', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_TYPE_DISK', index=8, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_TYPE_INCUBATOR', index=9, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_TYPE_INCENSE', index=10, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_TYPE_XP_BOOST', index=11, number=11,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_TYPE_INVENTORY_UPGRADE', index=12, number=12,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=243,
  serialized_end=549,
)
_sym_db.RegisterEnumDescriptor(_ITEMTYPE)

ItemType = enum_type_wrapper.EnumTypeWrapper(_ITEMTYPE)
_ITEMID = _descriptor.EnumDescriptor(
  name='ItemId',
  full_name='POGOProtos.Inventory.Item.ItemId',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ITEM_UNKNOWN', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_POKE_BALL', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_GREAT_BALL', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_ULTRA_BALL', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_MASTER_BALL', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_POTION', index=5, number=101,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_SUPER_POTION', index=6, number=102,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_HYPER_POTION', index=7, number=103,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_MAX_POTION', index=8, number=104,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_REVIVE', index=9, number=201,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_MAX_REVIVE', index=10, number=202,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_LUCKY_EGG', index=11, number=301,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_INCENSE_ORDINARY', index=12, number=401,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_INCENSE_SPICY', index=13, number=402,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_INCENSE_COOL', index=14, number=403,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_INCENSE_FLORAL', index=15, number=404,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_TROY_DISK', index=16, number=501,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_X_ATTACK', index=17, number=602,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_X_DEFENSE', index=18, number=603,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_X_MIRACLE', index=19, number=604,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_RAZZ_BERRY', index=20, number=701,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_BLUK_BERRY', index=21, number=702,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_NANAB_BERRY', index=22, number=703,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_WEPAR_BERRY', index=23, number=704,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_PINAP_BERRY', index=24, number=705,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_SPECIAL_CAMERA', index=25, number=801,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_INCUBATOR_BASIC_UNLIMITED', index=26, number=901,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_INCUBATOR_BASIC', index=27, number=902,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_POKEMON_STORAGE_UPGRADE', index=28, number=1001,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_ITEM_STORAGE_UPGRADE', index=29, number=1002,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=552,
  serialized_end=1263,
)
_sym_db.RegisterEnumDescriptor(_ITEMID)

ItemId = enum_type_wrapper.EnumTypeWrapper(_ITEMID)
ITEM_TYPE_NONE = 0
ITEM_TYPE_POKEBALL = 1
ITEM_TYPE_POTION = 2
ITEM_TYPE_REVIVE = 3
ITEM_TYPE_MAP = 4
ITEM_TYPE_BATTLE = 5
ITEM_TYPE_FOOD = 6
ITEM_TYPE_CAMERA = 7
ITEM_TYPE_DISK = 8
ITEM_TYPE_INCUBATOR = 9
ITEM_TYPE_INCENSE = 10
ITEM_TYPE_XP_BOOST = 11
ITEM_TYPE_INVENTORY_UPGRADE = 12
ITEM_UNKNOWN = 0
ITEM_POKE_BALL = 1
ITEM_GREAT_BALL = 2
ITEM_ULTRA_BALL = 3
ITEM_MASTER_BALL = 4
ITEM_POTION = 101
ITEM_SUPER_POTION = 102
ITEM_HYPER_POTION = 103
ITEM_MAX_POTION = 104
ITEM_REVIVE = 201
ITEM_MAX_REVIVE = 202
ITEM_LUCKY_EGG = 301
ITEM_INCENSE_ORDINARY = 401
ITEM_INCENSE_SPICY = 402
ITEM_INCENSE_COOL = 403
ITEM_INCENSE_FLORAL = 404
ITEM_TROY_DISK = 501
ITEM_X_ATTACK = 602
ITEM_X_DEFENSE = 603
ITEM_X_MIRACLE = 604
ITEM_RAZZ_BERRY = 701
ITEM_BLUK_BERRY = 702
ITEM_NANAB_BERRY = 703
ITEM_WEPAR_BERRY = 704
ITEM_PINAP_BERRY = 705
ITEM_SPECIAL_CAMERA = 801
ITEM_INCUBATOR_BASIC_UNLIMITED = 901
ITEM_INCUBATOR_BASIC = 902
ITEM_POKEMON_STORAGE_UPGRADE = 1001
ITEM_ITEM_STORAGE_UPGRADE = 1002



_ITEMAWARD = _descriptor.Descriptor(
  name='ItemAward',
  full_name='POGOProtos.Inventory.Item.ItemAward',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='item_id', full_name='POGOProtos.Inventory.Item.ItemAward.item_id', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='item_count', full_name='POGOProtos.Inventory.Item.ItemAward.item_count', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=62,
  serialized_end=145,
)


_ITEMDATA = _descriptor.Descriptor(
  name='ItemData',
  full_name='POGOProtos.Inventory.Item.ItemData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='item_id', full_name='POGOProtos.Inventory.Item.ItemData.item_id', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='count', full_name='POGOProtos.Inventory.Item.ItemData.count', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unseen', full_name='POGOProtos.Inventory.Item.ItemData.unseen', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=147,
  serialized_end=240,
)

_ITEMAWARD.fields_by_name['item_id'].enum_type = _ITEMID
_ITEMDATA.fields_by_name['item_id'].enum_type = _ITEMID
DESCRIPTOR.message_types_by_name['ItemAward'] = _ITEMAWARD
DESCRIPTOR.message_types_by_name['ItemData'] = _ITEMDATA
DESCRIPTOR.enum_types_by_name['ItemType'] = _ITEMTYPE
DESCRIPTOR.enum_types_by_name['ItemId'] = _ITEMID

ItemAward = _reflection.GeneratedProtocolMessageType('ItemAward', (_message.Message,), dict(
  DESCRIPTOR = _ITEMAWARD,
  __module__ = 'POGOProtos.Inventory.Item_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Inventory.Item.ItemAward)
  ))
_sym_db.RegisterMessage(ItemAward)

ItemData = _reflection.GeneratedProtocolMessageType('ItemData', (_message.Message,), dict(
  DESCRIPTOR = _ITEMDATA,
  __module__ = 'POGOProtos.Inventory.Item_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Inventory.Item.ItemData)
  ))
_sym_db.RegisterMessage(ItemData)


# @@protoc_insertion_point(module_scope)
