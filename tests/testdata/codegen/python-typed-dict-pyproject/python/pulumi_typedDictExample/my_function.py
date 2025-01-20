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
from . import outputs
from ._inputs import *
import pulumi_kubernetes

__all__ = [
    'MyFunctionResult',
    'AwaitableMyFunctionResult',
    'my_function',
    'my_function_output',
]

@pulumi.output_type
class MyFunctionResult:
    def __init__(__self__, my_output=None, simple_output=None):
        if my_output and not isinstance(my_output, dict):
            raise TypeError("Expected argument 'my_output' to be a dict")
        pulumi.set(__self__, "my_output", my_output)
        if simple_output and not isinstance(simple_output, str):
            raise TypeError("Expected argument 'simple_output' to be a str")
        pulumi.set(__self__, "simple_output", simple_output)

    @property
    @pulumi.getter(name="myOutput")
    def my_output(self) -> 'outputs.MyOutputType':
        return pulumi.get(self, "my_output")

    @property
    @pulumi.getter(name="simpleOutput")
    def simple_output(self) -> str:
        return pulumi.get(self, "simple_output")


class AwaitableMyFunctionResult(MyFunctionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return MyFunctionResult(
            my_output=self.my_output,
            simple_output=self.simple_output)


def my_function(my_type: Optional[Union['MyType', 'MyTypeDict']] = None,
                simple_prop: Optional[str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableMyFunctionResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['myType'] = my_type
    __args__['simpleProp'] = simple_prop
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('typedDictExample:index:MyFunction', __args__, opts=opts, typ=MyFunctionResult).value

    return AwaitableMyFunctionResult(
        my_output=pulumi.get(__ret__, 'my_output'),
        simple_output=pulumi.get(__ret__, 'simple_output'))
def my_function_output(my_type: Optional[pulumi.Input[Union['MyType', 'MyTypeDict']]] = None,
                       simple_prop: Optional[pulumi.Input[Optional[str]]] = None,
                       opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[MyFunctionResult]:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['myType'] = my_type
    __args__['simpleProp'] = simple_prop
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('typedDictExample:index:MyFunction', __args__, opts=opts, typ=MyFunctionResult)
    return __ret__.apply(lambda __response__: MyFunctionResult(
        my_output=pulumi.get(__response__, 'my_output'),
        simple_output=pulumi.get(__response__, 'simple_output')))
