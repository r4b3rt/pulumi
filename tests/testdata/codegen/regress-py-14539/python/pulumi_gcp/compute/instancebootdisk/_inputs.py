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
from ... import _utilities
from ... import compute as _compute

__all__ = [
    'InstanceBootDiskArgs',
    'InstanceBootDiskArgsDict',
]

MYPY = False

if not MYPY:
    class InstanceBootDiskArgsDict(TypedDict):
        initialize_params: pulumi.Input['_compute.instancebootdiskinitializeparams.InstanceBootDiskInitializeParamsArgsDict']
        """
        Parameters for a new disk that will be created
        alongside the new instance. Either `initialize_params` or `source` must be set.
        Structure is documented below.
        """
elif False:
    InstanceBootDiskArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class InstanceBootDiskArgs:
    def __init__(__self__, *,
                 initialize_params: pulumi.Input['_compute.instancebootdiskinitializeparams.InstanceBootDiskInitializeParamsArgs']):
        """
        :param pulumi.Input['_compute.instancebootdiskinitializeparams.InstanceBootDiskInitializeParamsArgs'] initialize_params: Parameters for a new disk that will be created
               alongside the new instance. Either `initialize_params` or `source` must be set.
               Structure is documented below.
        """
        pulumi.set(__self__, "initialize_params", initialize_params)

    @property
    @pulumi.getter(name="initializeParams")
    def initialize_params(self) -> pulumi.Input['_compute.instancebootdiskinitializeparams.InstanceBootDiskInitializeParamsArgs']:
        """
        Parameters for a new disk that will be created
        alongside the new instance. Either `initialize_params` or `source` must be set.
        Structure is documented below.
        """
        return pulumi.get(self, "initialize_params")

    @initialize_params.setter
    def initialize_params(self, value: pulumi.Input['_compute.instancebootdiskinitializeparams.InstanceBootDiskInitializeParamsArgs']):
        pulumi.set(self, "initialize_params", value)


