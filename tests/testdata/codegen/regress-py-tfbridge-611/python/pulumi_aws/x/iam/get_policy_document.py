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
from ... import x as _x

__all__ = [
    'GetPolicyDocumentResult',
    'AwaitableGetPolicyDocumentResult',
    'get_policy_document',
    'get_policy_document_output',
]

@pulumi.output_type
class GetPolicyDocumentResult:
    def __init__(__self__, id=None, json=None, statements=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if json and not isinstance(json, str):
            raise TypeError("Expected argument 'json' to be a str")
        pulumi.set(__self__, "json", json)
        if statements and not isinstance(statements, list):
            raise TypeError("Expected argument 'statements' to be a list")
        pulumi.set(__self__, "statements", statements)

    @property
    @pulumi.getter
    def id(self) -> str:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def json(self) -> str:
        return pulumi.get(self, "json")

    @property
    @pulumi.getter
    def statements(self) -> Optional[Sequence['_x.outputs.GetPolicyDocumentStatementResult']]:
        return pulumi.get(self, "statements")


class AwaitableGetPolicyDocumentResult(GetPolicyDocumentResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPolicyDocumentResult(
            id=self.id,
            json=self.json,
            statements=self.statements)


def get_policy_document(statements: Optional[Sequence[Union['_x.GetPolicyDocumentStatementArgs', '_x.GetPolicyDocumentStatementArgsDict']]] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetPolicyDocumentResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['statements'] = statements
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws:x/iam/getPolicyDocument:getPolicyDocument', __args__, opts=opts, typ=GetPolicyDocumentResult).value

    return AwaitableGetPolicyDocumentResult(
        id=pulumi.get(__ret__, 'id'),
        json=pulumi.get(__ret__, 'json'),
        statements=pulumi.get(__ret__, 'statements'))
def get_policy_document_output(statements: Optional[pulumi.Input[Optional[Sequence[Union['_x.GetPolicyDocumentStatementArgs', '_x.GetPolicyDocumentStatementArgsDict']]]]] = None,
                               opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetPolicyDocumentResult]:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['statements'] = statements
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('aws:x/iam/getPolicyDocument:getPolicyDocument', __args__, opts=opts, typ=GetPolicyDocumentResult)
    return __ret__.apply(lambda __response__: GetPolicyDocumentResult(
        id=pulumi.get(__response__, 'id'),
        json=pulumi.get(__response__, 'json'),
        statements=pulumi.get(__response__, 'statements')))
