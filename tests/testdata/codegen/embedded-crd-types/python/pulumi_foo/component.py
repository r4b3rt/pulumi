# coding=utf-8
# *** WARNING: this file was generated by test. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import crd_k8s_amazonaws_com as _crd_k8s_amazonaws_com
import pulumi_kubernetes

__all__ = ['ComponentArgs', 'Component']

@pulumi.input_type
class ComponentArgs:
    def __init__(__self__, *,
                 eni_config: Optional[pulumi.Input[Mapping[str, pulumi.Input['_crd_k8s_amazonaws_com.v1alpha1.ENIConfigSpecArgs']]]] = None,
                 pod: Optional[pulumi.Input['pulumi_kubernetes.core.v1.PodArgs']] = None):
        """
        The set of arguments for constructing a Component resource.
        """
        if eni_config is not None:
            pulumi.set(__self__, "eni_config", eni_config)
        if pod is not None:
            pulumi.set(__self__, "pod", pod)

    @property
    @pulumi.getter(name="eniConfig")
    def eni_config(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input['_crd_k8s_amazonaws_com.v1alpha1.ENIConfigSpecArgs']]]]:
        return pulumi.get(self, "eni_config")

    @eni_config.setter
    def eni_config(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input['_crd_k8s_amazonaws_com.v1alpha1.ENIConfigSpecArgs']]]]):
        pulumi.set(self, "eni_config", value)

    @property
    @pulumi.getter
    def pod(self) -> Optional[pulumi.Input['pulumi_kubernetes.core.v1.PodArgs']]:
        return pulumi.get(self, "pod")

    @pod.setter
    def pod(self, value: Optional[pulumi.Input['pulumi_kubernetes.core.v1.PodArgs']]):
        pulumi.set(self, "pod", value)


class Component(pulumi.ComponentResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 eni_config: Optional[pulumi.Input[Mapping[str, pulumi.Input[Union['_crd_k8s_amazonaws_com.v1alpha1.ENIConfigSpecArgs', '_crd_k8s_amazonaws_com.v1alpha1.ENIConfigSpecArgsDict']]]]] = None,
                 pod: Optional[pulumi.Input[pulumi.InputType['pulumi_kubernetes.core.v1.PodArgs']]] = None,
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
                 eni_config: Optional[pulumi.Input[Mapping[str, pulumi.Input[Union['_crd_k8s_amazonaws_com.v1alpha1.ENIConfigSpecArgs', '_crd_k8s_amazonaws_com.v1alpha1.ENIConfigSpecArgsDict']]]]] = None,
                 pod: Optional[pulumi.Input[pulumi.InputType['pulumi_kubernetes.core.v1.PodArgs']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is not None:
            raise ValueError('ComponentResource classes do not support opts.id')
        else:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ComponentArgs.__new__(ComponentArgs)

            __props__.__dict__["eni_config"] = eni_config
            __props__.__dict__["pod"] = pod
        super(Component, __self__).__init__(
            'foo:index:Component',
            resource_name,
            __props__,
            opts,
            remote=True)

    @property
    @pulumi.getter(name="eniConfig")
    def eni_config(self) -> pulumi.Output[Optional[Mapping[str, '_crd_k8s_amazonaws_com.v1alpha1.outputs.ENIConfigSpec']]]:
        return pulumi.get(self, "eni_config")

    @property
    @pulumi.getter
    def pod(self) -> pulumi.Output[Optional['pulumi_kubernetes.core.v1.outputs.Pod']]:
        return pulumi.get(self, "pod")

