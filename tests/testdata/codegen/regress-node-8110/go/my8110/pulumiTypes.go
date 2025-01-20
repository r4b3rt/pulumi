// Code generated by test DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package my8110

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"regress-node-8110/my8110/internal"
)

var _ = internal.GetEnvOrDefault

type MyObj struct {
	A *string `pulumi:"a"`
}

// MyObjInput is an input type that accepts MyObjArgs and MyObjOutput values.
// You can construct a concrete instance of `MyObjInput` via:
//
//	MyObjArgs{...}
type MyObjInput interface {
	pulumi.Input

	ToMyObjOutput() MyObjOutput
	ToMyObjOutputWithContext(context.Context) MyObjOutput
}

type MyObjArgs struct {
	A pulumi.StringPtrInput `pulumi:"a"`
}

func (MyObjArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*MyObj)(nil)).Elem()
}

func (i MyObjArgs) ToMyObjOutput() MyObjOutput {
	return i.ToMyObjOutputWithContext(context.Background())
}

func (i MyObjArgs) ToMyObjOutputWithContext(ctx context.Context) MyObjOutput {
	return pulumi.ToOutputWithContext(ctx, i).(MyObjOutput)
}

type MyObjOutput struct{ *pulumi.OutputState }

func (MyObjOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*MyObj)(nil)).Elem()
}

func (o MyObjOutput) ToMyObjOutput() MyObjOutput {
	return o
}

func (o MyObjOutput) ToMyObjOutputWithContext(ctx context.Context) MyObjOutput {
	return o
}

func (o MyObjOutput) A() pulumi.StringPtrOutput {
	return o.ApplyT(func(v MyObj) *string { return v.A }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*MyObjInput)(nil)).Elem(), MyObjArgs{})
	pulumi.RegisterOutputType(MyObjOutput{})
}
