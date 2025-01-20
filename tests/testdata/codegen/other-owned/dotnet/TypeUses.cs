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
    [ExampleResourceType("example::TypeUses")]
    public partial class TypeUses : global::Pulumi.CustomResource
    {
        [Output("bar")]
        public Output<Outputs.SomeOtherObject?> Bar { get; private set; } = null!;

        [Output("baz")]
        public Output<Outputs.ObjectWithNodeOptionalInputs?> Baz { get; private set; } = null!;

        [Output("foo")]
        public Output<Outputs.Object?> Foo { get; private set; } = null!;


        /// <summary>
        /// Create a TypeUses resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public TypeUses(string name, TypeUsesArgs? args = null, CustomResourceOptions? options = null)
            : base("example::TypeUses", name, args ?? new TypeUsesArgs(), MakeResourceOptions(options, ""))
        {
        }

        private TypeUses(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("example::TypeUses", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                PluginDownloadURL = "example.com/download",
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing TypeUses resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static TypeUses Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new TypeUses(name, id, options);
        }
    }

    public sealed class TypeUsesArgs : global::Pulumi.ResourceArgs
    {
        [Input("bar")]
        public Input<Inputs.SomeOtherObjectArgs>? Bar { get; set; }

        [Input("baz")]
        public Input<Inputs.ObjectWithNodeOptionalInputsArgs>? Baz { get; set; }

        [Input("foo")]
        public Input<Inputs.ObjectArgs>? Foo { get; set; }

        public TypeUsesArgs()
        {
        }
        public static new TypeUsesArgs Empty => new TypeUsesArgs();
    }
}
