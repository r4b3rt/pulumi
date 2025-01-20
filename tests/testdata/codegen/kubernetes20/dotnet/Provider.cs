// *** WARNING: this file was generated by test. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Kubernetes
{
    /// <summary>
    /// The provider type for the kubernetes package.
    /// </summary>
    [KubernetesResourceType("pulumi:providers:kubernetes")]
    public partial class Provider : global::Pulumi.ProviderResource
    {
        /// <summary>
        /// Create a Provider resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Provider(string name, ProviderArgs? args = null, CustomResourceOptions? options = null)
            : base("kubernetes", name, args ?? new ProviderArgs(), MakeResourceOptions(options, ""))
        {
        }
        internal Provider(string name, ImmutableDictionary<string, object?> dictionary, CustomResourceOptions? options = null)
            : base("kubernetes", name, new DictionaryResourceArgs(dictionary), MakeResourceOptions(options, ""))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
    }

    public sealed class ProviderArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Options for tuning the Kubernetes client used by a Provider.
        /// </summary>
        [Input("kubeClientSettings", json: true)]
        public Input<Pulumi.Kubernetes.Types.Inputs.Provider.KubeClientSettingsArgs>? KubeClientSettings { get; set; }

        /// <summary>
        /// The contents of a kubeconfig file or the path to a kubeconfig file.
        /// </summary>
        [Input("kubeconfig")]
        public Input<string>? KubeConfig { get; set; }

        /// <summary>
        /// If present, the default namespace to use. This flag is ignored for cluster-scoped resources.
        /// 
        /// A namespace can be specified in multiple places, and the precedence is as follows:
        /// 1. `.metadata.namespace` set on the resource.
        /// 2. This `namespace` parameter.
        /// 3. `namespace` set for the active context in the kubeconfig.
        /// </summary>
        [Input("namespace")]
        public Input<string>? Namespace { get; set; }

        public ProviderArgs()
        {
            KubeConfig = Utilities.GetEnv("KUBECONFIG");
        }
        public static new ProviderArgs Empty => new ProviderArgs();
    }
}
