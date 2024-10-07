// Code generated by pulumi-language-go DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package simpleinvoke

import (
	"context"
	"reflect"

	"example.com/pulumi-simple-invoke/sdk/go/v10/simpleinvoke/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func Unit(ctx *pulumi.Context, args *UnitArgs, opts ...pulumi.InvokeOption) (*UnitResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv UnitResult
	err := ctx.Invoke("simple-invoke:index:unit", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type UnitArgs struct {
}

type UnitResult struct {
	Result string `pulumi:"result"`
}

func UnitOutput(ctx *pulumi.Context, args UnitOutputArgs, opts ...pulumi.InvokeOption) UnitResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (UnitResultOutput, error) {
			args := v.(UnitArgs)
			opts = internal.PkgInvokeDefaultOpts(opts)
			var rv UnitResult
			secret, err := ctx.InvokePackageRaw("simple-invoke:index:unit", args, &rv, "", opts...)
			if err != nil {
				return UnitResultOutput{}, err
			}

			output := pulumi.ToOutput(rv).(UnitResultOutput)
			if secret {
				return pulumi.ToSecret(output).(UnitResultOutput), nil
			}
			return output, nil
		}).(UnitResultOutput)
}

type UnitOutputArgs struct {
}

func (UnitOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*UnitArgs)(nil)).Elem()
}

type UnitResultOutput struct{ *pulumi.OutputState }

func (UnitResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*UnitResult)(nil)).Elem()
}

func (o UnitResultOutput) ToUnitResultOutput() UnitResultOutput {
	return o
}

func (o UnitResultOutput) ToUnitResultOutputWithContext(ctx context.Context) UnitResultOutput {
	return o
}

func (o UnitResultOutput) Result() pulumi.StringOutput {
	return o.ApplyT(func(v UnitResult) string { return v.Result }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(UnitResultOutput{})
}