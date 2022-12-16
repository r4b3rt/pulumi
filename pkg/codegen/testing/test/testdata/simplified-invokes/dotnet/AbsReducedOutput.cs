// *** WARNING: this file was generated by test. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Std
{
    public static class AbsReducedOutput
    {
        /// <summary>
        /// Returns the absolute value of a given float. 
        /// Example: abs(1) returns 1, and abs(-1) would also return 1, whereas abs(-3.14) would return 3.14.
        /// </summary>
        public static Task<double> InvokeAsync(AbsReducedOutputArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeSingleAsync<double>("std:index:AbsReducedOutput", args ?? new AbsReducedOutputArgs(), options.WithDefaults());

        /// <summary>
        /// Returns the absolute value of a given float. 
        /// Example: abs(1) returns 1, and abs(-1) would also return 1, whereas abs(-3.14) would return 3.14.
        /// </summary>
        public static Output<double> Invoke(AbsReducedOutputInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeSingle<double>("std:index:AbsReducedOutput", args ?? new AbsReducedOutputInvokeArgs(), options.WithDefaults());
    }


    public sealed class AbsReducedOutputArgs : global::Pulumi.InvokeArgs
    {
        [Input("a", required: true)]
        public double A { get; set; }

        [Input("b")]
        public double? B { get; set; }

        public AbsReducedOutputArgs()
        {
        }
        public static new AbsReducedOutputArgs Empty => new AbsReducedOutputArgs();
    }

    public sealed class AbsReducedOutputInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("a", required: true)]
        public Input<double> A { get; set; } = null!;

        [Input("b")]
        public Input<double>? B { get; set; }

        public AbsReducedOutputInvokeArgs()
        {
        }
        public static new AbsReducedOutputInvokeArgs Empty => new AbsReducedOutputInvokeArgs();
    }
}