# coding=utf-8
# *** WARNING: this file was generated by test. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from . import _utilities
import typing
# Export this package's modules as members:
from ._enums import *
from .func_with_all_optional_inputs import *
from .provider import *
from . import outputs

# Make subpackages available:
if typing.TYPE_CHECKING:
    import pulumi_configstation.config as __config
    config = __config
else:
    config = _utilities.lazy_import('pulumi_configstation.config')

_utilities.register(
    resource_modules="""
[]
""",
    resource_packages="""
[
 {
  "pkg": "configstation",
  "token": "pulumi:providers:configstation",
  "fqn": "pulumi_configstation",
  "class": "Provider"
 }
]
"""
)
