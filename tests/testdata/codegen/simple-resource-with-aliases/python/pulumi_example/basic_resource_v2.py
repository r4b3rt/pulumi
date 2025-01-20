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

__all__ = ['BasicResourceV2Args', 'BasicResourceV2']

@pulumi.input_type
class BasicResourceV2Args:
    def __init__(__self__, *,
                 bar: pulumi.Input[str]):
        """
        The set of arguments for constructing a BasicResourceV2 resource.
        """
        pulumi.set(__self__, "bar", bar)

    @property
    @pulumi.getter
    def bar(self) -> pulumi.Input[str]:
        return pulumi.get(self, "bar")

    @bar.setter
    def bar(self, value: pulumi.Input[str]):
        pulumi.set(self, "bar", value)


class BasicResourceV2(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bar: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a BasicResourceV2 resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: BasicResourceV2Args,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a BasicResourceV2 resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param BasicResourceV2Args args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(BasicResourceV2Args, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bar: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = BasicResourceV2Args.__new__(BasicResourceV2Args)

            if bar is None and not opts.urn:
                raise TypeError("Missing required property 'bar'")
            __props__.__dict__["bar"] = bar
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="example:index:BasicResource")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(BasicResourceV2, __self__).__init__(
            'example:index:BasicResourceV2',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'BasicResourceV2':
        """
        Get an existing BasicResourceV2 resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = BasicResourceV2Args.__new__(BasicResourceV2Args)

        __props__.__dict__["bar"] = None
        return BasicResourceV2(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def bar(self) -> pulumi.Output[str]:
        return pulumi.get(self, "bar")

