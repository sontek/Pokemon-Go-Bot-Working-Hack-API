# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: POGOProtos.Data.Gym.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from POGOProtos.Map import Fort_pb2 as POGOProtos_dot_Map_dot_Fort__pb2
POGOProtos_dot_Enums__pb2 = POGOProtos_dot_Map_dot_Fort__pb2.POGOProtos_dot_Enums__pb2
POGOProtos_dot_Inventory_dot_Item__pb2 = POGOProtos_dot_Map_dot_Fort__pb2.POGOProtos_dot_Inventory_dot_Item__pb2
from POGOProtos import Data_pb2 as POGOProtos_dot_Data__pb2
POGOProtos_dot_Enums__pb2 = POGOProtos_dot_Data__pb2.POGOProtos_dot_Enums__pb2
POGOProtos_dot_Inventory_dot_Item__pb2 = POGOProtos_dot_Data__pb2.POGOProtos_dot_Inventory_dot_Item__pb2
POGOProtos_dot_Data_dot_Player__pb2 = POGOProtos_dot_Data__pb2.POGOProtos_dot_Data_dot_Player__pb2
POGOProtos_dot_Enums__pb2 = POGOProtos_dot_Data__pb2.POGOProtos_dot_Enums__pb2
from POGOProtos.Data import Player_pb2 as POGOProtos_dot_Data_dot_Player__pb2
POGOProtos_dot_Enums__pb2 = POGOProtos_dot_Data_dot_Player__pb2.POGOProtos_dot_Enums__pb2

from POGOProtos.Map.Fort_pb2 import *
from POGOProtos.Data_pb2 import *
from POGOProtos.Data.Player_pb2 import *

DESCRIPTOR = _descriptor.FileDescriptor(
  name='POGOProtos.Data.Gym.proto',
  package='POGOProtos.Data.Gym',
  syntax='proto3',
  serialized_pb=_b('\n\x19POGOProtos.Data.Gym.proto\x12\x13POGOProtos.Data.Gym\x1a\x19POGOProtos.Map.Fort.proto\x1a\x15POGOProtos.Data.proto\x1a\x1cPOGOProtos.Data.Player.proto\"u\n\x08GymState\x12\x30\n\tfort_data\x18\x01 \x01(\x0b\x32\x1d.POGOProtos.Map.Fort.FortData\x12\x37\n\x0bmemberships\x18\x02 \x03(\x0b\x32\".POGOProtos.Data.Gym.GymMembership\"\x90\x01\n\rGymMembership\x12\x32\n\x0cpokemon_data\x18\x01 \x01(\x0b\x32\x1c.POGOProtos.Data.PokemonData\x12K\n\x16trainer_public_profile\x18\x02 \x01(\x0b\x32+.POGOProtos.Data.Player.PlayerPublicProfileP\x00P\x01P\x02\x62\x06proto3')
  ,
  dependencies=[POGOProtos_dot_Map_dot_Fort__pb2.DESCRIPTOR,POGOProtos_dot_Data__pb2.DESCRIPTOR,POGOProtos_dot_Data_dot_Player__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_GYMSTATE = _descriptor.Descriptor(
  name='GymState',
  full_name='POGOProtos.Data.Gym.GymState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='fort_data', full_name='POGOProtos.Data.Gym.GymState.fort_data', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='memberships', full_name='POGOProtos.Data.Gym.GymState.memberships', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=130,
  serialized_end=247,
)


_GYMMEMBERSHIP = _descriptor.Descriptor(
  name='GymMembership',
  full_name='POGOProtos.Data.Gym.GymMembership',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pokemon_data', full_name='POGOProtos.Data.Gym.GymMembership.pokemon_data', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='trainer_public_profile', full_name='POGOProtos.Data.Gym.GymMembership.trainer_public_profile', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=250,
  serialized_end=394,
)

_GYMSTATE.fields_by_name['fort_data'].message_type = POGOProtos_dot_Map_dot_Fort__pb2._FORTDATA
_GYMSTATE.fields_by_name['memberships'].message_type = _GYMMEMBERSHIP
_GYMMEMBERSHIP.fields_by_name['pokemon_data'].message_type = POGOProtos_dot_Data__pb2._POKEMONDATA
_GYMMEMBERSHIP.fields_by_name['trainer_public_profile'].message_type = POGOProtos_dot_Data_dot_Player__pb2._PLAYERPUBLICPROFILE
DESCRIPTOR.message_types_by_name['GymState'] = _GYMSTATE
DESCRIPTOR.message_types_by_name['GymMembership'] = _GYMMEMBERSHIP

GymState = _reflection.GeneratedProtocolMessageType('GymState', (_message.Message,), dict(
  DESCRIPTOR = _GYMSTATE,
  __module__ = 'POGOProtos.Data.Gym_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Data.Gym.GymState)
  ))
_sym_db.RegisterMessage(GymState)

GymMembership = _reflection.GeneratedProtocolMessageType('GymMembership', (_message.Message,), dict(
  DESCRIPTOR = _GYMMEMBERSHIP,
  __module__ = 'POGOProtos.Data.Gym_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Data.Gym.GymMembership)
  ))
_sym_db.RegisterMessage(GymMembership)


# @@protoc_insertion_point(module_scope)
