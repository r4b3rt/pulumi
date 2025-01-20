// *** WARNING: this file was generated by test. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Urnid.Outputs
{

    /// <summary>
    /// It's fine to use urn and id in nested objects
    /// </summary>
    [OutputType]
    public sealed class InnerType
    {
        public readonly string? Id;
        public readonly string? Urn;

        [OutputConstructor]
        private InnerType(
            string? id,

            string? urn)
        {
            Id = id;
            Urn = urn;
        }
    }
}
