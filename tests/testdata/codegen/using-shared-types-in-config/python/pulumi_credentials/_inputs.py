# coding=utf-8
# *** WARNING: this file was generated by test. ***
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
from . import _utilities
from ._enums import *

__all__ = [
    'SharedArgs',
    'SharedArgsDict',
]

MYPY = False

if not MYPY:
    class SharedArgsDict(TypedDict):
        foo: NotRequired[pulumi.Input[str]]
elif False:
    SharedArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class SharedArgs:
    def __init__(__self__, *,
                 foo: Optional[pulumi.Input[str]] = None):
        if foo is not None:
            pulumi.set(__self__, "foo", foo)

    @property
    @pulumi.getter
    def foo(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "foo")

    @foo.setter
    def foo(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "foo", value)


