// *** WARNING: this file was generated by test. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Example.Inputs
{

    public sealed class ServerPropertiesForRestoreArgs : global::Pulumi.ResourceArgs
    {
        [Input("createMode", required: true)]
        public Input<string> CreateMode { get; set; } = null!;

        [Input("restorePointInTime", required: true)]
        public Input<string> RestorePointInTime { get; set; } = null!;

        public ServerPropertiesForRestoreArgs()
        {
        }
        public static new ServerPropertiesForRestoreArgs Empty => new ServerPropertiesForRestoreArgs();
    }
}
