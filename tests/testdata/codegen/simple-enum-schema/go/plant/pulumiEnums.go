// Code generated by test DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package plant

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// The log_name to populate in the Cloud Audit Record. This is added to regress pulumi/pulumi issue #7913
type CloudAuditOptionsLogName string

const (
	// Default. Should not be used.
	CloudAuditOptionsLogNameUnspecifiedLogName = CloudAuditOptionsLogName("UNSPECIFIED_LOG_NAME")
	// Corresponds to "cloudaudit.googleapis.com/activity"
	CloudAuditOptionsLogNameAdminActivity = CloudAuditOptionsLogName("ADMIN_ACTIVITY")
	// Corresponds to "cloudaudit.googleapis.com/data_access"
	CloudAuditOptionsLogNameDataAccess = CloudAuditOptionsLogName("DATA_ACCESS")
	// What if triple quotes """ are used in the description
	CloudAuditOptionsLogNameSynthetic = CloudAuditOptionsLogName("SYNTHETIC")
	CloudAuditOptionsLogName_NO_NAME  = CloudAuditOptionsLogName("_NO_NAME")
)

func (CloudAuditOptionsLogName) ElementType() reflect.Type {
	return reflect.TypeOf((*CloudAuditOptionsLogName)(nil)).Elem()
}

func (e CloudAuditOptionsLogName) ToCloudAuditOptionsLogNameOutput() CloudAuditOptionsLogNameOutput {
	return pulumi.ToOutput(e).(CloudAuditOptionsLogNameOutput)
}

func (e CloudAuditOptionsLogName) ToCloudAuditOptionsLogNameOutputWithContext(ctx context.Context) CloudAuditOptionsLogNameOutput {
	return pulumi.ToOutputWithContext(ctx, e).(CloudAuditOptionsLogNameOutput)
}

func (e CloudAuditOptionsLogName) ToCloudAuditOptionsLogNamePtrOutput() CloudAuditOptionsLogNamePtrOutput {
	return e.ToCloudAuditOptionsLogNamePtrOutputWithContext(context.Background())
}

func (e CloudAuditOptionsLogName) ToCloudAuditOptionsLogNamePtrOutputWithContext(ctx context.Context) CloudAuditOptionsLogNamePtrOutput {
	return CloudAuditOptionsLogName(e).ToCloudAuditOptionsLogNameOutputWithContext(ctx).ToCloudAuditOptionsLogNamePtrOutputWithContext(ctx)
}

func (e CloudAuditOptionsLogName) ToStringOutput() pulumi.StringOutput {
	return pulumi.ToOutput(pulumi.String(e)).(pulumi.StringOutput)
}

func (e CloudAuditOptionsLogName) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return pulumi.ToOutputWithContext(ctx, pulumi.String(e)).(pulumi.StringOutput)
}

func (e CloudAuditOptionsLogName) ToStringPtrOutput() pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringPtrOutputWithContext(context.Background())
}

func (e CloudAuditOptionsLogName) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringOutputWithContext(ctx).ToStringPtrOutputWithContext(ctx)
}

type CloudAuditOptionsLogNameOutput struct{ *pulumi.OutputState }

func (CloudAuditOptionsLogNameOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*CloudAuditOptionsLogName)(nil)).Elem()
}

func (o CloudAuditOptionsLogNameOutput) ToCloudAuditOptionsLogNameOutput() CloudAuditOptionsLogNameOutput {
	return o
}

func (o CloudAuditOptionsLogNameOutput) ToCloudAuditOptionsLogNameOutputWithContext(ctx context.Context) CloudAuditOptionsLogNameOutput {
	return o
}

func (o CloudAuditOptionsLogNameOutput) ToCloudAuditOptionsLogNamePtrOutput() CloudAuditOptionsLogNamePtrOutput {
	return o.ToCloudAuditOptionsLogNamePtrOutputWithContext(context.Background())
}

func (o CloudAuditOptionsLogNameOutput) ToCloudAuditOptionsLogNamePtrOutputWithContext(ctx context.Context) CloudAuditOptionsLogNamePtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, v CloudAuditOptionsLogName) *CloudAuditOptionsLogName {
		return &v
	}).(CloudAuditOptionsLogNamePtrOutput)
}

func (o CloudAuditOptionsLogNameOutput) ToOutput(ctx context.Context) pulumix.Output[CloudAuditOptionsLogName] {
	return pulumix.Output[CloudAuditOptionsLogName]{
		OutputState: o.OutputState,
	}
}

func (o CloudAuditOptionsLogNameOutput) ToStringOutput() pulumi.StringOutput {
	return o.ToStringOutputWithContext(context.Background())
}

func (o CloudAuditOptionsLogNameOutput) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e CloudAuditOptionsLogName) string {
		return string(e)
	}).(pulumi.StringOutput)
}

func (o CloudAuditOptionsLogNameOutput) ToStringPtrOutput() pulumi.StringPtrOutput {
	return o.ToStringPtrOutputWithContext(context.Background())
}

func (o CloudAuditOptionsLogNameOutput) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e CloudAuditOptionsLogName) *string {
		v := string(e)
		return &v
	}).(pulumi.StringPtrOutput)
}

type CloudAuditOptionsLogNamePtrOutput struct{ *pulumi.OutputState }

func (CloudAuditOptionsLogNamePtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**CloudAuditOptionsLogName)(nil)).Elem()
}

func (o CloudAuditOptionsLogNamePtrOutput) ToCloudAuditOptionsLogNamePtrOutput() CloudAuditOptionsLogNamePtrOutput {
	return o
}

func (o CloudAuditOptionsLogNamePtrOutput) ToCloudAuditOptionsLogNamePtrOutputWithContext(ctx context.Context) CloudAuditOptionsLogNamePtrOutput {
	return o
}

func (o CloudAuditOptionsLogNamePtrOutput) ToOutput(ctx context.Context) pulumix.Output[*CloudAuditOptionsLogName] {
	return pulumix.Output[*CloudAuditOptionsLogName]{
		OutputState: o.OutputState,
	}
}

func (o CloudAuditOptionsLogNamePtrOutput) Elem() CloudAuditOptionsLogNameOutput {
	return o.ApplyT(func(v *CloudAuditOptionsLogName) CloudAuditOptionsLogName {
		if v != nil {
			return *v
		}
		var ret CloudAuditOptionsLogName
		return ret
	}).(CloudAuditOptionsLogNameOutput)
}

func (o CloudAuditOptionsLogNamePtrOutput) ToStringPtrOutput() pulumi.StringPtrOutput {
	return o.ToStringPtrOutputWithContext(context.Background())
}

func (o CloudAuditOptionsLogNamePtrOutput) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e *CloudAuditOptionsLogName) *string {
		if e == nil {
			return nil
		}
		v := string(*e)
		return &v
	}).(pulumi.StringPtrOutput)
}

// CloudAuditOptionsLogNameInput is an input type that accepts values of the CloudAuditOptionsLogName enum
// A concrete instance of `CloudAuditOptionsLogNameInput` can be one of the following:
//
//	CloudAuditOptionsLogNameUnspecifiedLogName
//	CloudAuditOptionsLogNameAdminActivity
//	CloudAuditOptionsLogNameDataAccess
//	CloudAuditOptionsLogNameSynthetic
//	CloudAuditOptionsLogName_NO_NAME
type CloudAuditOptionsLogNameInput interface {
	pulumi.Input

	ToCloudAuditOptionsLogNameOutput() CloudAuditOptionsLogNameOutput
	ToCloudAuditOptionsLogNameOutputWithContext(context.Context) CloudAuditOptionsLogNameOutput
}

var cloudAuditOptionsLogNamePtrType = reflect.TypeOf((**CloudAuditOptionsLogName)(nil)).Elem()

type CloudAuditOptionsLogNamePtrInput interface {
	pulumi.Input

	ToCloudAuditOptionsLogNamePtrOutput() CloudAuditOptionsLogNamePtrOutput
	ToCloudAuditOptionsLogNamePtrOutputWithContext(context.Context) CloudAuditOptionsLogNamePtrOutput
}

type cloudAuditOptionsLogNamePtr string

func CloudAuditOptionsLogNamePtr(v string) CloudAuditOptionsLogNamePtrInput {
	return (*cloudAuditOptionsLogNamePtr)(&v)
}

func (*cloudAuditOptionsLogNamePtr) ElementType() reflect.Type {
	return cloudAuditOptionsLogNamePtrType
}

func (in *cloudAuditOptionsLogNamePtr) ToCloudAuditOptionsLogNamePtrOutput() CloudAuditOptionsLogNamePtrOutput {
	return pulumi.ToOutput(in).(CloudAuditOptionsLogNamePtrOutput)
}

func (in *cloudAuditOptionsLogNamePtr) ToCloudAuditOptionsLogNamePtrOutputWithContext(ctx context.Context) CloudAuditOptionsLogNamePtrOutput {
	return pulumi.ToOutputWithContext(ctx, in).(CloudAuditOptionsLogNamePtrOutput)
}

func (in *cloudAuditOptionsLogNamePtr) ToOutput(ctx context.Context) pulumix.Output[*CloudAuditOptionsLogName] {
	return pulumix.Output[*CloudAuditOptionsLogName]{
		OutputState: in.ToCloudAuditOptionsLogNamePtrOutputWithContext(ctx).OutputState,
	}
}

type ContainerBrightness float64

const (
	ContainerBrightnessZeroPointOne = ContainerBrightness(0.1)
	ContainerBrightnessOne          = ContainerBrightness(1)
)

func (ContainerBrightness) ElementType() reflect.Type {
	return reflect.TypeOf((*ContainerBrightness)(nil)).Elem()
}

func (e ContainerBrightness) ToContainerBrightnessOutput() ContainerBrightnessOutput {
	return pulumi.ToOutput(e).(ContainerBrightnessOutput)
}

func (e ContainerBrightness) ToContainerBrightnessOutputWithContext(ctx context.Context) ContainerBrightnessOutput {
	return pulumi.ToOutputWithContext(ctx, e).(ContainerBrightnessOutput)
}

func (e ContainerBrightness) ToContainerBrightnessPtrOutput() ContainerBrightnessPtrOutput {
	return e.ToContainerBrightnessPtrOutputWithContext(context.Background())
}

func (e ContainerBrightness) ToContainerBrightnessPtrOutputWithContext(ctx context.Context) ContainerBrightnessPtrOutput {
	return ContainerBrightness(e).ToContainerBrightnessOutputWithContext(ctx).ToContainerBrightnessPtrOutputWithContext(ctx)
}

func (e ContainerBrightness) ToFloat64Output() pulumi.Float64Output {
	return pulumi.ToOutput(pulumi.Float64(e)).(pulumi.Float64Output)
}

func (e ContainerBrightness) ToFloat64OutputWithContext(ctx context.Context) pulumi.Float64Output {
	return pulumi.ToOutputWithContext(ctx, pulumi.Float64(e)).(pulumi.Float64Output)
}

func (e ContainerBrightness) ToFloat64PtrOutput() pulumi.Float64PtrOutput {
	return pulumi.Float64(e).ToFloat64PtrOutputWithContext(context.Background())
}

func (e ContainerBrightness) ToFloat64PtrOutputWithContext(ctx context.Context) pulumi.Float64PtrOutput {
	return pulumi.Float64(e).ToFloat64OutputWithContext(ctx).ToFloat64PtrOutputWithContext(ctx)
}

type ContainerBrightnessOutput struct{ *pulumi.OutputState }

func (ContainerBrightnessOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*ContainerBrightness)(nil)).Elem()
}

func (o ContainerBrightnessOutput) ToContainerBrightnessOutput() ContainerBrightnessOutput {
	return o
}

func (o ContainerBrightnessOutput) ToContainerBrightnessOutputWithContext(ctx context.Context) ContainerBrightnessOutput {
	return o
}

func (o ContainerBrightnessOutput) ToContainerBrightnessPtrOutput() ContainerBrightnessPtrOutput {
	return o.ToContainerBrightnessPtrOutputWithContext(context.Background())
}

func (o ContainerBrightnessOutput) ToContainerBrightnessPtrOutputWithContext(ctx context.Context) ContainerBrightnessPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, v ContainerBrightness) *ContainerBrightness {
		return &v
	}).(ContainerBrightnessPtrOutput)
}

func (o ContainerBrightnessOutput) ToOutput(ctx context.Context) pulumix.Output[ContainerBrightness] {
	return pulumix.Output[ContainerBrightness]{
		OutputState: o.OutputState,
	}
}

func (o ContainerBrightnessOutput) ToFloat64Output() pulumi.Float64Output {
	return o.ToFloat64OutputWithContext(context.Background())
}

func (o ContainerBrightnessOutput) ToFloat64OutputWithContext(ctx context.Context) pulumi.Float64Output {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e ContainerBrightness) float64 {
		return float64(e)
	}).(pulumi.Float64Output)
}

func (o ContainerBrightnessOutput) ToFloat64PtrOutput() pulumi.Float64PtrOutput {
	return o.ToFloat64PtrOutputWithContext(context.Background())
}

func (o ContainerBrightnessOutput) ToFloat64PtrOutputWithContext(ctx context.Context) pulumi.Float64PtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e ContainerBrightness) *float64 {
		v := float64(e)
		return &v
	}).(pulumi.Float64PtrOutput)
}

type ContainerBrightnessPtrOutput struct{ *pulumi.OutputState }

func (ContainerBrightnessPtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**ContainerBrightness)(nil)).Elem()
}

func (o ContainerBrightnessPtrOutput) ToContainerBrightnessPtrOutput() ContainerBrightnessPtrOutput {
	return o
}

func (o ContainerBrightnessPtrOutput) ToContainerBrightnessPtrOutputWithContext(ctx context.Context) ContainerBrightnessPtrOutput {
	return o
}

func (o ContainerBrightnessPtrOutput) ToOutput(ctx context.Context) pulumix.Output[*ContainerBrightness] {
	return pulumix.Output[*ContainerBrightness]{
		OutputState: o.OutputState,
	}
}

func (o ContainerBrightnessPtrOutput) Elem() ContainerBrightnessOutput {
	return o.ApplyT(func(v *ContainerBrightness) ContainerBrightness {
		if v != nil {
			return *v
		}
		var ret ContainerBrightness
		return ret
	}).(ContainerBrightnessOutput)
}

func (o ContainerBrightnessPtrOutput) ToFloat64PtrOutput() pulumi.Float64PtrOutput {
	return o.ToFloat64PtrOutputWithContext(context.Background())
}

func (o ContainerBrightnessPtrOutput) ToFloat64PtrOutputWithContext(ctx context.Context) pulumi.Float64PtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e *ContainerBrightness) *float64 {
		if e == nil {
			return nil
		}
		v := float64(*e)
		return &v
	}).(pulumi.Float64PtrOutput)
}

// ContainerBrightnessInput is an input type that accepts values of the ContainerBrightness enum
// A concrete instance of `ContainerBrightnessInput` can be one of the following:
//
//	ContainerBrightnessZeroPointOne
//	ContainerBrightnessOne
type ContainerBrightnessInput interface {
	pulumi.Input

	ToContainerBrightnessOutput() ContainerBrightnessOutput
	ToContainerBrightnessOutputWithContext(context.Context) ContainerBrightnessOutput
}

var containerBrightnessPtrType = reflect.TypeOf((**ContainerBrightness)(nil)).Elem()

type ContainerBrightnessPtrInput interface {
	pulumi.Input

	ToContainerBrightnessPtrOutput() ContainerBrightnessPtrOutput
	ToContainerBrightnessPtrOutputWithContext(context.Context) ContainerBrightnessPtrOutput
}

type containerBrightnessPtr float64

func ContainerBrightnessPtr(v float64) ContainerBrightnessPtrInput {
	return (*containerBrightnessPtr)(&v)
}

func (*containerBrightnessPtr) ElementType() reflect.Type {
	return containerBrightnessPtrType
}

func (in *containerBrightnessPtr) ToContainerBrightnessPtrOutput() ContainerBrightnessPtrOutput {
	return pulumi.ToOutput(in).(ContainerBrightnessPtrOutput)
}

func (in *containerBrightnessPtr) ToContainerBrightnessPtrOutputWithContext(ctx context.Context) ContainerBrightnessPtrOutput {
	return pulumi.ToOutputWithContext(ctx, in).(ContainerBrightnessPtrOutput)
}

func (in *containerBrightnessPtr) ToOutput(ctx context.Context) pulumix.Output[*ContainerBrightness] {
	return pulumix.Output[*ContainerBrightness]{
		OutputState: in.ToContainerBrightnessPtrOutputWithContext(ctx).OutputState,
	}
}

// plant container colors
type ContainerColor string

const (
	ContainerColorRed    = ContainerColor("red")
	ContainerColorBlue   = ContainerColor("blue")
	ContainerColorYellow = ContainerColor("yellow")
)

func (ContainerColor) ElementType() reflect.Type {
	return reflect.TypeOf((*ContainerColor)(nil)).Elem()
}

func (e ContainerColor) ToContainerColorOutput() ContainerColorOutput {
	return pulumi.ToOutput(e).(ContainerColorOutput)
}

func (e ContainerColor) ToContainerColorOutputWithContext(ctx context.Context) ContainerColorOutput {
	return pulumi.ToOutputWithContext(ctx, e).(ContainerColorOutput)
}

func (e ContainerColor) ToContainerColorPtrOutput() ContainerColorPtrOutput {
	return e.ToContainerColorPtrOutputWithContext(context.Background())
}

func (e ContainerColor) ToContainerColorPtrOutputWithContext(ctx context.Context) ContainerColorPtrOutput {
	return ContainerColor(e).ToContainerColorOutputWithContext(ctx).ToContainerColorPtrOutputWithContext(ctx)
}

func (e ContainerColor) ToStringOutput() pulumi.StringOutput {
	return pulumi.ToOutput(pulumi.String(e)).(pulumi.StringOutput)
}

func (e ContainerColor) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return pulumi.ToOutputWithContext(ctx, pulumi.String(e)).(pulumi.StringOutput)
}

func (e ContainerColor) ToStringPtrOutput() pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringPtrOutputWithContext(context.Background())
}

func (e ContainerColor) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringOutputWithContext(ctx).ToStringPtrOutputWithContext(ctx)
}

type ContainerColorOutput struct{ *pulumi.OutputState }

func (ContainerColorOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*ContainerColor)(nil)).Elem()
}

func (o ContainerColorOutput) ToContainerColorOutput() ContainerColorOutput {
	return o
}

func (o ContainerColorOutput) ToContainerColorOutputWithContext(ctx context.Context) ContainerColorOutput {
	return o
}

func (o ContainerColorOutput) ToContainerColorPtrOutput() ContainerColorPtrOutput {
	return o.ToContainerColorPtrOutputWithContext(context.Background())
}

func (o ContainerColorOutput) ToContainerColorPtrOutputWithContext(ctx context.Context) ContainerColorPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, v ContainerColor) *ContainerColor {
		return &v
	}).(ContainerColorPtrOutput)
}

func (o ContainerColorOutput) ToOutput(ctx context.Context) pulumix.Output[ContainerColor] {
	return pulumix.Output[ContainerColor]{
		OutputState: o.OutputState,
	}
}

func (o ContainerColorOutput) ToStringOutput() pulumi.StringOutput {
	return o.ToStringOutputWithContext(context.Background())
}

func (o ContainerColorOutput) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e ContainerColor) string {
		return string(e)
	}).(pulumi.StringOutput)
}

func (o ContainerColorOutput) ToStringPtrOutput() pulumi.StringPtrOutput {
	return o.ToStringPtrOutputWithContext(context.Background())
}

func (o ContainerColorOutput) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e ContainerColor) *string {
		v := string(e)
		return &v
	}).(pulumi.StringPtrOutput)
}

type ContainerColorPtrOutput struct{ *pulumi.OutputState }

func (ContainerColorPtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**ContainerColor)(nil)).Elem()
}

func (o ContainerColorPtrOutput) ToContainerColorPtrOutput() ContainerColorPtrOutput {
	return o
}

func (o ContainerColorPtrOutput) ToContainerColorPtrOutputWithContext(ctx context.Context) ContainerColorPtrOutput {
	return o
}

func (o ContainerColorPtrOutput) ToOutput(ctx context.Context) pulumix.Output[*ContainerColor] {
	return pulumix.Output[*ContainerColor]{
		OutputState: o.OutputState,
	}
}

func (o ContainerColorPtrOutput) Elem() ContainerColorOutput {
	return o.ApplyT(func(v *ContainerColor) ContainerColor {
		if v != nil {
			return *v
		}
		var ret ContainerColor
		return ret
	}).(ContainerColorOutput)
}

func (o ContainerColorPtrOutput) ToStringPtrOutput() pulumi.StringPtrOutput {
	return o.ToStringPtrOutputWithContext(context.Background())
}

func (o ContainerColorPtrOutput) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e *ContainerColor) *string {
		if e == nil {
			return nil
		}
		v := string(*e)
		return &v
	}).(pulumi.StringPtrOutput)
}

// ContainerColorInput is an input type that accepts values of the ContainerColor enum
// A concrete instance of `ContainerColorInput` can be one of the following:
//
//	ContainerColorRed
//	ContainerColorBlue
//	ContainerColorYellow
type ContainerColorInput interface {
	pulumi.Input

	ToContainerColorOutput() ContainerColorOutput
	ToContainerColorOutputWithContext(context.Context) ContainerColorOutput
}

var containerColorPtrType = reflect.TypeOf((**ContainerColor)(nil)).Elem()

type ContainerColorPtrInput interface {
	pulumi.Input

	ToContainerColorPtrOutput() ContainerColorPtrOutput
	ToContainerColorPtrOutputWithContext(context.Context) ContainerColorPtrOutput
}

type containerColorPtr string

func ContainerColorPtr(v string) ContainerColorPtrInput {
	return (*containerColorPtr)(&v)
}

func (*containerColorPtr) ElementType() reflect.Type {
	return containerColorPtrType
}

func (in *containerColorPtr) ToContainerColorPtrOutput() ContainerColorPtrOutput {
	return pulumi.ToOutput(in).(ContainerColorPtrOutput)
}

func (in *containerColorPtr) ToContainerColorPtrOutputWithContext(ctx context.Context) ContainerColorPtrOutput {
	return pulumi.ToOutputWithContext(ctx, in).(ContainerColorPtrOutput)
}

func (in *containerColorPtr) ToOutput(ctx context.Context) pulumix.Output[*ContainerColor] {
	return pulumix.Output[*ContainerColor]{
		OutputState: in.ToContainerColorPtrOutputWithContext(ctx).OutputState,
	}
}

// plant container sizes
type ContainerSize int

const (
	ContainerSizeFourInch = ContainerSize(4)
	ContainerSizeSixInch  = ContainerSize(6)
	// Deprecated: Eight inch pots are no longer supported.
	ContainerSizeEightInch = ContainerSize(8)
)

func (ContainerSize) ElementType() reflect.Type {
	return reflect.TypeOf((*ContainerSize)(nil)).Elem()
}

func (e ContainerSize) ToContainerSizeOutput() ContainerSizeOutput {
	return pulumi.ToOutput(e).(ContainerSizeOutput)
}

func (e ContainerSize) ToContainerSizeOutputWithContext(ctx context.Context) ContainerSizeOutput {
	return pulumi.ToOutputWithContext(ctx, e).(ContainerSizeOutput)
}

func (e ContainerSize) ToContainerSizePtrOutput() ContainerSizePtrOutput {
	return e.ToContainerSizePtrOutputWithContext(context.Background())
}

func (e ContainerSize) ToContainerSizePtrOutputWithContext(ctx context.Context) ContainerSizePtrOutput {
	return ContainerSize(e).ToContainerSizeOutputWithContext(ctx).ToContainerSizePtrOutputWithContext(ctx)
}

func (e ContainerSize) ToIntOutput() pulumi.IntOutput {
	return pulumi.ToOutput(pulumi.Int(e)).(pulumi.IntOutput)
}

func (e ContainerSize) ToIntOutputWithContext(ctx context.Context) pulumi.IntOutput {
	return pulumi.ToOutputWithContext(ctx, pulumi.Int(e)).(pulumi.IntOutput)
}

func (e ContainerSize) ToIntPtrOutput() pulumi.IntPtrOutput {
	return pulumi.Int(e).ToIntPtrOutputWithContext(context.Background())
}

func (e ContainerSize) ToIntPtrOutputWithContext(ctx context.Context) pulumi.IntPtrOutput {
	return pulumi.Int(e).ToIntOutputWithContext(ctx).ToIntPtrOutputWithContext(ctx)
}

type ContainerSizeOutput struct{ *pulumi.OutputState }

func (ContainerSizeOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*ContainerSize)(nil)).Elem()
}

func (o ContainerSizeOutput) ToContainerSizeOutput() ContainerSizeOutput {
	return o
}

func (o ContainerSizeOutput) ToContainerSizeOutputWithContext(ctx context.Context) ContainerSizeOutput {
	return o
}

func (o ContainerSizeOutput) ToContainerSizePtrOutput() ContainerSizePtrOutput {
	return o.ToContainerSizePtrOutputWithContext(context.Background())
}

func (o ContainerSizeOutput) ToContainerSizePtrOutputWithContext(ctx context.Context) ContainerSizePtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, v ContainerSize) *ContainerSize {
		return &v
	}).(ContainerSizePtrOutput)
}

func (o ContainerSizeOutput) ToOutput(ctx context.Context) pulumix.Output[ContainerSize] {
	return pulumix.Output[ContainerSize]{
		OutputState: o.OutputState,
	}
}

func (o ContainerSizeOutput) ToIntOutput() pulumi.IntOutput {
	return o.ToIntOutputWithContext(context.Background())
}

func (o ContainerSizeOutput) ToIntOutputWithContext(ctx context.Context) pulumi.IntOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e ContainerSize) int {
		return int(e)
	}).(pulumi.IntOutput)
}

func (o ContainerSizeOutput) ToIntPtrOutput() pulumi.IntPtrOutput {
	return o.ToIntPtrOutputWithContext(context.Background())
}

func (o ContainerSizeOutput) ToIntPtrOutputWithContext(ctx context.Context) pulumi.IntPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e ContainerSize) *int {
		v := int(e)
		return &v
	}).(pulumi.IntPtrOutput)
}

type ContainerSizePtrOutput struct{ *pulumi.OutputState }

func (ContainerSizePtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**ContainerSize)(nil)).Elem()
}

func (o ContainerSizePtrOutput) ToContainerSizePtrOutput() ContainerSizePtrOutput {
	return o
}

func (o ContainerSizePtrOutput) ToContainerSizePtrOutputWithContext(ctx context.Context) ContainerSizePtrOutput {
	return o
}

func (o ContainerSizePtrOutput) ToOutput(ctx context.Context) pulumix.Output[*ContainerSize] {
	return pulumix.Output[*ContainerSize]{
		OutputState: o.OutputState,
	}
}

func (o ContainerSizePtrOutput) Elem() ContainerSizeOutput {
	return o.ApplyT(func(v *ContainerSize) ContainerSize {
		if v != nil {
			return *v
		}
		var ret ContainerSize
		return ret
	}).(ContainerSizeOutput)
}

func (o ContainerSizePtrOutput) ToIntPtrOutput() pulumi.IntPtrOutput {
	return o.ToIntPtrOutputWithContext(context.Background())
}

func (o ContainerSizePtrOutput) ToIntPtrOutputWithContext(ctx context.Context) pulumi.IntPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e *ContainerSize) *int {
		if e == nil {
			return nil
		}
		v := int(*e)
		return &v
	}).(pulumi.IntPtrOutput)
}

// ContainerSizeInput is an input type that accepts values of the ContainerSize enum
// A concrete instance of `ContainerSizeInput` can be one of the following:
//
//	ContainerSizeFourInch
//	ContainerSizeSixInch
type ContainerSizeInput interface {
	pulumi.Input

	ToContainerSizeOutput() ContainerSizeOutput
	ToContainerSizeOutputWithContext(context.Context) ContainerSizeOutput
}

var containerSizePtrType = reflect.TypeOf((**ContainerSize)(nil)).Elem()

type ContainerSizePtrInput interface {
	pulumi.Input

	ToContainerSizePtrOutput() ContainerSizePtrOutput
	ToContainerSizePtrOutputWithContext(context.Context) ContainerSizePtrOutput
}

type containerSizePtr int

func ContainerSizePtr(v int) ContainerSizePtrInput {
	return (*containerSizePtr)(&v)
}

func (*containerSizePtr) ElementType() reflect.Type {
	return containerSizePtrType
}

func (in *containerSizePtr) ToContainerSizePtrOutput() ContainerSizePtrOutput {
	return pulumi.ToOutput(in).(ContainerSizePtrOutput)
}

func (in *containerSizePtr) ToContainerSizePtrOutputWithContext(ctx context.Context) ContainerSizePtrOutput {
	return pulumi.ToOutputWithContext(ctx, in).(ContainerSizePtrOutput)
}

func (in *containerSizePtr) ToOutput(ctx context.Context) pulumix.Output[*ContainerSize] {
	return pulumix.Output[*ContainerSize]{
		OutputState: in.ToContainerSizePtrOutputWithContext(ctx).OutputState,
	}
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*CloudAuditOptionsLogNameInput)(nil)).Elem(), CloudAuditOptionsLogName("UNSPECIFIED_LOG_NAME"))
	pulumi.RegisterInputType(reflect.TypeOf((*CloudAuditOptionsLogNamePtrInput)(nil)).Elem(), CloudAuditOptionsLogName("UNSPECIFIED_LOG_NAME"))
	pulumi.RegisterInputType(reflect.TypeOf((*ContainerBrightnessInput)(nil)).Elem(), ContainerBrightness(0.1))
	pulumi.RegisterInputType(reflect.TypeOf((*ContainerBrightnessPtrInput)(nil)).Elem(), ContainerBrightness(0.1))
	pulumi.RegisterInputType(reflect.TypeOf((*ContainerColorInput)(nil)).Elem(), ContainerColor("red"))
	pulumi.RegisterInputType(reflect.TypeOf((*ContainerColorPtrInput)(nil)).Elem(), ContainerColor("red"))
	pulumi.RegisterInputType(reflect.TypeOf((*ContainerSizeInput)(nil)).Elem(), ContainerSize(4))
	pulumi.RegisterInputType(reflect.TypeOf((*ContainerSizePtrInput)(nil)).Elem(), ContainerSize(4))
	pulumi.RegisterOutputType(CloudAuditOptionsLogNameOutput{})
	pulumi.RegisterOutputType(CloudAuditOptionsLogNamePtrOutput{})
	pulumi.RegisterOutputType(ContainerBrightnessOutput{})
	pulumi.RegisterOutputType(ContainerBrightnessPtrOutput{})
	pulumi.RegisterOutputType(ContainerColorOutput{})
	pulumi.RegisterOutputType(ContainerColorPtrOutput{})
	pulumi.RegisterOutputType(ContainerSizeOutput{})
	pulumi.RegisterOutputType(ContainerSizePtrOutput{})
}
