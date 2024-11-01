# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'Tbool1',
    'Tbool2',
    'Tbool3',
    'Tint1',
    'Tint2',
    'Tint3',
    'Tnum1',
    'Tnum2',
    'Tnum3',
    'TsecretBool1',
    'TsecretBool2',
    'TsecretBool3',
    'TsecretInt1',
    'TsecretInt2',
    'TsecretInt3',
    'TsecretNum1',
    'TsecretNum2',
    'TsecretNum3',
    'TsecretString1',
    'TsecretString2',
    'TsecretString3',
    'Tstring1',
    'Tstring2',
    'Tstring3',
]

@pulumi.output_type
class Tbool1(dict):
    def __init__(__self__, *,
                 x: Optional[bool] = None):
        if x is not None:
            pulumi.set(__self__, "x", x)

    @property
    @pulumi.getter
    def x(self) -> Optional[bool]:
        return pulumi.get(self, "x")


@pulumi.output_type
class Tbool2(dict):
    def __init__(__self__, *,
                 x: Optional[bool] = None):
        if x is not None:
            pulumi.set(__self__, "x", x)

    @property
    @pulumi.getter
    def x(self) -> Optional[bool]:
        return pulumi.get(self, "x")


@pulumi.output_type
class Tbool3(dict):
    def __init__(__self__, *,
                 x: Optional[bool] = None):
        if x is not None:
            pulumi.set(__self__, "x", x)

    @property
    @pulumi.getter
    def x(self) -> Optional[bool]:
        return pulumi.get(self, "x")


@pulumi.output_type
class Tint1(dict):
    def __init__(__self__, *,
                 x: Optional[int] = None):
        if x is not None:
            pulumi.set(__self__, "x", x)

    @property
    @pulumi.getter
    def x(self) -> Optional[int]:
        return pulumi.get(self, "x")


@pulumi.output_type
class Tint2(dict):
    def __init__(__self__, *,
                 x: Optional[int] = None):
        if x is not None:
            pulumi.set(__self__, "x", x)

    @property
    @pulumi.getter
    def x(self) -> Optional[int]:
        return pulumi.get(self, "x")


@pulumi.output_type
class Tint3(dict):
    def __init__(__self__, *,
                 x: Optional[int] = None):
        if x is not None:
            pulumi.set(__self__, "x", x)

    @property
    @pulumi.getter
    def x(self) -> Optional[int]:
        return pulumi.get(self, "x")


@pulumi.output_type
class Tnum1(dict):
    def __init__(__self__, *,
                 x: Optional[float] = None):
        if x is not None:
            pulumi.set(__self__, "x", x)

    @property
    @pulumi.getter
    def x(self) -> Optional[float]:
        return pulumi.get(self, "x")


@pulumi.output_type
class Tnum2(dict):
    def __init__(__self__, *,
                 x: Optional[float] = None):
        if x is not None:
            pulumi.set(__self__, "x", x)

    @property
    @pulumi.getter
    def x(self) -> Optional[float]:
        return pulumi.get(self, "x")


@pulumi.output_type
class Tnum3(dict):
    def __init__(__self__, *,
                 x: Optional[float] = None):
        if x is not None:
            pulumi.set(__self__, "x", x)

    @property
    @pulumi.getter
    def x(self) -> Optional[float]:
        return pulumi.get(self, "x")


@pulumi.output_type
class TsecretBool1(dict):
    def __init__(__self__, *,
                 secret_x: Optional[bool] = None):
        if secret_x is not None:
            pulumi.set(__self__, "secret_x", secret_x)

    @property
    @pulumi.getter(name="secretX")
    def secret_x(self) -> Optional[bool]:
        return pulumi.get(self, "secret_x")


@pulumi.output_type
class TsecretBool2(dict):
    def __init__(__self__, *,
                 secret_x: Optional[bool] = None):
        if secret_x is not None:
            pulumi.set(__self__, "secret_x", secret_x)

    @property
    @pulumi.getter(name="secretX")
    def secret_x(self) -> Optional[bool]:
        return pulumi.get(self, "secret_x")


@pulumi.output_type
class TsecretBool3(dict):
    def __init__(__self__, *,
                 secret_x: Optional[bool] = None):
        if secret_x is not None:
            pulumi.set(__self__, "secret_x", secret_x)

    @property
    @pulumi.getter(name="secretX")
    def secret_x(self) -> Optional[bool]:
        return pulumi.get(self, "secret_x")


@pulumi.output_type
class TsecretInt1(dict):
    def __init__(__self__, *,
                 secret_x: Optional[int] = None):
        if secret_x is not None:
            pulumi.set(__self__, "secret_x", secret_x)

    @property
    @pulumi.getter(name="secretX")
    def secret_x(self) -> Optional[int]:
        return pulumi.get(self, "secret_x")


@pulumi.output_type
class TsecretInt2(dict):
    def __init__(__self__, *,
                 secret_x: Optional[int] = None):
        if secret_x is not None:
            pulumi.set(__self__, "secret_x", secret_x)

    @property
    @pulumi.getter(name="secretX")
    def secret_x(self) -> Optional[int]:
        return pulumi.get(self, "secret_x")


@pulumi.output_type
class TsecretInt3(dict):
    def __init__(__self__, *,
                 secret_x: Optional[int] = None):
        if secret_x is not None:
            pulumi.set(__self__, "secret_x", secret_x)

    @property
    @pulumi.getter(name="secretX")
    def secret_x(self) -> Optional[int]:
        return pulumi.get(self, "secret_x")


@pulumi.output_type
class TsecretNum1(dict):
    def __init__(__self__, *,
                 secret_x: Optional[float] = None):
        if secret_x is not None:
            pulumi.set(__self__, "secret_x", secret_x)

    @property
    @pulumi.getter(name="secretX")
    def secret_x(self) -> Optional[float]:
        return pulumi.get(self, "secret_x")


@pulumi.output_type
class TsecretNum2(dict):
    def __init__(__self__, *,
                 secret_x: Optional[float] = None):
        if secret_x is not None:
            pulumi.set(__self__, "secret_x", secret_x)

    @property
    @pulumi.getter(name="secretX")
    def secret_x(self) -> Optional[float]:
        return pulumi.get(self, "secret_x")


@pulumi.output_type
class TsecretNum3(dict):
    def __init__(__self__, *,
                 secret_x: Optional[float] = None):
        if secret_x is not None:
            pulumi.set(__self__, "secret_x", secret_x)

    @property
    @pulumi.getter(name="secretX")
    def secret_x(self) -> Optional[float]:
        return pulumi.get(self, "secret_x")


@pulumi.output_type
class TsecretString1(dict):
    def __init__(__self__, *,
                 secret_x: Optional[str] = None):
        if secret_x is not None:
            pulumi.set(__self__, "secret_x", secret_x)

    @property
    @pulumi.getter(name="secretX")
    def secret_x(self) -> Optional[str]:
        return pulumi.get(self, "secret_x")


@pulumi.output_type
class TsecretString2(dict):
    def __init__(__self__, *,
                 secret_x: Optional[str] = None):
        if secret_x is not None:
            pulumi.set(__self__, "secret_x", secret_x)

    @property
    @pulumi.getter(name="secretX")
    def secret_x(self) -> Optional[str]:
        return pulumi.get(self, "secret_x")


@pulumi.output_type
class TsecretString3(dict):
    def __init__(__self__, *,
                 secret_x: Optional[str] = None):
        if secret_x is not None:
            pulumi.set(__self__, "secret_x", secret_x)

    @property
    @pulumi.getter(name="secretX")
    def secret_x(self) -> Optional[str]:
        return pulumi.get(self, "secret_x")


@pulumi.output_type
class Tstring1(dict):
    def __init__(__self__, *,
                 x: Optional[str] = None):
        if x is not None:
            pulumi.set(__self__, "x", x)

    @property
    @pulumi.getter
    def x(self) -> Optional[str]:
        return pulumi.get(self, "x")


@pulumi.output_type
class Tstring2(dict):
    def __init__(__self__, *,
                 x: Optional[str] = None):
        if x is not None:
            pulumi.set(__self__, "x", x)

    @property
    @pulumi.getter
    def x(self) -> Optional[str]:
        return pulumi.get(self, "x")


@pulumi.output_type
class Tstring3(dict):
    def __init__(__self__, *,
                 x: Optional[str] = None):
        if x is not None:
            pulumi.set(__self__, "x", x)

    @property
    @pulumi.getter
    def x(self) -> Optional[str]:
        return pulumi.get(self, "x")

