# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import sys
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
if sys.version_info >= (3, 11):
    from typing import NotRequired, TypedDict, TypeAlias
else:
    from typing_extensions import NotRequired, TypedDict, TypeAlias
from .. import _utilities
from .. import outputs as _root_outputs

import types

__config__ = pulumi.Config('config-grpc')


class _ExportableConfig(types.ModuleType):
    @property
    def bool1(self) -> Optional[bool]:
        return __config__.get_bool('bool1')

    @property
    def bool2(self) -> Optional[bool]:
        return __config__.get_bool('bool2')

    @property
    def bool3(self) -> Optional[bool]:
        return __config__.get_bool('bool3')

    @property
    def int1(self) -> Optional[int]:
        return __config__.get_int('int1')

    @property
    def int2(self) -> Optional[int]:
        return __config__.get_int('int2')

    @property
    def int3(self) -> Optional[int]:
        return __config__.get_int('int3')

    @property
    def list_bool1(self) -> Optional[str]:
        return __config__.get('listBool1')

    @property
    def list_bool2(self) -> Optional[str]:
        return __config__.get('listBool2')

    @property
    def list_bool3(self) -> Optional[str]:
        return __config__.get('listBool3')

    @property
    def list_int1(self) -> Optional[str]:
        return __config__.get('listInt1')

    @property
    def list_int2(self) -> Optional[str]:
        return __config__.get('listInt2')

    @property
    def list_int3(self) -> Optional[str]:
        return __config__.get('listInt3')

    @property
    def list_num1(self) -> Optional[str]:
        return __config__.get('listNum1')

    @property
    def list_num2(self) -> Optional[str]:
        return __config__.get('listNum2')

    @property
    def list_num3(self) -> Optional[str]:
        return __config__.get('listNum3')

    @property
    def list_secret_bool1(self) -> Optional[str]:
        return __config__.get('listSecretBool1')

    @property
    def list_secret_bool2(self) -> Optional[str]:
        return __config__.get('listSecretBool2')

    @property
    def list_secret_bool3(self) -> Optional[str]:
        return __config__.get('listSecretBool3')

    @property
    def list_secret_int1(self) -> Optional[str]:
        return __config__.get('listSecretInt1')

    @property
    def list_secret_int2(self) -> Optional[str]:
        return __config__.get('listSecretInt2')

    @property
    def list_secret_int3(self) -> Optional[str]:
        return __config__.get('listSecretInt3')

    @property
    def list_secret_num1(self) -> Optional[str]:
        return __config__.get('listSecretNum1')

    @property
    def list_secret_num2(self) -> Optional[str]:
        return __config__.get('listSecretNum2')

    @property
    def list_secret_num3(self) -> Optional[str]:
        return __config__.get('listSecretNum3')

    @property
    def list_secret_string1(self) -> Optional[str]:
        return __config__.get('listSecretString1')

    @property
    def list_secret_string2(self) -> Optional[str]:
        return __config__.get('listSecretString2')

    @property
    def list_secret_string3(self) -> Optional[str]:
        return __config__.get('listSecretString3')

    @property
    def list_string1(self) -> Optional[str]:
        return __config__.get('listString1')

    @property
    def list_string2(self) -> Optional[str]:
        return __config__.get('listString2')

    @property
    def list_string3(self) -> Optional[str]:
        return __config__.get('listString3')

    @property
    def map_bool1(self) -> Optional[str]:
        return __config__.get('mapBool1')

    @property
    def map_bool2(self) -> Optional[str]:
        return __config__.get('mapBool2')

    @property
    def map_bool3(self) -> Optional[str]:
        return __config__.get('mapBool3')

    @property
    def map_int1(self) -> Optional[str]:
        return __config__.get('mapInt1')

    @property
    def map_int2(self) -> Optional[str]:
        return __config__.get('mapInt2')

    @property
    def map_int3(self) -> Optional[str]:
        return __config__.get('mapInt3')

    @property
    def map_num1(self) -> Optional[str]:
        return __config__.get('mapNum1')

    @property
    def map_num2(self) -> Optional[str]:
        return __config__.get('mapNum2')

    @property
    def map_num3(self) -> Optional[str]:
        return __config__.get('mapNum3')

    @property
    def map_secret_bool1(self) -> Optional[str]:
        return __config__.get('mapSecretBool1')

    @property
    def map_secret_bool2(self) -> Optional[str]:
        return __config__.get('mapSecretBool2')

    @property
    def map_secret_bool3(self) -> Optional[str]:
        return __config__.get('mapSecretBool3')

    @property
    def map_secret_int1(self) -> Optional[str]:
        return __config__.get('mapSecretInt1')

    @property
    def map_secret_int2(self) -> Optional[str]:
        return __config__.get('mapSecretInt2')

    @property
    def map_secret_int3(self) -> Optional[str]:
        return __config__.get('mapSecretInt3')

    @property
    def map_secret_num1(self) -> Optional[str]:
        return __config__.get('mapSecretNum1')

    @property
    def map_secret_num2(self) -> Optional[str]:
        return __config__.get('mapSecretNum2')

    @property
    def map_secret_num3(self) -> Optional[str]:
        return __config__.get('mapSecretNum3')

    @property
    def map_secret_string1(self) -> Optional[str]:
        return __config__.get('mapSecretString1')

    @property
    def map_secret_string2(self) -> Optional[str]:
        return __config__.get('mapSecretString2')

    @property
    def map_secret_string3(self) -> Optional[str]:
        return __config__.get('mapSecretString3')

    @property
    def map_string1(self) -> Optional[str]:
        return __config__.get('mapString1')

    @property
    def map_string2(self) -> Optional[str]:
        return __config__.get('mapString2')

    @property
    def map_string3(self) -> Optional[str]:
        return __config__.get('mapString3')

    @property
    def num1(self) -> Optional[float]:
        return __config__.get_float('num1')

    @property
    def num2(self) -> Optional[float]:
        return __config__.get_float('num2')

    @property
    def num3(self) -> Optional[float]:
        return __config__.get_float('num3')

    @property
    def obj_bool1(self) -> Optional[str]:
        return __config__.get('objBool1')

    @property
    def obj_bool2(self) -> Optional[str]:
        return __config__.get('objBool2')

    @property
    def obj_bool3(self) -> Optional[str]:
        return __config__.get('objBool3')

    @property
    def obj_int1(self) -> Optional[str]:
        return __config__.get('objInt1')

    @property
    def obj_int2(self) -> Optional[str]:
        return __config__.get('objInt2')

    @property
    def obj_int3(self) -> Optional[str]:
        return __config__.get('objInt3')

    @property
    def obj_num1(self) -> Optional[str]:
        return __config__.get('objNum1')

    @property
    def obj_num2(self) -> Optional[str]:
        return __config__.get('objNum2')

    @property
    def obj_num3(self) -> Optional[str]:
        return __config__.get('objNum3')

    @property
    def obj_secret_bool1(self) -> Optional[str]:
        return __config__.get('objSecretBool1')

    @property
    def obj_secret_bool2(self) -> Optional[str]:
        return __config__.get('objSecretBool2')

    @property
    def obj_secret_bool3(self) -> Optional[str]:
        return __config__.get('objSecretBool3')

    @property
    def obj_secret_int1(self) -> Optional[str]:
        return __config__.get('objSecretInt1')

    @property
    def obj_secret_int2(self) -> Optional[str]:
        return __config__.get('objSecretInt2')

    @property
    def obj_secret_int3(self) -> Optional[str]:
        return __config__.get('objSecretInt3')

    @property
    def obj_secret_num1(self) -> Optional[str]:
        return __config__.get('objSecretNum1')

    @property
    def obj_secret_num2(self) -> Optional[str]:
        return __config__.get('objSecretNum2')

    @property
    def obj_secret_num3(self) -> Optional[str]:
        return __config__.get('objSecretNum3')

    @property
    def obj_secret_string1(self) -> Optional[str]:
        return __config__.get('objSecretString1')

    @property
    def obj_secret_string2(self) -> Optional[str]:
        return __config__.get('objSecretString2')

    @property
    def obj_secret_string3(self) -> Optional[str]:
        return __config__.get('objSecretString3')

    @property
    def obj_string1(self) -> Optional[str]:
        return __config__.get('objString1')

    @property
    def obj_string2(self) -> Optional[str]:
        return __config__.get('objString2')

    @property
    def obj_string3(self) -> Optional[str]:
        return __config__.get('objString3')

    @property
    def secret_bool1(self) -> Optional[bool]:
        return __config__.get_bool('secretBool1')

    @property
    def secret_bool2(self) -> Optional[bool]:
        return __config__.get_bool('secretBool2')

    @property
    def secret_bool3(self) -> Optional[bool]:
        return __config__.get_bool('secretBool3')

    @property
    def secret_int1(self) -> Optional[int]:
        return __config__.get_int('secretInt1')

    @property
    def secret_int2(self) -> Optional[int]:
        return __config__.get_int('secretInt2')

    @property
    def secret_int3(self) -> Optional[int]:
        return __config__.get_int('secretInt3')

    @property
    def secret_num1(self) -> Optional[float]:
        return __config__.get_float('secretNum1')

    @property
    def secret_num2(self) -> Optional[float]:
        return __config__.get_float('secretNum2')

    @property
    def secret_num3(self) -> Optional[float]:
        return __config__.get_float('secretNum3')

    @property
    def secret_string1(self) -> Optional[str]:
        return __config__.get('secretString1')

    @property
    def secret_string2(self) -> Optional[str]:
        return __config__.get('secretString2')

    @property
    def secret_string3(self) -> Optional[str]:
        return __config__.get('secretString3')

    @property
    def string1(self) -> Optional[str]:
        return __config__.get('string1')

    @property
    def string2(self) -> Optional[str]:
        return __config__.get('string2')

    @property
    def string3(self) -> Optional[str]:
        return __config__.get('string3')

