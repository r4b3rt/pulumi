// *** WARNING: this file was generated by test. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * Codegen demo with const inputs
 */
export function funcWithConstInput(args?: FuncWithConstInputArgs, opts?: pulumi.InvokeOptions): Promise<void> {
    args = args || {};
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("mypkg::funcWithConstInput", {
        "plainInput": args.plainInput,
    }, opts);
}

export interface FuncWithConstInputArgs {
    plainInput?: "fixed";
}
