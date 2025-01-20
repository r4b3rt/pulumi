// Code generated by test DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package mypkg

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
	"output-funcs/mypkg/internal"
)

// The response from the ListKeys operation.
// API Version: 2021-02-01.
func ListStorageAccountKeys(ctx *pulumi.Context, args *ListStorageAccountKeysArgs, opts ...pulumi.InvokeOption) (*ListStorageAccountKeysResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv ListStorageAccountKeysResult
	err := ctx.Invoke("mypkg::listStorageAccountKeys", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type ListStorageAccountKeysArgs struct {
	// The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
	AccountName string `pulumi:"accountName"`
	// Specifies type of the key to be listed. Possible value is kerb.
	Expand *string `pulumi:"expand"`
	// The name of the resource group within the user's subscription. The name is case insensitive.
	ResourceGroupName string `pulumi:"resourceGroupName"`
}

// The response from the ListKeys operation.
type ListStorageAccountKeysResult struct {
	// Gets the list of storage account keys and their properties for the specified storage account.
	Keys []StorageAccountKeyResponse `pulumi:"keys"`
}

func ListStorageAccountKeysOutput(ctx *pulumi.Context, args ListStorageAccountKeysOutputArgs, opts ...pulumi.InvokeOption) ListStorageAccountKeysResultOutput {
	outputResult := pulumix.ApplyErr[*ListStorageAccountKeysArgs](args.ToOutput(), func(plainArgs *ListStorageAccountKeysArgs) (*ListStorageAccountKeysResult, error) {
		return ListStorageAccountKeys(ctx, plainArgs, opts...)
	})

	return pulumix.Cast[ListStorageAccountKeysResultOutput, *ListStorageAccountKeysResult](outputResult)
}

type ListStorageAccountKeysOutputArgs struct {
	// The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
	AccountName pulumix.Input[string] `pulumi:"accountName"`
	// Specifies type of the key to be listed. Possible value is kerb.
	Expand pulumix.Input[*string] `pulumi:"expand"`
	// The name of the resource group within the user's subscription. The name is case insensitive.
	ResourceGroupName pulumix.Input[string] `pulumi:"resourceGroupName"`
}

func (args ListStorageAccountKeysOutputArgs) ToOutput() pulumix.Output[*ListStorageAccountKeysArgs] {
	allArgs := pulumix.All(
		args.AccountName.ToOutput(context.Background()).AsAny(),
		args.Expand.ToOutput(context.Background()).AsAny(),
		args.ResourceGroupName.ToOutput(context.Background()).AsAny())
	return pulumix.Apply[[]any](allArgs, func(resolvedArgs []interface{}) *ListStorageAccountKeysArgs {
		return &ListStorageAccountKeysArgs{
			AccountName:       resolvedArgs[0].(string),
			Expand:            resolvedArgs[1].(*string),
			ResourceGroupName: resolvedArgs[2].(string),
		}
	})
}

type ListStorageAccountKeysResultOutput struct{ *pulumi.OutputState }

func (ListStorageAccountKeysResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*ListStorageAccountKeysResult)(nil)).Elem()
}

func (o ListStorageAccountKeysResultOutput) ToOutput(context.Context) pulumix.Output[*ListStorageAccountKeysResult] {
	return pulumix.Output[*ListStorageAccountKeysResult]{
		OutputState: o.OutputState,
	}
}

func (o ListStorageAccountKeysResultOutput) Keys() pulumix.GArrayOutput[StorageAccountKeyResponse, StorageAccountKeyResponseOutput] {
	value := pulumix.Apply[*ListStorageAccountKeysResult](o, func(v *ListStorageAccountKeysResult) []StorageAccountKeyResponse { return v.Keys })
	return pulumix.GArrayOutput[StorageAccountKeyResponse, StorageAccountKeyResponseOutput]{
		OutputState: value.OutputState,
	}
}
