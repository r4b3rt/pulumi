// *** WARNING: this file was generated by test. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

export function getCustomResult(a?: number, opts?: pulumi.InvokeOptions): Promise<outputs.CustomResult> {
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("std:index:GetCustomResult", {
        "a": a,
    }, opts);
}
export function getCustomResultOutput(a?: pulumi.Input<number | undefined>, opts?: pulumi.InvokeOptions): pulumi.Output<outputs.CustomResult> {
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invokeOutput("std:index:GetCustomResult", {
        "a": a,
    }, opts);
}
