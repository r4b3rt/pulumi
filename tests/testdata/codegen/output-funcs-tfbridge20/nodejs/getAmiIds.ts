// *** WARNING: this file was generated by test. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

/**
 * Taken from pulumi-AWS to regress an issue
 */
/** @deprecated aws.getAmiIds has been deprecated in favor of aws.ec2.getAmiIds */
export function getAmiIds(args: GetAmiIdsArgs, opts?: pulumi.InvokeOptions): Promise<GetAmiIdsResult> {
    pulumi.log.warn("getAmiIds is deprecated: aws.getAmiIds has been deprecated in favor of aws.ec2.getAmiIds")
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("mypkg::getAmiIds", {
        "executableUsers": args.executableUsers,
        "filters": args.filters,
        "nameRegex": args.nameRegex,
        "owners": args.owners,
        "sortAscending": args.sortAscending,
    }, opts);
}

/**
 * A collection of arguments for invoking getAmiIds.
 */
export interface GetAmiIdsArgs {
    /**
     * Limit search to users with *explicit* launch
     * permission on  the image. Valid items are the numeric account ID or `self`.
     */
    executableUsers?: string[];
    /**
     * One or more name/value pairs to filter off of. There
     * are several valid keys, for a full reference, check out
     * [describe-images in the AWS CLI reference][1].
     */
    filters?: inputs.GetAmiIdsFilter[];
    /**
     * A regex string to apply to the AMI list returned
     * by AWS. This allows more advanced filtering not supported from the AWS API.
     * This filtering is done locally on what AWS returns, and could have a performance
     * impact if the result is large. It is recommended to combine this with other
     * options to narrow down the list AWS returns.
     */
    nameRegex?: string;
    /**
     * List of AMI owners to limit search. At least 1 value must be specified. Valid values: an AWS account ID, `self` (the current account), or an AWS owner alias (e.g. `amazon`, `aws-marketplace`, `microsoft`).
     */
    owners: string[];
    /**
     * Used to sort AMIs by creation time.
     */
    sortAscending?: boolean;
}

/**
 * A collection of values returned by getAmiIds.
 */
export interface GetAmiIdsResult {
    readonly executableUsers?: string[];
    readonly filters?: outputs.GetAmiIdsFilter[];
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    readonly ids: string[];
    readonly nameRegex?: string;
    readonly owners: string[];
    readonly sortAscending?: boolean;
}
/**
 * Taken from pulumi-AWS to regress an issue
 */
/** @deprecated aws.getAmiIds has been deprecated in favor of aws.ec2.getAmiIds */
export function getAmiIdsOutput(args: GetAmiIdsOutputArgs, opts?: pulumi.InvokeOutputOptions): pulumi.Output<GetAmiIdsResult> {
    pulumi.log.warn("getAmiIds is deprecated: aws.getAmiIds has been deprecated in favor of aws.ec2.getAmiIds")
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invokeOutput("mypkg::getAmiIds", {
        "executableUsers": args.executableUsers,
        "filters": args.filters,
        "nameRegex": args.nameRegex,
        "owners": args.owners,
        "sortAscending": args.sortAscending,
    }, opts);
}

/**
 * A collection of arguments for invoking getAmiIds.
 */
export interface GetAmiIdsOutputArgs {
    /**
     * Limit search to users with *explicit* launch
     * permission on  the image. Valid items are the numeric account ID or `self`.
     */
    executableUsers?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * One or more name/value pairs to filter off of. There
     * are several valid keys, for a full reference, check out
     * [describe-images in the AWS CLI reference][1].
     */
    filters?: pulumi.Input<pulumi.Input<inputs.GetAmiIdsFilterArgs>[]>;
    /**
     * A regex string to apply to the AMI list returned
     * by AWS. This allows more advanced filtering not supported from the AWS API.
     * This filtering is done locally on what AWS returns, and could have a performance
     * impact if the result is large. It is recommended to combine this with other
     * options to narrow down the list AWS returns.
     */
    nameRegex?: pulumi.Input<string>;
    /**
     * List of AMI owners to limit search. At least 1 value must be specified. Valid values: an AWS account ID, `self` (the current account), or an AWS owner alias (e.g. `amazon`, `aws-marketplace`, `microsoft`).
     */
    owners: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Used to sort AMIs by creation time.
     */
    sortAscending?: pulumi.Input<boolean>;
}
