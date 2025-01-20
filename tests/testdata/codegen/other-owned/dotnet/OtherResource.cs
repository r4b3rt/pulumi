// *** WARNING: this file was generated by test. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Other.Example
{
    [ExampleResourceType("example::OtherResource")]
    public partial class OtherResource : global::Pulumi.ComponentResource
    {
        [Output("foo")]
        public Output<Other.Example.Resource?> Foo { get; private set; } = null!;


        /// <summary>
        /// Create a OtherResource resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public OtherResource(string name, OtherResourceArgs? args = null, ComponentResourceOptions? options = null)
            : base("example::OtherResource", name, args ?? new OtherResourceArgs(), MakeResourceOptions(options, ""), remote: true)
        {
        }

        private static ComponentResourceOptions MakeResourceOptions(ComponentResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new ComponentResourceOptions
            {
                Version = Utilities.Version,
                PluginDownloadURL = "example.com/download",
            };
            var merged = ComponentResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
    }

    public sealed class OtherResourceArgs : global::Pulumi.ResourceArgs
    {
        [Input("foo")]
        public Input<Other.Example.Resource>? Foo { get; set; }

        public OtherResourceArgs()
        {
        }
        public static new OtherResourceArgs Empty => new OtherResourceArgs();
    }
}
