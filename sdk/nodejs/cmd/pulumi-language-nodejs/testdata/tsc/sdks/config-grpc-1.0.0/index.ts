// *** WARNING: this file was generated by pulumi-language-nodejs. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

// Export members:
export { ConfigFetcherArgs } from "./configFetcher";
export type ConfigFetcher = import("./configFetcher").ConfigFetcher;
export const ConfigFetcher: typeof import("./configFetcher").ConfigFetcher = null as any;
utilities.lazyLoad(exports, ["ConfigFetcher"], () => require("./configFetcher"));

export { ProviderArgs } from "./provider";
export type Provider = import("./provider").Provider;
export const Provider: typeof import("./provider").Provider = null as any;
utilities.lazyLoad(exports, ["Provider"], () => require("./provider"));

export { ToSecretArgs, ToSecretResult, ToSecretOutputArgs } from "./toSecret";
export const toSecret: typeof import("./toSecret").toSecret = null as any;
export const toSecretOutput: typeof import("./toSecret").toSecretOutput = null as any;
utilities.lazyLoad(exports, ["toSecret","toSecretOutput"], () => require("./toSecret"));


// Export sub-modules:
import * as config from "./config";
import * as types from "./types";

export {
    config,
    types,
};

const _module = {
    version: utilities.getVersion(),
    construct: (name: string, type: string, urn: string): pulumi.Resource => {
        switch (type) {
            case "config-grpc:index:ConfigFetcher":
                return new ConfigFetcher(name, <any>undefined, { urn })
            default:
                throw new Error(`unknown resource type ${type}`);
        }
    },
};
pulumi.runtime.registerResourceModule("config-grpc", "index", _module)
pulumi.runtime.registerResourcePackage("config-grpc", {
    version: utilities.getVersion(),
    constructProvider: (name: string, type: string, urn: string): pulumi.ProviderResource => {
        if (type !== "pulumi:providers:config-grpc") {
            throw new Error(`unknown provider type ${type}`);
        }
        return new Provider(name, <any>undefined, { urn });
    },
});
