// Code generated by test DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package repro

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"go-nested-collections/repro/internal"
)

var _ = internal.GetEnvOrDefault

type Bar struct {
	Prop *string `pulumi:"prop"`
}

type BarOutput struct{ *pulumi.OutputState }

func (BarOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*Bar)(nil)).Elem()
}

func (o BarOutput) ToBarOutput() BarOutput {
	return o
}

func (o BarOutput) ToBarOutputWithContext(ctx context.Context) BarOutput {
	return o
}

func (o BarOutput) Prop() pulumi.StringPtrOutput {
	return o.ApplyT(func(v Bar) *string { return v.Prop }).(pulumi.StringPtrOutput)
}

type BarArrayOutput struct{ *pulumi.OutputState }

func (BarArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]Bar)(nil)).Elem()
}

func (o BarArrayOutput) ToBarArrayOutput() BarArrayOutput {
	return o
}

func (o BarArrayOutput) ToBarArrayOutputWithContext(ctx context.Context) BarArrayOutput {
	return o
}

func (o BarArrayOutput) Index(i pulumi.IntInput) BarOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) Bar {
		return vs[0].([]Bar)[vs[1].(int)]
	}).(BarOutput)
}

type BarArrayArrayOutput struct{ *pulumi.OutputState }

func (BarArrayArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[][]Bar)(nil)).Elem()
}

func (o BarArrayArrayOutput) ToBarArrayArrayOutput() BarArrayArrayOutput {
	return o
}

func (o BarArrayArrayOutput) ToBarArrayArrayOutputWithContext(ctx context.Context) BarArrayArrayOutput {
	return o
}

func (o BarArrayArrayOutput) Index(i pulumi.IntInput) BarArrayOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) []Bar {
		return vs[0].([][]Bar)[vs[1].(int)]
	}).(BarArrayOutput)
}

type BarArrayArrayArrayOutput struct{ *pulumi.OutputState }

func (BarArrayArrayArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[][][]Bar)(nil)).Elem()
}

func (o BarArrayArrayArrayOutput) ToBarArrayArrayArrayOutput() BarArrayArrayArrayOutput {
	return o
}

func (o BarArrayArrayArrayOutput) ToBarArrayArrayArrayOutputWithContext(ctx context.Context) BarArrayArrayArrayOutput {
	return o
}

func (o BarArrayArrayArrayOutput) Index(i pulumi.IntInput) BarArrayArrayOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) [][]Bar {
		return vs[0].([][][]Bar)[vs[1].(int)]
	}).(BarArrayArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(BarOutput{})
	pulumi.RegisterOutputType(BarArrayOutput{})
	pulumi.RegisterOutputType(BarArrayArrayOutput{})
	pulumi.RegisterOutputType(BarArrayArrayArrayOutput{})
}
