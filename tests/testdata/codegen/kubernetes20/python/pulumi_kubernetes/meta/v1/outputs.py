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
from . import outputs

__all__ = [
    'ListMeta',
    'ManagedFieldsEntry',
    'ObjectMeta',
    'OwnerReference',
]

@pulumi.output_type
class ListMeta(dict):
    """
    ListMeta describes metadata that synthetic resources must have, including lists and various status objects. A resource may have only one of {ObjectMeta, ListMeta}.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "continue":
            suggest = "continue_"
        elif key == "remainingItemCount":
            suggest = "remaining_item_count"
        elif key == "resourceVersion":
            suggest = "resource_version"
        elif key == "selfLink":
            suggest = "self_link"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ListMeta. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ListMeta.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ListMeta.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 continue_: Optional[str] = None,
                 remaining_item_count: Optional[int] = None,
                 resource_version: Optional[str] = None,
                 self_link: Optional[str] = None):
        """
        ListMeta describes metadata that synthetic resources must have, including lists and various status objects. A resource may have only one of {ObjectMeta, ListMeta}.
        :param str continue_: continue may be set if the user set a limit on the number of items returned, and indicates that the server has more data available. The value is opaque and may be used to issue another request to the endpoint that served this list to retrieve the next set of available objects. Continuing a consistent list may not be possible if the server configuration has changed or more than a few minutes have passed. The resourceVersion field returned when using this continue value will be identical to the value in the first response, unless you have received this token from an error message.
        :param int remaining_item_count: remainingItemCount is the number of subsequent items in the list which are not included in this list response. If the list request contained label or field selectors, then the number of remaining items is unknown and the field will be left unset and omitted during serialization. If the list is complete (either because it is not chunking or because this is the last chunk), then there are no more remaining items and this field will be left unset and omitted during serialization. Servers older than v1.15 do not set this field. The intended use of the remainingItemCount is *estimating* the size of a collection. Clients should not rely on the remainingItemCount to be set or to be exact.
        :param str resource_version: String that identifies the server's internal version of this object that can be used by clients to determine when objects have changed. Value must be treated as opaque by clients and passed unmodified back to the server. Populated by the system. Read-only. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency
        :param str self_link: Deprecated: selfLink is a legacy read-only field that is no longer populated by the system.
        """
        if continue_ is not None:
            pulumi.set(__self__, "continue_", continue_)
        if remaining_item_count is not None:
            pulumi.set(__self__, "remaining_item_count", remaining_item_count)
        if resource_version is not None:
            pulumi.set(__self__, "resource_version", resource_version)
        if self_link is not None:
            pulumi.set(__self__, "self_link", self_link)

    @property
    @pulumi.getter(name="continue")
    def continue_(self) -> Optional[str]:
        """
        continue may be set if the user set a limit on the number of items returned, and indicates that the server has more data available. The value is opaque and may be used to issue another request to the endpoint that served this list to retrieve the next set of available objects. Continuing a consistent list may not be possible if the server configuration has changed or more than a few minutes have passed. The resourceVersion field returned when using this continue value will be identical to the value in the first response, unless you have received this token from an error message.
        """
        return pulumi.get(self, "continue_")

    @property
    @pulumi.getter(name="remainingItemCount")
    def remaining_item_count(self) -> Optional[int]:
        """
        remainingItemCount is the number of subsequent items in the list which are not included in this list response. If the list request contained label or field selectors, then the number of remaining items is unknown and the field will be left unset and omitted during serialization. If the list is complete (either because it is not chunking or because this is the last chunk), then there are no more remaining items and this field will be left unset and omitted during serialization. Servers older than v1.15 do not set this field. The intended use of the remainingItemCount is *estimating* the size of a collection. Clients should not rely on the remainingItemCount to be set or to be exact.
        """
        return pulumi.get(self, "remaining_item_count")

    @property
    @pulumi.getter(name="resourceVersion")
    def resource_version(self) -> Optional[str]:
        """
        String that identifies the server's internal version of this object that can be used by clients to determine when objects have changed. Value must be treated as opaque by clients and passed unmodified back to the server. Populated by the system. Read-only. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency
        """
        return pulumi.get(self, "resource_version")

    @property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> Optional[str]:
        """
        Deprecated: selfLink is a legacy read-only field that is no longer populated by the system.
        """
        return pulumi.get(self, "self_link")


@pulumi.output_type
class ManagedFieldsEntry(dict):
    """
    ManagedFieldsEntry is a workflow-id, a FieldSet and the group version of the resource that the fieldset applies to.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "apiVersion":
            suggest = "api_version"
        elif key == "fieldsType":
            suggest = "fields_type"
        elif key == "fieldsV1":
            suggest = "fields_v1"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ManagedFieldsEntry. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ManagedFieldsEntry.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ManagedFieldsEntry.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 api_version: Optional[str] = None,
                 fields_type: Optional[str] = None,
                 fields_v1: Optional[Any] = None,
                 manager: Optional[str] = None,
                 operation: Optional[str] = None,
                 subresource: Optional[str] = None,
                 time: Optional[str] = None):
        """
        ManagedFieldsEntry is a workflow-id, a FieldSet and the group version of the resource that the fieldset applies to.
        :param str api_version: APIVersion defines the version of this resource that this field set applies to. The format is "group/version" just like the top-level APIVersion field. It is necessary to track the version of a field set because it cannot be automatically converted.
        :param str fields_type: FieldsType is the discriminator for the different fields format and version. There is currently only one possible value: "FieldsV1"
        :param Any fields_v1: FieldsV1 holds the first JSON version format as described in the "FieldsV1" type.
        :param str manager: Manager is an identifier of the workflow managing these fields.
        :param str operation: Operation is the type of operation which lead to this ManagedFieldsEntry being created. The only valid values for this field are 'Apply' and 'Update'.
        :param str subresource: Subresource is the name of the subresource used to update that object, or empty string if the object was updated through the main resource. The value of this field is used to distinguish between managers, even if they share the same name. For example, a status update will be distinct from a regular update using the same manager name. Note that the APIVersion field is not related to the Subresource field and it always corresponds to the version of the main resource.
        :param str time: Time is the timestamp of when the ManagedFields entry was added. The timestamp will also be updated if a field is added, the manager changes any of the owned fields value or removes a field. The timestamp does not update when a field is removed from the entry because another manager took it over.
        """
        if api_version is not None:
            pulumi.set(__self__, "api_version", api_version)
        if fields_type is not None:
            pulumi.set(__self__, "fields_type", fields_type)
        if fields_v1 is not None:
            pulumi.set(__self__, "fields_v1", fields_v1)
        if manager is not None:
            pulumi.set(__self__, "manager", manager)
        if operation is not None:
            pulumi.set(__self__, "operation", operation)
        if subresource is not None:
            pulumi.set(__self__, "subresource", subresource)
        if time is not None:
            pulumi.set(__self__, "time", time)

    @property
    @pulumi.getter(name="apiVersion")
    def api_version(self) -> Optional[str]:
        """
        APIVersion defines the version of this resource that this field set applies to. The format is "group/version" just like the top-level APIVersion field. It is necessary to track the version of a field set because it cannot be automatically converted.
        """
        return pulumi.get(self, "api_version")

    @property
    @pulumi.getter(name="fieldsType")
    def fields_type(self) -> Optional[str]:
        """
        FieldsType is the discriminator for the different fields format and version. There is currently only one possible value: "FieldsV1"
        """
        return pulumi.get(self, "fields_type")

    @property
    @pulumi.getter(name="fieldsV1")
    def fields_v1(self) -> Optional[Any]:
        """
        FieldsV1 holds the first JSON version format as described in the "FieldsV1" type.
        """
        return pulumi.get(self, "fields_v1")

    @property
    @pulumi.getter
    def manager(self) -> Optional[str]:
        """
        Manager is an identifier of the workflow managing these fields.
        """
        return pulumi.get(self, "manager")

    @property
    @pulumi.getter
    def operation(self) -> Optional[str]:
        """
        Operation is the type of operation which lead to this ManagedFieldsEntry being created. The only valid values for this field are 'Apply' and 'Update'.
        """
        return pulumi.get(self, "operation")

    @property
    @pulumi.getter
    def subresource(self) -> Optional[str]:
        """
        Subresource is the name of the subresource used to update that object, or empty string if the object was updated through the main resource. The value of this field is used to distinguish between managers, even if they share the same name. For example, a status update will be distinct from a regular update using the same manager name. Note that the APIVersion field is not related to the Subresource field and it always corresponds to the version of the main resource.
        """
        return pulumi.get(self, "subresource")

    @property
    @pulumi.getter
    def time(self) -> Optional[str]:
        """
        Time is the timestamp of when the ManagedFields entry was added. The timestamp will also be updated if a field is added, the manager changes any of the owned fields value or removes a field. The timestamp does not update when a field is removed from the entry because another manager took it over.
        """
        return pulumi.get(self, "time")


@pulumi.output_type
class ObjectMeta(dict):
    """
    ObjectMeta is metadata that all persisted resources must have, which includes all objects users must create.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "clusterName":
            suggest = "cluster_name"
        elif key == "creationTimestamp":
            suggest = "creation_timestamp"
        elif key == "deletionGracePeriodSeconds":
            suggest = "deletion_grace_period_seconds"
        elif key == "deletionTimestamp":
            suggest = "deletion_timestamp"
        elif key == "generateName":
            suggest = "generate_name"
        elif key == "managedFields":
            suggest = "managed_fields"
        elif key == "ownerReferences":
            suggest = "owner_references"
        elif key == "resourceVersion":
            suggest = "resource_version"
        elif key == "selfLink":
            suggest = "self_link"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ObjectMeta. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ObjectMeta.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ObjectMeta.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 annotations: Optional[Mapping[str, str]] = None,
                 cluster_name: Optional[str] = None,
                 creation_timestamp: Optional[str] = None,
                 deletion_grace_period_seconds: Optional[int] = None,
                 deletion_timestamp: Optional[str] = None,
                 finalizers: Optional[Sequence[str]] = None,
                 generate_name: Optional[str] = None,
                 generation: Optional[int] = None,
                 labels: Optional[Mapping[str, str]] = None,
                 managed_fields: Optional[Sequence['outputs.ManagedFieldsEntry']] = None,
                 name: Optional[str] = None,
                 namespace: Optional[str] = None,
                 owner_references: Optional[Sequence['outputs.OwnerReference']] = None,
                 resource_version: Optional[str] = None,
                 self_link: Optional[str] = None,
                 uid: Optional[str] = None):
        """
        ObjectMeta is metadata that all persisted resources must have, which includes all objects users must create.
        :param Mapping[str, str] annotations: Annotations is an unstructured key value map stored with a resource that may be set by external tools to store and retrieve arbitrary metadata. They are not queryable and should be preserved when modifying objects. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations
        :param str cluster_name: The name of the cluster which the object belongs to. This is used to distinguish resources with same name and namespace in different clusters. This field is not set anywhere right now and apiserver is going to ignore it if set in create or update request.
        :param str creation_timestamp: CreationTimestamp is a timestamp representing the server time when this object was created. It is not guaranteed to be set in happens-before order across separate operations. Clients may not set this value. It is represented in RFC3339 form and is in UTC.
               
               Populated by the system. Read-only. Null for lists. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata
        :param int deletion_grace_period_seconds: Number of seconds allowed for this object to gracefully terminate before it will be removed from the system. Only set when deletionTimestamp is also set. May only be shortened. Read-only.
        :param str deletion_timestamp: DeletionTimestamp is RFC 3339 date and time at which this resource will be deleted. This field is set by the server when a graceful deletion is requested by the user, and is not directly settable by a client. The resource is expected to be deleted (no longer visible from resource lists, and not reachable by name) after the time in this field, once the finalizers list is empty. As long as the finalizers list contains items, deletion is blocked. Once the deletionTimestamp is set, this value may not be unset or be set further into the future, although it may be shortened or the resource may be deleted prior to this time. For example, a user may request that a pod is deleted in 30 seconds. The Kubelet will react by sending a graceful termination signal to the containers in the pod. After that 30 seconds, the Kubelet will send a hard termination signal (SIGKILL) to the container and after cleanup, remove the pod from the API. In the presence of network partitions, this object may still exist after this timestamp, until an administrator or automated process can determine the resource is fully terminated. If not set, graceful deletion of the object has not been requested.
               
               Populated by the system when a graceful deletion is requested. Read-only. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata
        :param Sequence[str] finalizers: Must be empty before the object is deleted from the registry. Each entry is an identifier for the responsible component that will remove the entry from the list. If the deletionTimestamp of the object is non-nil, entries in this list can only be removed. Finalizers may be processed and removed in any order.  Order is NOT enforced because it introduces significant risk of stuck finalizers. finalizers is a shared field, any actor with permission can reorder it. If the finalizer list is processed in order, then this can lead to a situation in which the component responsible for the first finalizer in the list is waiting for a signal (field value, external system, or other) produced by a component responsible for a finalizer later in the list, resulting in a deadlock. Without enforced ordering finalizers are free to order amongst themselves and are not vulnerable to ordering changes in the list.
        :param str generate_name: GenerateName is an optional prefix, used by the server, to generate a unique name ONLY IF the Name field has not been provided. If this field is used, the name returned to the client will be different than the name passed. This value will also be combined with a unique suffix. The provided value has the same validation rules as the Name field, and may be truncated by the length of the suffix required to make the value unique on the server.
               
               If this field is specified and the generated name exists, the server will return a 409.
               
               Applied only if Name is not specified. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#idempotency
        :param int generation: A sequence number representing a specific generation of the desired state. Populated by the system. Read-only.
        :param Mapping[str, str] labels: Map of string keys and values that can be used to organize and categorize (scope and select) objects. May match selectors of replication controllers and services. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels
        :param Sequence['ManagedFieldsEntryArgs'] managed_fields: ManagedFields maps workflow-id and version to the set of fields that are managed by that workflow. This is mostly for internal housekeeping, and users typically shouldn't need to set or understand this field. A workflow can be the user's name, a controller's name, or the name of a specific apply path like "ci-cd". The set of fields is always in the version that the workflow used when modifying the object.
        :param str name: Name must be unique within a namespace. Is required when creating resources, although some resources may allow a client to request the generation of an appropriate name automatically. Name is primarily intended for creation idempotence and configuration definition. Cannot be updated. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names#names
        :param str namespace: Namespace defines the space within which each name must be unique. An empty namespace is equivalent to the "default" namespace, but "default" is the canonical representation. Not all objects are required to be scoped to a namespace - the value of this field for those objects will be empty.
               
               Must be a DNS_LABEL. Cannot be updated. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces
        :param Sequence['OwnerReferenceArgs'] owner_references: List of objects depended by this object. If ALL objects in the list have been deleted, this object will be garbage collected. If this object is managed by a controller, then an entry in this list will point to this controller, with the controller field set to true. There cannot be more than one managing controller.
        :param str resource_version: An opaque value that represents the internal version of this object that can be used by clients to determine when objects have changed. May be used for optimistic concurrency, change detection, and the watch operation on a resource or set of resources. Clients must treat these values as opaque and passed unmodified back to the server. They may only be valid for a particular resource or set of resources.
               
               Populated by the system. Read-only. Value must be treated as opaque by clients and . More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency
        :param str self_link: Deprecated: selfLink is a legacy read-only field that is no longer populated by the system.
        :param str uid: UID is the unique in time and space value for this object. It is typically generated by the server on successful creation of a resource and is not allowed to change on PUT operations.
               
               Populated by the system. Read-only. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names#uids
        """
        if annotations is not None:
            pulumi.set(__self__, "annotations", annotations)
        if cluster_name is not None:
            pulumi.set(__self__, "cluster_name", cluster_name)
        if creation_timestamp is not None:
            pulumi.set(__self__, "creation_timestamp", creation_timestamp)
        if deletion_grace_period_seconds is not None:
            pulumi.set(__self__, "deletion_grace_period_seconds", deletion_grace_period_seconds)
        if deletion_timestamp is not None:
            pulumi.set(__self__, "deletion_timestamp", deletion_timestamp)
        if finalizers is not None:
            pulumi.set(__self__, "finalizers", finalizers)
        if generate_name is not None:
            pulumi.set(__self__, "generate_name", generate_name)
        if generation is not None:
            pulumi.set(__self__, "generation", generation)
        if labels is not None:
            pulumi.set(__self__, "labels", labels)
        if managed_fields is not None:
            pulumi.set(__self__, "managed_fields", managed_fields)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if namespace is not None:
            pulumi.set(__self__, "namespace", namespace)
        if owner_references is not None:
            pulumi.set(__self__, "owner_references", owner_references)
        if resource_version is not None:
            pulumi.set(__self__, "resource_version", resource_version)
        if self_link is not None:
            pulumi.set(__self__, "self_link", self_link)
        if uid is not None:
            pulumi.set(__self__, "uid", uid)

    @property
    @pulumi.getter
    def annotations(self) -> Optional[Mapping[str, str]]:
        """
        Annotations is an unstructured key value map stored with a resource that may be set by external tools to store and retrieve arbitrary metadata. They are not queryable and should be preserved when modifying objects. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations
        """
        return pulumi.get(self, "annotations")

    @property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> Optional[str]:
        """
        The name of the cluster which the object belongs to. This is used to distinguish resources with same name and namespace in different clusters. This field is not set anywhere right now and apiserver is going to ignore it if set in create or update request.
        """
        return pulumi.get(self, "cluster_name")

    @property
    @pulumi.getter(name="creationTimestamp")
    def creation_timestamp(self) -> Optional[str]:
        """
        CreationTimestamp is a timestamp representing the server time when this object was created. It is not guaranteed to be set in happens-before order across separate operations. Clients may not set this value. It is represented in RFC3339 form and is in UTC.

        Populated by the system. Read-only. Null for lists. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata
        """
        return pulumi.get(self, "creation_timestamp")

    @property
    @pulumi.getter(name="deletionGracePeriodSeconds")
    def deletion_grace_period_seconds(self) -> Optional[int]:
        """
        Number of seconds allowed for this object to gracefully terminate before it will be removed from the system. Only set when deletionTimestamp is also set. May only be shortened. Read-only.
        """
        return pulumi.get(self, "deletion_grace_period_seconds")

    @property
    @pulumi.getter(name="deletionTimestamp")
    def deletion_timestamp(self) -> Optional[str]:
        """
        DeletionTimestamp is RFC 3339 date and time at which this resource will be deleted. This field is set by the server when a graceful deletion is requested by the user, and is not directly settable by a client. The resource is expected to be deleted (no longer visible from resource lists, and not reachable by name) after the time in this field, once the finalizers list is empty. As long as the finalizers list contains items, deletion is blocked. Once the deletionTimestamp is set, this value may not be unset or be set further into the future, although it may be shortened or the resource may be deleted prior to this time. For example, a user may request that a pod is deleted in 30 seconds. The Kubelet will react by sending a graceful termination signal to the containers in the pod. After that 30 seconds, the Kubelet will send a hard termination signal (SIGKILL) to the container and after cleanup, remove the pod from the API. In the presence of network partitions, this object may still exist after this timestamp, until an administrator or automated process can determine the resource is fully terminated. If not set, graceful deletion of the object has not been requested.

        Populated by the system when a graceful deletion is requested. Read-only. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata
        """
        return pulumi.get(self, "deletion_timestamp")

    @property
    @pulumi.getter
    def finalizers(self) -> Optional[Sequence[str]]:
        """
        Must be empty before the object is deleted from the registry. Each entry is an identifier for the responsible component that will remove the entry from the list. If the deletionTimestamp of the object is non-nil, entries in this list can only be removed. Finalizers may be processed and removed in any order.  Order is NOT enforced because it introduces significant risk of stuck finalizers. finalizers is a shared field, any actor with permission can reorder it. If the finalizer list is processed in order, then this can lead to a situation in which the component responsible for the first finalizer in the list is waiting for a signal (field value, external system, or other) produced by a component responsible for a finalizer later in the list, resulting in a deadlock. Without enforced ordering finalizers are free to order amongst themselves and are not vulnerable to ordering changes in the list.
        """
        return pulumi.get(self, "finalizers")

    @property
    @pulumi.getter(name="generateName")
    def generate_name(self) -> Optional[str]:
        """
        GenerateName is an optional prefix, used by the server, to generate a unique name ONLY IF the Name field has not been provided. If this field is used, the name returned to the client will be different than the name passed. This value will also be combined with a unique suffix. The provided value has the same validation rules as the Name field, and may be truncated by the length of the suffix required to make the value unique on the server.

        If this field is specified and the generated name exists, the server will return a 409.

        Applied only if Name is not specified. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#idempotency
        """
        return pulumi.get(self, "generate_name")

    @property
    @pulumi.getter
    def generation(self) -> Optional[int]:
        """
        A sequence number representing a specific generation of the desired state. Populated by the system. Read-only.
        """
        return pulumi.get(self, "generation")

    @property
    @pulumi.getter
    def labels(self) -> Optional[Mapping[str, str]]:
        """
        Map of string keys and values that can be used to organize and categorize (scope and select) objects. May match selectors of replication controllers and services. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter(name="managedFields")
    def managed_fields(self) -> Optional[Sequence['outputs.ManagedFieldsEntry']]:
        """
        ManagedFields maps workflow-id and version to the set of fields that are managed by that workflow. This is mostly for internal housekeeping, and users typically shouldn't need to set or understand this field. A workflow can be the user's name, a controller's name, or the name of a specific apply path like "ci-cd". The set of fields is always in the version that the workflow used when modifying the object.
        """
        return pulumi.get(self, "managed_fields")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        Name must be unique within a namespace. Is required when creating resources, although some resources may allow a client to request the generation of an appropriate name automatically. Name is primarily intended for creation idempotence and configuration definition. Cannot be updated. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names#names
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def namespace(self) -> Optional[str]:
        """
        Namespace defines the space within which each name must be unique. An empty namespace is equivalent to the "default" namespace, but "default" is the canonical representation. Not all objects are required to be scoped to a namespace - the value of this field for those objects will be empty.

        Must be a DNS_LABEL. Cannot be updated. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces
        """
        return pulumi.get(self, "namespace")

    @property
    @pulumi.getter(name="ownerReferences")
    def owner_references(self) -> Optional[Sequence['outputs.OwnerReference']]:
        """
        List of objects depended by this object. If ALL objects in the list have been deleted, this object will be garbage collected. If this object is managed by a controller, then an entry in this list will point to this controller, with the controller field set to true. There cannot be more than one managing controller.
        """
        return pulumi.get(self, "owner_references")

    @property
    @pulumi.getter(name="resourceVersion")
    def resource_version(self) -> Optional[str]:
        """
        An opaque value that represents the internal version of this object that can be used by clients to determine when objects have changed. May be used for optimistic concurrency, change detection, and the watch operation on a resource or set of resources. Clients must treat these values as opaque and passed unmodified back to the server. They may only be valid for a particular resource or set of resources.

        Populated by the system. Read-only. Value must be treated as opaque by clients and . More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency
        """
        return pulumi.get(self, "resource_version")

    @property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> Optional[str]:
        """
        Deprecated: selfLink is a legacy read-only field that is no longer populated by the system.
        """
        return pulumi.get(self, "self_link")

    @property
    @pulumi.getter
    def uid(self) -> Optional[str]:
        """
        UID is the unique in time and space value for this object. It is typically generated by the server on successful creation of a resource and is not allowed to change on PUT operations.

        Populated by the system. Read-only. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names#uids
        """
        return pulumi.get(self, "uid")


@pulumi.output_type
class OwnerReference(dict):
    """
    OwnerReference contains enough information to let you identify an owning object. An owning object must be in the same namespace as the dependent, or be cluster-scoped, so there is no namespace field.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "apiVersion":
            suggest = "api_version"
        elif key == "blockOwnerDeletion":
            suggest = "block_owner_deletion"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in OwnerReference. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        OwnerReference.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        OwnerReference.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 api_version: str,
                 kind: str,
                 name: str,
                 uid: str,
                 block_owner_deletion: Optional[bool] = None,
                 controller: Optional[bool] = None):
        """
        OwnerReference contains enough information to let you identify an owning object. An owning object must be in the same namespace as the dependent, or be cluster-scoped, so there is no namespace field.
        :param str api_version: API version of the referent.
        :param str kind: Kind of the referent. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
        :param str name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names#names
        :param str uid: UID of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names#uids
        :param bool block_owner_deletion: If true, AND if the owner has the "foregroundDeletion" finalizer, then the owner cannot be deleted from the key-value store until this reference is removed. See https://kubernetes.io/docs/concepts/architecture/garbage-collection/#foreground-deletion for how the garbage collector interacts with this field and enforces the foreground deletion. Defaults to false. To set this field, a user needs "delete" permission of the owner, otherwise 422 (Unprocessable Entity) will be returned.
        :param bool controller: If true, this reference points to the managing controller.
        """
        pulumi.set(__self__, "api_version", api_version)
        pulumi.set(__self__, "kind", kind)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "uid", uid)
        if block_owner_deletion is not None:
            pulumi.set(__self__, "block_owner_deletion", block_owner_deletion)
        if controller is not None:
            pulumi.set(__self__, "controller", controller)

    @property
    @pulumi.getter(name="apiVersion")
    def api_version(self) -> str:
        """
        API version of the referent.
        """
        return pulumi.get(self, "api_version")

    @property
    @pulumi.getter
    def kind(self) -> str:
        """
        Kind of the referent. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names#names
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def uid(self) -> str:
        """
        UID of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names#uids
        """
        return pulumi.get(self, "uid")

    @property
    @pulumi.getter(name="blockOwnerDeletion")
    def block_owner_deletion(self) -> Optional[bool]:
        """
        If true, AND if the owner has the "foregroundDeletion" finalizer, then the owner cannot be deleted from the key-value store until this reference is removed. See https://kubernetes.io/docs/concepts/architecture/garbage-collection/#foreground-deletion for how the garbage collector interacts with this field and enforces the foreground deletion. Defaults to false. To set this field, a user needs "delete" permission of the owner, otherwise 422 (Unprocessable Entity) will be returned.
        """
        return pulumi.get(self, "block_owner_deletion")

    @property
    @pulumi.getter
    def controller(self) -> Optional[bool]:
        """
        If true, this reference points to the managing controller.
        """
        return pulumi.get(self, "controller")


