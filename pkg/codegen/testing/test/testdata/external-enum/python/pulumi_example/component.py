# coding=utf-8
# *** WARNING: this file was generated by test. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import local
import pulumi_google_native

__all__ = ['ComponentArgs', 'Component']

@pulumi.input_type
class ComponentArgs:
    def __init__(__self__, *,
                 local_enum: Optional[pulumi.Input['local.MyEnum']] = None,
                 remote_enum: Optional[pulumi.Input['pulumi_google_native.accesscontextmanager.v1.DevicePolicyAllowedDeviceManagementLevelsItem']] = None):
        """
        The set of arguments for constructing a Component resource.
        """
        if local_enum is not None:
            pulumi.set(__self__, "local_enum", local_enum)
        if remote_enum is not None:
            pulumi.set(__self__, "remote_enum", remote_enum)

    @property
    @pulumi.getter(name="localEnum")
    def local_enum(self) -> Optional[pulumi.Input['local.MyEnum']]:
        return pulumi.get(self, "local_enum")

    @local_enum.setter
    def local_enum(self, value: Optional[pulumi.Input['local.MyEnum']]):
        pulumi.set(self, "local_enum", value)

    @property
    @pulumi.getter(name="remoteEnum")
    def remote_enum(self) -> Optional[pulumi.Input['pulumi_google_native.accesscontextmanager.v1.DevicePolicyAllowedDeviceManagementLevelsItem']]:
        return pulumi.get(self, "remote_enum")

    @remote_enum.setter
    def remote_enum(self, value: Optional[pulumi.Input['pulumi_google_native.accesscontextmanager.v1.DevicePolicyAllowedDeviceManagementLevelsItem']]):
        pulumi.set(self, "remote_enum", value)


class Component(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 local_enum: Optional[pulumi.Input['local.MyEnum']] = None,
                 remote_enum: Optional[pulumi.Input['pulumi_google_native.accesscontextmanager.v1.DevicePolicyAllowedDeviceManagementLevelsItem']] = None,
                 __props__=None):
        """
        Create a Component resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[ComponentArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a Component resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param ComponentArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ComponentArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 local_enum: Optional[pulumi.Input['local.MyEnum']] = None,
                 remote_enum: Optional[pulumi.Input['pulumi_google_native.accesscontextmanager.v1.DevicePolicyAllowedDeviceManagementLevelsItem']] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ComponentArgs.__new__(ComponentArgs)

            __props__.__dict__["local_enum"] = local_enum
            __props__.__dict__["remote_enum"] = remote_enum
        super(Component, __self__).__init__(
            'example:index:Component',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Component':
        """
        Get an existing Component resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ComponentArgs.__new__(ComponentArgs)

        __props__.__dict__["local_enum"] = None
        __props__.__dict__["remote_enum"] = None
        return Component(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="localEnum")
    def local_enum(self) -> pulumi.Output[Optional['local.MyEnum']]:
        return pulumi.get(self, "local_enum")

    @property
    @pulumi.getter(name="remoteEnum")
    def remote_enum(self) -> pulumi.Output[Optional['pulumi_google_native.accesscontextmanager.v1.DevicePolicyAllowedDeviceManagementLevelsItem']]:
        return pulumi.get(self, "remote_enum")

