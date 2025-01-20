// Code generated by test DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package example

import (
	"context"
	"reflect"

	"external-resource-schema/example/internal"
	"github.com/pulumi/pulumi-random/sdk/v4/go/random"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

var _ = internal.GetEnvOrDefault

type Pet struct {
	Age               *int                         `pulumi:"age"`
	Name              *random.RandomPet            `pulumi:"name"`
	NameArray         []*random.RandomPet          `pulumi:"nameArray"`
	NameMap           map[string]*random.RandomPet `pulumi:"nameMap"`
	RequiredName      *random.RandomPet            `pulumi:"requiredName"`
	RequiredNameArray []*random.RandomPet          `pulumi:"requiredNameArray"`
	RequiredNameMap   map[string]*random.RandomPet `pulumi:"requiredNameMap"`
}

// PetInput is an input type that accepts PetArgs and PetOutput values.
// You can construct a concrete instance of `PetInput` via:
//
//	PetArgs{...}
type PetInput interface {
	pulumi.Input

	ToPetOutput() PetOutput
	ToPetOutputWithContext(context.Context) PetOutput
}

type PetArgs struct {
	Age               pulumi.IntPtrInput         `pulumi:"age"`
	Name              random.RandomPetInput      `pulumi:"name"`
	NameArray         random.RandomPetArrayInput `pulumi:"nameArray"`
	NameMap           random.RandomPetMapInput   `pulumi:"nameMap"`
	RequiredName      random.RandomPetInput      `pulumi:"requiredName"`
	RequiredNameArray random.RandomPetArrayInput `pulumi:"requiredNameArray"`
	RequiredNameMap   random.RandomPetMapInput   `pulumi:"requiredNameMap"`
}

func (PetArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*Pet)(nil)).Elem()
}

func (i PetArgs) ToPetOutput() PetOutput {
	return i.ToPetOutputWithContext(context.Background())
}

func (i PetArgs) ToPetOutputWithContext(ctx context.Context) PetOutput {
	return pulumi.ToOutputWithContext(ctx, i).(PetOutput)
}

func (i PetArgs) ToPetPtrOutput() PetPtrOutput {
	return i.ToPetPtrOutputWithContext(context.Background())
}

func (i PetArgs) ToPetPtrOutputWithContext(ctx context.Context) PetPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(PetOutput).ToPetPtrOutputWithContext(ctx)
}

// PetPtrInput is an input type that accepts PetArgs, PetPtr and PetPtrOutput values.
// You can construct a concrete instance of `PetPtrInput` via:
//
//	        PetArgs{...}
//
//	or:
//
//	        nil
type PetPtrInput interface {
	pulumi.Input

	ToPetPtrOutput() PetPtrOutput
	ToPetPtrOutputWithContext(context.Context) PetPtrOutput
}

type petPtrType PetArgs

func PetPtr(v *PetArgs) PetPtrInput {
	return (*petPtrType)(v)
}

func (*petPtrType) ElementType() reflect.Type {
	return reflect.TypeOf((**Pet)(nil)).Elem()
}

func (i *petPtrType) ToPetPtrOutput() PetPtrOutput {
	return i.ToPetPtrOutputWithContext(context.Background())
}

func (i *petPtrType) ToPetPtrOutputWithContext(ctx context.Context) PetPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(PetPtrOutput)
}

type PetOutput struct{ *pulumi.OutputState }

func (PetOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*Pet)(nil)).Elem()
}

func (o PetOutput) ToPetOutput() PetOutput {
	return o
}

func (o PetOutput) ToPetOutputWithContext(ctx context.Context) PetOutput {
	return o
}

func (o PetOutput) ToPetPtrOutput() PetPtrOutput {
	return o.ToPetPtrOutputWithContext(context.Background())
}

func (o PetOutput) ToPetPtrOutputWithContext(ctx context.Context) PetPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, v Pet) *Pet {
		return &v
	}).(PetPtrOutput)
}

func (o PetOutput) Age() pulumi.IntPtrOutput {
	return o.ApplyT(func(v Pet) *int { return v.Age }).(pulumi.IntPtrOutput)
}

func (o PetOutput) Name() random.RandomPetOutput {
	return o.ApplyT(func(v Pet) *random.RandomPet { return v.Name }).(random.RandomPetOutput)
}

func (o PetOutput) NameArray() random.RandomPetArrayOutput {
	return o.ApplyT(func(v Pet) []*random.RandomPet { return v.NameArray }).(random.RandomPetArrayOutput)
}

func (o PetOutput) NameMap() random.RandomPetMapOutput {
	return o.ApplyT(func(v Pet) map[string]*random.RandomPet { return v.NameMap }).(random.RandomPetMapOutput)
}

func (o PetOutput) RequiredName() random.RandomPetOutput {
	return o.ApplyT(func(v Pet) *random.RandomPet { return v.RequiredName }).(random.RandomPetOutput)
}

func (o PetOutput) RequiredNameArray() random.RandomPetArrayOutput {
	return o.ApplyT(func(v Pet) []*random.RandomPet { return v.RequiredNameArray }).(random.RandomPetArrayOutput)
}

func (o PetOutput) RequiredNameMap() random.RandomPetMapOutput {
	return o.ApplyT(func(v Pet) map[string]*random.RandomPet { return v.RequiredNameMap }).(random.RandomPetMapOutput)
}

type PetPtrOutput struct{ *pulumi.OutputState }

func (PetPtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Pet)(nil)).Elem()
}

func (o PetPtrOutput) ToPetPtrOutput() PetPtrOutput {
	return o
}

func (o PetPtrOutput) ToPetPtrOutputWithContext(ctx context.Context) PetPtrOutput {
	return o
}

func (o PetPtrOutput) Elem() PetOutput {
	return o.ApplyT(func(v *Pet) Pet {
		if v != nil {
			return *v
		}
		var ret Pet
		return ret
	}).(PetOutput)
}

func (o PetPtrOutput) Age() pulumi.IntPtrOutput {
	return o.ApplyT(func(v *Pet) *int {
		if v == nil {
			return nil
		}
		return v.Age
	}).(pulumi.IntPtrOutput)
}

func (o PetPtrOutput) Name() random.RandomPetOutput {
	return o.ApplyT(func(v *Pet) *random.RandomPet {
		if v == nil {
			return nil
		}
		return v.Name
	}).(random.RandomPetOutput)
}

func (o PetPtrOutput) NameArray() random.RandomPetArrayOutput {
	return o.ApplyT(func(v *Pet) []*random.RandomPet {
		if v == nil {
			return nil
		}
		return v.NameArray
	}).(random.RandomPetArrayOutput)
}

func (o PetPtrOutput) NameMap() random.RandomPetMapOutput {
	return o.ApplyT(func(v *Pet) map[string]*random.RandomPet {
		if v == nil {
			return nil
		}
		return v.NameMap
	}).(random.RandomPetMapOutput)
}

func (o PetPtrOutput) RequiredName() random.RandomPetOutput {
	return o.ApplyT(func(v *Pet) *random.RandomPet {
		if v == nil {
			return nil
		}
		return v.RequiredName
	}).(random.RandomPetOutput)
}

func (o PetPtrOutput) RequiredNameArray() random.RandomPetArrayOutput {
	return o.ApplyT(func(v *Pet) []*random.RandomPet {
		if v == nil {
			return nil
		}
		return v.RequiredNameArray
	}).(random.RandomPetArrayOutput)
}

func (o PetPtrOutput) RequiredNameMap() random.RandomPetMapOutput {
	return o.ApplyT(func(v *Pet) map[string]*random.RandomPet {
		if v == nil {
			return nil
		}
		return v.RequiredNameMap
	}).(random.RandomPetMapOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*PetInput)(nil)).Elem(), PetArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*PetPtrInput)(nil)).Elem(), PetArgs{})
	pulumi.RegisterOutputType(PetOutput{})
	pulumi.RegisterOutputType(PetPtrOutput{})
}
