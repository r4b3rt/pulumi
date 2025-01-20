// *** WARNING: this file was generated by test. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Myedgeorder
{
    public static class ListConfigurations
    {
        /// <summary>
        /// The list of configurations.
        /// API Version: 2020-12-01-preview.
        /// </summary>
        public static Task<ListConfigurationsResult> InvokeAsync(ListConfigurationsArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<ListConfigurationsResult>("myedgeorder::listConfigurations", args ?? new ListConfigurationsArgs(), options.WithDefaults());

        /// <summary>
        /// The list of configurations.
        /// API Version: 2020-12-01-preview.
        /// </summary>
        public static Output<ListConfigurationsResult> Invoke(ListConfigurationsInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<ListConfigurationsResult>("myedgeorder::listConfigurations", args ?? new ListConfigurationsInvokeArgs(), options.WithDefaults());

        /// <summary>
        /// The list of configurations.
        /// API Version: 2020-12-01-preview.
        /// </summary>
        public static Output<ListConfigurationsResult> Invoke(ListConfigurationsInvokeArgs args, InvokeOutputOptions options)
            => global::Pulumi.Deployment.Instance.Invoke<ListConfigurationsResult>("myedgeorder::listConfigurations", args ?? new ListConfigurationsInvokeArgs(), options.WithDefaults());
    }


    public sealed class ListConfigurationsArgs : global::Pulumi.InvokeArgs
    {
        [Input("configurationFilters", required: true)]
        private List<Inputs.ConfigurationFilters>? _configurationFilters;

        /// <summary>
        /// Holds details about product hierarchy information and filterable property.
        /// </summary>
        public List<Inputs.ConfigurationFilters> ConfigurationFilters
        {
            get => _configurationFilters ?? (_configurationFilters = new List<Inputs.ConfigurationFilters>());
            set => _configurationFilters = value;
        }

        /// <summary>
        /// Customer subscription properties. Clients can display available products to unregistered customers by explicitly passing subscription details
        /// </summary>
        [Input("customerSubscriptionDetails")]
        public Inputs.CustomerSubscriptionDetails? CustomerSubscriptionDetails { get; set; }

        /// <summary>
        /// $skipToken is supported on list of configurations, which provides the next page in the list of configurations.
        /// </summary>
        [Input("skipToken")]
        public string? SkipToken { get; set; }

        public ListConfigurationsArgs()
        {
        }
        public static new ListConfigurationsArgs Empty => new ListConfigurationsArgs();
    }

    public sealed class ListConfigurationsInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("configurationFilters", required: true)]
        private InputList<Inputs.ConfigurationFiltersArgs>? _configurationFilters;

        /// <summary>
        /// Holds details about product hierarchy information and filterable property.
        /// </summary>
        public InputList<Inputs.ConfigurationFiltersArgs> ConfigurationFilters
        {
            get => _configurationFilters ?? (_configurationFilters = new InputList<Inputs.ConfigurationFiltersArgs>());
            set => _configurationFilters = value;
        }

        /// <summary>
        /// Customer subscription properties. Clients can display available products to unregistered customers by explicitly passing subscription details
        /// </summary>
        [Input("customerSubscriptionDetails")]
        public Input<Inputs.CustomerSubscriptionDetailsArgs>? CustomerSubscriptionDetails { get; set; }

        /// <summary>
        /// $skipToken is supported on list of configurations, which provides the next page in the list of configurations.
        /// </summary>
        [Input("skipToken")]
        public Input<string>? SkipToken { get; set; }

        public ListConfigurationsInvokeArgs()
        {
        }
        public static new ListConfigurationsInvokeArgs Empty => new ListConfigurationsInvokeArgs();
    }


    [OutputType]
    public sealed class ListConfigurationsResult
    {
        /// <summary>
        /// Link for the next set of configurations.
        /// </summary>
        public readonly string? NextLink;
        /// <summary>
        /// List of configurations.
        /// </summary>
        public readonly ImmutableArray<Outputs.ConfigurationResponse> Value;

        [OutputConstructor]
        private ListConfigurationsResult(
            string? nextLink,

            ImmutableArray<Outputs.ConfigurationResponse> value)
        {
            NextLink = nextLink;
            Value = value;
        }
    }
}
