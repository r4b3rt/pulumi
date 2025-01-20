# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['ResourceArgs', 'Resource']

@pulumi.input_type
class ResourceArgs:
    def __init__(__self__, *,
                 boolean: pulumi.Input[bool],
                 boolean_map: pulumi.Input[Mapping[str, pulumi.Input[bool]]],
                 float: pulumi.Input[float],
                 integer: pulumi.Input[int],
                 number_array: pulumi.Input[Sequence[pulumi.Input[float]]],
                 string: pulumi.Input[str]):
        """
        The set of arguments for constructing a Resource resource.
        """
        pulumi.set(__self__, "boolean", boolean)
        pulumi.set(__self__, "boolean_map", boolean_map)
        pulumi.set(__self__, "float", float)
        pulumi.set(__self__, "integer", integer)
        pulumi.set(__self__, "number_array", number_array)
        pulumi.set(__self__, "string", string)

    @property
    @pulumi.getter
    def boolean(self) -> pulumi.Input[bool]:
        return pulumi.get(self, "boolean")

    @boolean.setter
    def boolean(self, value: pulumi.Input[bool]):
        pulumi.set(self, "boolean", value)

    @property
    @pulumi.getter(name="booleanMap")
    def boolean_map(self) -> pulumi.Input[Mapping[str, pulumi.Input[bool]]]:
        return pulumi.get(self, "boolean_map")

    @boolean_map.setter
    def boolean_map(self, value: pulumi.Input[Mapping[str, pulumi.Input[bool]]]):
        pulumi.set(self, "boolean_map", value)

    @property
    @pulumi.getter
    def float(self) -> pulumi.Input[float]:
        return pulumi.get(self, "float")

    @float.setter
    def float(self, value: pulumi.Input[float]):
        pulumi.set(self, "float", value)

    @property
    @pulumi.getter
    def integer(self) -> pulumi.Input[int]:
        return pulumi.get(self, "integer")

    @integer.setter
    def integer(self, value: pulumi.Input[int]):
        pulumi.set(self, "integer", value)

    @property
    @pulumi.getter(name="numberArray")
    def number_array(self) -> pulumi.Input[Sequence[pulumi.Input[float]]]:
        return pulumi.get(self, "number_array")

    @number_array.setter
    def number_array(self, value: pulumi.Input[Sequence[pulumi.Input[float]]]):
        pulumi.set(self, "number_array", value)

    @property
    @pulumi.getter
    def string(self) -> pulumi.Input[str]:
        return pulumi.get(self, "string")

    @string.setter
    def string(self, value: pulumi.Input[str]):
        pulumi.set(self, "string", value)


class Resource(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 boolean: Optional[pulumi.Input[bool]] = None,
                 boolean_map: Optional[pulumi.Input[Mapping[str, pulumi.Input[bool]]]] = None,
                 float: Optional[pulumi.Input[float]] = None,
                 integer: Optional[pulumi.Input[int]] = None,
                 number_array: Optional[pulumi.Input[Sequence[pulumi.Input[float]]]] = None,
                 string: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a Resource resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ResourceArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a Resource resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param ResourceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ResourceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 boolean: Optional[pulumi.Input[bool]] = None,
                 boolean_map: Optional[pulumi.Input[Mapping[str, pulumi.Input[bool]]]] = None,
                 float: Optional[pulumi.Input[float]] = None,
                 integer: Optional[pulumi.Input[int]] = None,
                 number_array: Optional[pulumi.Input[Sequence[pulumi.Input[float]]]] = None,
                 string: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ResourceArgs.__new__(ResourceArgs)

            if boolean is None and not opts.urn:
                raise TypeError("Missing required property 'boolean'")
            __props__.__dict__["boolean"] = boolean
            if boolean_map is None and not opts.urn:
                raise TypeError("Missing required property 'boolean_map'")
            __props__.__dict__["boolean_map"] = boolean_map
            if float is None and not opts.urn:
                raise TypeError("Missing required property 'float'")
            __props__.__dict__["float"] = float
            if integer is None and not opts.urn:
                raise TypeError("Missing required property 'integer'")
            __props__.__dict__["integer"] = integer
            if number_array is None and not opts.urn:
                raise TypeError("Missing required property 'number_array'")
            __props__.__dict__["number_array"] = number_array
            if string is None and not opts.urn:
                raise TypeError("Missing required property 'string'")
            __props__.__dict__["string"] = string
        super(Resource, __self__).__init__(
            'primitive:index:Resource',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Resource':
        """
        Get an existing Resource resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ResourceArgs.__new__(ResourceArgs)

        __props__.__dict__["boolean"] = None
        __props__.__dict__["boolean_map"] = None
        __props__.__dict__["float"] = None
        __props__.__dict__["integer"] = None
        __props__.__dict__["number_array"] = None
        __props__.__dict__["string"] = None
        return Resource(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def boolean(self) -> pulumi.Output[bool]:
        return pulumi.get(self, "boolean")

    @property
    @pulumi.getter(name="booleanMap")
    def boolean_map(self) -> pulumi.Output[Mapping[str, bool]]:
        return pulumi.get(self, "boolean_map")

    @property
    @pulumi.getter
    def float(self) -> pulumi.Output[float]:
        return pulumi.get(self, "float")

    @property
    @pulumi.getter
    def integer(self) -> pulumi.Output[int]:
        return pulumi.get(self, "integer")

    @property
    @pulumi.getter(name="numberArray")
    def number_array(self) -> pulumi.Output[Sequence[float]]:
        return pulumi.get(self, "number_array")

    @property
    @pulumi.getter
    def string(self) -> pulumi.Output[str]:
        return pulumi.get(self, "string")

