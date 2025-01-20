// Code generated by test DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package mypkg

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
	"secrets/mypkg/internal"
)

type Resource struct {
	pulumi.CustomResourceState

	Config      pulumix.GPtrOutput[Config, ConfigOutput]   `pulumi:"config"`
	ConfigArray pulumix.GArrayOutput[Config, ConfigOutput] `pulumi:"configArray"`
	ConfigMap   pulumix.GMapOutput[Config, ConfigOutput]   `pulumi:"configMap"`
	Foo         pulumix.Output[string]                     `pulumi:"foo"`
	FooArray    pulumix.ArrayOutput[string]                `pulumi:"fooArray"`
	FooMap      pulumix.MapOutput[string]                  `pulumi:"fooMap"`
}

// NewResource registers a new resource with the given unique name, arguments, and options.
func NewResource(ctx *pulumi.Context,
	name string, args *ResourceArgs, opts ...pulumi.ResourceOption) (*Resource, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Config == nil {
		return nil, errors.New("invalid value for required argument 'Config'")
	}
	if args.ConfigArray == nil {
		return nil, errors.New("invalid value for required argument 'ConfigArray'")
	}
	if args.ConfigMap == nil {
		return nil, errors.New("invalid value for required argument 'ConfigMap'")
	}
	if args.Foo == nil {
		return nil, errors.New("invalid value for required argument 'Foo'")
	}
	if args.FooArray == nil {
		return nil, errors.New("invalid value for required argument 'FooArray'")
	}
	if args.FooMap == nil {
		return nil, errors.New("invalid value for required argument 'FooMap'")
	}
	if args.Config != nil {
		untypedSecretValue := pulumi.ToSecret(args.Config.ToOutput(ctx.Context()).Untyped())
		args.Config = pulumix.MustConvertTyped[*ConfigArgs](untypedSecretValue)
	}
	if args.ConfigArray != nil {
		untypedSecretValue := pulumi.ToSecret(args.ConfigArray.ToOutput(ctx.Context()).Untyped())
		args.ConfigArray = pulumix.MustConvertTyped[[]*ConfigArgs](untypedSecretValue)
	}
	if args.ConfigMap != nil {
		untypedSecretValue := pulumi.ToSecret(args.ConfigMap.ToOutput(ctx.Context()).Untyped())
		args.ConfigMap = pulumix.MustConvertTyped[map[string]*ConfigArgs](untypedSecretValue)
	}
	if args.Foo != nil {
		untypedSecretValue := pulumi.ToSecret(args.Foo.ToOutput(ctx.Context()).Untyped())
		args.Foo = pulumix.MustConvertTyped[string](untypedSecretValue)
	}
	if args.FooArray != nil {
		untypedSecretValue := pulumi.ToSecret(args.FooArray.ToOutput(ctx.Context()).Untyped())
		args.FooArray = pulumix.MustConvertTyped[[]string](untypedSecretValue)
	}
	if args.FooMap != nil {
		untypedSecretValue := pulumi.ToSecret(args.FooMap.ToOutput(ctx.Context()).Untyped())
		args.FooMap = pulumix.MustConvertTyped[map[string]string](untypedSecretValue)
	}
	secrets := pulumi.AdditionalSecretOutputs([]string{
		"config",
		"configArray",
		"configMap",
		"foo",
		"fooArray",
		"fooMap",
	})
	opts = append(opts, secrets)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource Resource
	err := ctx.RegisterResource("mypkg::Resource", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetResource gets an existing Resource resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetResource(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ResourceState, opts ...pulumi.ResourceOption) (*Resource, error) {
	var resource Resource
	err := ctx.ReadResource("mypkg::Resource", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Resource resources.
type resourceState struct {
}

type ResourceState struct {
}

func (ResourceState) ElementType() reflect.Type {
	return reflect.TypeOf((*resourceState)(nil)).Elem()
}

type resourceArgs struct {
	Config      Config            `pulumi:"config"`
	ConfigArray []Config          `pulumi:"configArray"`
	ConfigMap   map[string]Config `pulumi:"configMap"`
	Foo         string            `pulumi:"foo"`
	FooArray    []string          `pulumi:"fooArray"`
	FooMap      map[string]string `pulumi:"fooMap"`
}

// The set of arguments for constructing a Resource resource.
type ResourceArgs struct {
	Config      pulumix.Input[*ConfigArgs]
	ConfigArray pulumix.Input[[]*ConfigArgs]
	ConfigMap   pulumix.Input[map[string]*ConfigArgs]
	Foo         pulumix.Input[string]
	FooArray    pulumix.Input[[]string]
	FooMap      pulumix.Input[map[string]string]
}

func (ResourceArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*resourceArgs)(nil)).Elem()
}

type ResourceOutput struct{ *pulumi.OutputState }

func (ResourceOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*Resource)(nil)).Elem()
}

func (o ResourceOutput) ToResourceOutput() ResourceOutput {
	return o
}

func (o ResourceOutput) ToResourceOutputWithContext(ctx context.Context) ResourceOutput {
	return o
}

func (o ResourceOutput) ToOutput(ctx context.Context) pulumix.Output[Resource] {
	return pulumix.Output[Resource]{
		OutputState: o.OutputState,
	}
}

func (o ResourceOutput) Config() pulumix.GPtrOutput[Config, ConfigOutput] {
	value := pulumix.Apply[Resource](o, func(v Resource) pulumix.GPtrOutput[Config, ConfigOutput] { return v.Config })
	unwrapped := pulumix.Flatten[*Config, pulumix.GPtrOutput[Config, ConfigOutput]](value)
	return pulumix.GPtrOutput[Config, ConfigOutput]{OutputState: unwrapped.OutputState}
}

func (o ResourceOutput) ConfigArray() pulumix.GArrayOutput[Config, ConfigOutput] {
	value := pulumix.Apply[Resource](o, func(v Resource) pulumix.GArrayOutput[Config, ConfigOutput] { return v.ConfigArray })
	unwrapped := pulumix.Flatten[[]Config, pulumix.GArrayOutput[Config, ConfigOutput]](value)
	return pulumix.GArrayOutput[Config, ConfigOutput]{OutputState: unwrapped.OutputState}
}

func (o ResourceOutput) ConfigMap() pulumix.GMapOutput[Config, ConfigOutput] {
	value := pulumix.Apply[Resource](o, func(v Resource) pulumix.GMapOutput[Config, ConfigOutput] { return v.ConfigMap })
	unwrapped := pulumix.Flatten[map[string]Config, pulumix.GMapOutput[Config, ConfigOutput]](value)
	return pulumix.GMapOutput[Config, ConfigOutput]{OutputState: unwrapped.OutputState}
}

func (o ResourceOutput) Foo() pulumix.Output[string] {
	value := pulumix.Apply[Resource](o, func(v Resource) pulumix.Output[string] { return v.Foo })
	return pulumix.Flatten[string, pulumix.Output[string]](value)
}

func (o ResourceOutput) FooArray() pulumix.ArrayOutput[string] {
	value := pulumix.Apply[Resource](o, func(v Resource) pulumix.ArrayOutput[string] { return v.FooArray })
	unwrapped := pulumix.Flatten[[]string, pulumix.ArrayOutput[string]](value)
	return pulumix.ArrayOutput[string]{OutputState: unwrapped.OutputState}
}

func (o ResourceOutput) FooMap() pulumix.MapOutput[string] {
	value := pulumix.Apply[Resource](o, func(v Resource) pulumix.MapOutput[string] { return v.FooMap })
	unwrapped := pulumix.Flatten[map[string]string, pulumix.MapOutput[string]](value)
	return pulumix.MapOutput[string]{OutputState: unwrapped.OutputState}
}

func init() {
	pulumi.RegisterOutputType(ResourceOutput{})
}
