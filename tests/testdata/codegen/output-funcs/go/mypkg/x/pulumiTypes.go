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

var _ = internal.GetEnvOrDefault

// Bastion Shareable Link.
type BastionShareableLink struct {
	// Reference of the virtual machine resource.
	Vm string `pulumi:"vm"`
}

// Bastion Shareable Link.
type BastionShareableLinkArgs struct {
	// Reference of the virtual machine resource.
	Vm pulumix.Input[string] `pulumi:"vm"`
}

func (BastionShareableLinkArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*BastionShareableLink)(nil)).Elem()
}

func (i BastionShareableLinkArgs) ToBastionShareableLinkOutput() BastionShareableLinkOutput {
	return i.ToBastionShareableLinkOutputWithContext(context.Background())
}

func (i BastionShareableLinkArgs) ToBastionShareableLinkOutputWithContext(ctx context.Context) BastionShareableLinkOutput {
	return pulumi.ToOutputWithContext(ctx, i).(BastionShareableLinkOutput)
}

func (i *BastionShareableLinkArgs) ToOutput(ctx context.Context) pulumix.Output[*BastionShareableLinkArgs] {
	return pulumix.Val(i)
}

// Bastion Shareable Link.
type BastionShareableLinkOutput struct{ *pulumi.OutputState }

func (BastionShareableLinkOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*BastionShareableLink)(nil)).Elem()
}

func (o BastionShareableLinkOutput) ToBastionShareableLinkOutput() BastionShareableLinkOutput {
	return o
}

func (o BastionShareableLinkOutput) ToBastionShareableLinkOutputWithContext(ctx context.Context) BastionShareableLinkOutput {
	return o
}

func (o BastionShareableLinkOutput) ToOutput(ctx context.Context) pulumix.Output[BastionShareableLink] {
	return pulumix.Output[BastionShareableLink]{
		OutputState: o.OutputState,
	}
}

// Reference of the virtual machine resource.
func (o BastionShareableLinkOutput) Vm() pulumix.Output[string] {
	return pulumix.Apply[BastionShareableLink](o, func(v BastionShareableLink) string { return v.Vm })
}

// Ssis environment reference.
type SsisEnvironmentReferenceResponse struct {
	// Environment folder name.
	EnvironmentFolderName *string `pulumi:"environmentFolderName"`
	// Environment name.
	EnvironmentName *string `pulumi:"environmentName"`
	// Environment reference id.
	Id *float64 `pulumi:"id"`
	// Reference type
	ReferenceType *string `pulumi:"referenceType"`
}

// Ssis environment reference.
type SsisEnvironmentReferenceResponseArgs struct {
	// Environment folder name.
	EnvironmentFolderName pulumix.Input[*string] `pulumi:"environmentFolderName"`
	// Environment name.
	EnvironmentName pulumix.Input[*string] `pulumi:"environmentName"`
	// Environment reference id.
	Id pulumix.Input[*float64] `pulumi:"id"`
	// Reference type
	ReferenceType pulumix.Input[*string] `pulumi:"referenceType"`
}

func (SsisEnvironmentReferenceResponseArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*SsisEnvironmentReferenceResponse)(nil)).Elem()
}

func (i SsisEnvironmentReferenceResponseArgs) ToSsisEnvironmentReferenceResponseOutput() SsisEnvironmentReferenceResponseOutput {
	return i.ToSsisEnvironmentReferenceResponseOutputWithContext(context.Background())
}

func (i SsisEnvironmentReferenceResponseArgs) ToSsisEnvironmentReferenceResponseOutputWithContext(ctx context.Context) SsisEnvironmentReferenceResponseOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SsisEnvironmentReferenceResponseOutput)
}

func (i *SsisEnvironmentReferenceResponseArgs) ToOutput(ctx context.Context) pulumix.Output[*SsisEnvironmentReferenceResponseArgs] {
	return pulumix.Val(i)
}

// Ssis environment reference.
type SsisEnvironmentReferenceResponseOutput struct{ *pulumi.OutputState }

func (SsisEnvironmentReferenceResponseOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*SsisEnvironmentReferenceResponse)(nil)).Elem()
}

func (o SsisEnvironmentReferenceResponseOutput) ToSsisEnvironmentReferenceResponseOutput() SsisEnvironmentReferenceResponseOutput {
	return o
}

func (o SsisEnvironmentReferenceResponseOutput) ToSsisEnvironmentReferenceResponseOutputWithContext(ctx context.Context) SsisEnvironmentReferenceResponseOutput {
	return o
}

func (o SsisEnvironmentReferenceResponseOutput) ToOutput(ctx context.Context) pulumix.Output[SsisEnvironmentReferenceResponse] {
	return pulumix.Output[SsisEnvironmentReferenceResponse]{
		OutputState: o.OutputState,
	}
}

// Environment folder name.
func (o SsisEnvironmentReferenceResponseOutput) EnvironmentFolderName() pulumix.Output[*string] {
	return pulumix.Apply[SsisEnvironmentReferenceResponse](o, func(v SsisEnvironmentReferenceResponse) *string { return v.EnvironmentFolderName })
}

// Environment name.
func (o SsisEnvironmentReferenceResponseOutput) EnvironmentName() pulumix.Output[*string] {
	return pulumix.Apply[SsisEnvironmentReferenceResponse](o, func(v SsisEnvironmentReferenceResponse) *string { return v.EnvironmentName })
}

// Environment reference id.
func (o SsisEnvironmentReferenceResponseOutput) Id() pulumix.Output[*float64] {
	return pulumix.Apply[SsisEnvironmentReferenceResponse](o, func(v SsisEnvironmentReferenceResponse) *float64 { return v.Id })
}

// Reference type
func (o SsisEnvironmentReferenceResponseOutput) ReferenceType() pulumix.Output[*string] {
	return pulumix.Apply[SsisEnvironmentReferenceResponse](o, func(v SsisEnvironmentReferenceResponse) *string { return v.ReferenceType })
}

// Ssis environment.
type SsisEnvironmentResponse struct {
	// Metadata description.
	Description *string `pulumi:"description"`
	// Folder id which contains environment.
	FolderId *float64 `pulumi:"folderId"`
	// Metadata id.
	Id *float64 `pulumi:"id"`
	// Metadata name.
	Name *string `pulumi:"name"`
	// The type of SSIS object metadata.
	// Expected value is 'Environment'.
	Type string `pulumi:"type"`
	// Variable in environment
	Variables []*SsisVariableResponse `pulumi:"variables"`
}

// Ssis environment.
type SsisEnvironmentResponseArgs struct {
	// Metadata description.
	Description pulumix.Input[*string] `pulumi:"description"`
	// Folder id which contains environment.
	FolderId pulumix.Input[*float64] `pulumi:"folderId"`
	// Metadata id.
	Id pulumix.Input[*float64] `pulumi:"id"`
	// Metadata name.
	Name pulumix.Input[*string] `pulumi:"name"`
	// The type of SSIS object metadata.
	// Expected value is 'Environment'.
	Type pulumix.Input[string] `pulumi:"type"`
	// Variable in environment
	Variables pulumix.Input[[]*SsisVariableResponseArgs] `pulumi:"variables"`
}

func (SsisEnvironmentResponseArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*SsisEnvironmentResponse)(nil)).Elem()
}

func (i SsisEnvironmentResponseArgs) ToSsisEnvironmentResponseOutput() SsisEnvironmentResponseOutput {
	return i.ToSsisEnvironmentResponseOutputWithContext(context.Background())
}

func (i SsisEnvironmentResponseArgs) ToSsisEnvironmentResponseOutputWithContext(ctx context.Context) SsisEnvironmentResponseOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SsisEnvironmentResponseOutput)
}

func (i *SsisEnvironmentResponseArgs) ToOutput(ctx context.Context) pulumix.Output[*SsisEnvironmentResponseArgs] {
	return pulumix.Val(i)
}

// Ssis environment.
type SsisEnvironmentResponseOutput struct{ *pulumi.OutputState }

func (SsisEnvironmentResponseOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*SsisEnvironmentResponse)(nil)).Elem()
}

func (o SsisEnvironmentResponseOutput) ToSsisEnvironmentResponseOutput() SsisEnvironmentResponseOutput {
	return o
}

func (o SsisEnvironmentResponseOutput) ToSsisEnvironmentResponseOutputWithContext(ctx context.Context) SsisEnvironmentResponseOutput {
	return o
}

func (o SsisEnvironmentResponseOutput) ToOutput(ctx context.Context) pulumix.Output[SsisEnvironmentResponse] {
	return pulumix.Output[SsisEnvironmentResponse]{
		OutputState: o.OutputState,
	}
}

// Metadata description.
func (o SsisEnvironmentResponseOutput) Description() pulumix.Output[*string] {
	return pulumix.Apply[SsisEnvironmentResponse](o, func(v SsisEnvironmentResponse) *string { return v.Description })
}

// Folder id which contains environment.
func (o SsisEnvironmentResponseOutput) FolderId() pulumix.Output[*float64] {
	return pulumix.Apply[SsisEnvironmentResponse](o, func(v SsisEnvironmentResponse) *float64 { return v.FolderId })
}

// Metadata id.
func (o SsisEnvironmentResponseOutput) Id() pulumix.Output[*float64] {
	return pulumix.Apply[SsisEnvironmentResponse](o, func(v SsisEnvironmentResponse) *float64 { return v.Id })
}

// Metadata name.
func (o SsisEnvironmentResponseOutput) Name() pulumix.Output[*string] {
	return pulumix.Apply[SsisEnvironmentResponse](o, func(v SsisEnvironmentResponse) *string { return v.Name })
}

// The type of SSIS object metadata.
// Expected value is 'Environment'.
func (o SsisEnvironmentResponseOutput) Type() pulumix.Output[string] {
	return pulumix.Apply[SsisEnvironmentResponse](o, func(v SsisEnvironmentResponse) string { return v.Type })
}

// Variable in environment
func (o SsisEnvironmentResponseOutput) Variables() pulumix.GArrayOutput[SsisVariableResponse, SsisVariableResponseOutput] {
	value := pulumix.Apply[SsisEnvironmentResponse](o, func(v SsisEnvironmentResponse) []*SsisVariableResponse { return v.Variables })
	return pulumix.GArrayOutput[SsisVariableResponse, SsisVariableResponseOutput]{OutputState: value.OutputState}
}

// Ssis folder.
type SsisFolderResponse struct {
	// Metadata description.
	Description *string `pulumi:"description"`
	// Metadata id.
	Id *float64 `pulumi:"id"`
	// Metadata name.
	Name *string `pulumi:"name"`
	// The type of SSIS object metadata.
	// Expected value is 'Folder'.
	Type string `pulumi:"type"`
}

// Ssis folder.
type SsisFolderResponseArgs struct {
	// Metadata description.
	Description pulumix.Input[*string] `pulumi:"description"`
	// Metadata id.
	Id pulumix.Input[*float64] `pulumi:"id"`
	// Metadata name.
	Name pulumix.Input[*string] `pulumi:"name"`
	// The type of SSIS object metadata.
	// Expected value is 'Folder'.
	Type pulumix.Input[string] `pulumi:"type"`
}

func (SsisFolderResponseArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*SsisFolderResponse)(nil)).Elem()
}

func (i SsisFolderResponseArgs) ToSsisFolderResponseOutput() SsisFolderResponseOutput {
	return i.ToSsisFolderResponseOutputWithContext(context.Background())
}

func (i SsisFolderResponseArgs) ToSsisFolderResponseOutputWithContext(ctx context.Context) SsisFolderResponseOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SsisFolderResponseOutput)
}

func (i *SsisFolderResponseArgs) ToOutput(ctx context.Context) pulumix.Output[*SsisFolderResponseArgs] {
	return pulumix.Val(i)
}

// Ssis folder.
type SsisFolderResponseOutput struct{ *pulumi.OutputState }

func (SsisFolderResponseOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*SsisFolderResponse)(nil)).Elem()
}

func (o SsisFolderResponseOutput) ToSsisFolderResponseOutput() SsisFolderResponseOutput {
	return o
}

func (o SsisFolderResponseOutput) ToSsisFolderResponseOutputWithContext(ctx context.Context) SsisFolderResponseOutput {
	return o
}

func (o SsisFolderResponseOutput) ToOutput(ctx context.Context) pulumix.Output[SsisFolderResponse] {
	return pulumix.Output[SsisFolderResponse]{
		OutputState: o.OutputState,
	}
}

// Metadata description.
func (o SsisFolderResponseOutput) Description() pulumix.Output[*string] {
	return pulumix.Apply[SsisFolderResponse](o, func(v SsisFolderResponse) *string { return v.Description })
}

// Metadata id.
func (o SsisFolderResponseOutput) Id() pulumix.Output[*float64] {
	return pulumix.Apply[SsisFolderResponse](o, func(v SsisFolderResponse) *float64 { return v.Id })
}

// Metadata name.
func (o SsisFolderResponseOutput) Name() pulumix.Output[*string] {
	return pulumix.Apply[SsisFolderResponse](o, func(v SsisFolderResponse) *string { return v.Name })
}

// The type of SSIS object metadata.
// Expected value is 'Folder'.
func (o SsisFolderResponseOutput) Type() pulumix.Output[string] {
	return pulumix.Apply[SsisFolderResponse](o, func(v SsisFolderResponse) string { return v.Type })
}

// Ssis Package.
type SsisPackageResponse struct {
	// Metadata description.
	Description *string `pulumi:"description"`
	// Folder id which contains package.
	FolderId *float64 `pulumi:"folderId"`
	// Metadata id.
	Id *float64 `pulumi:"id"`
	// Metadata name.
	Name *string `pulumi:"name"`
	// Parameters in package
	Parameters []*SsisParameterResponse `pulumi:"parameters"`
	// Project id which contains package.
	ProjectId *float64 `pulumi:"projectId"`
	// Project version which contains package.
	ProjectVersion *float64 `pulumi:"projectVersion"`
	// The type of SSIS object metadata.
	// Expected value is 'Package'.
	Type string `pulumi:"type"`
}

// Ssis Package.
type SsisPackageResponseArgs struct {
	// Metadata description.
	Description pulumix.Input[*string] `pulumi:"description"`
	// Folder id which contains package.
	FolderId pulumix.Input[*float64] `pulumi:"folderId"`
	// Metadata id.
	Id pulumix.Input[*float64] `pulumi:"id"`
	// Metadata name.
	Name pulumix.Input[*string] `pulumi:"name"`
	// Parameters in package
	Parameters pulumix.Input[[]*SsisParameterResponseArgs] `pulumi:"parameters"`
	// Project id which contains package.
	ProjectId pulumix.Input[*float64] `pulumi:"projectId"`
	// Project version which contains package.
	ProjectVersion pulumix.Input[*float64] `pulumi:"projectVersion"`
	// The type of SSIS object metadata.
	// Expected value is 'Package'.
	Type pulumix.Input[string] `pulumi:"type"`
}

func (SsisPackageResponseArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*SsisPackageResponse)(nil)).Elem()
}

func (i SsisPackageResponseArgs) ToSsisPackageResponseOutput() SsisPackageResponseOutput {
	return i.ToSsisPackageResponseOutputWithContext(context.Background())
}

func (i SsisPackageResponseArgs) ToSsisPackageResponseOutputWithContext(ctx context.Context) SsisPackageResponseOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SsisPackageResponseOutput)
}

func (i *SsisPackageResponseArgs) ToOutput(ctx context.Context) pulumix.Output[*SsisPackageResponseArgs] {
	return pulumix.Val(i)
}

// Ssis Package.
type SsisPackageResponseOutput struct{ *pulumi.OutputState }

func (SsisPackageResponseOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*SsisPackageResponse)(nil)).Elem()
}

func (o SsisPackageResponseOutput) ToSsisPackageResponseOutput() SsisPackageResponseOutput {
	return o
}

func (o SsisPackageResponseOutput) ToSsisPackageResponseOutputWithContext(ctx context.Context) SsisPackageResponseOutput {
	return o
}

func (o SsisPackageResponseOutput) ToOutput(ctx context.Context) pulumix.Output[SsisPackageResponse] {
	return pulumix.Output[SsisPackageResponse]{
		OutputState: o.OutputState,
	}
}

// Metadata description.
func (o SsisPackageResponseOutput) Description() pulumix.Output[*string] {
	return pulumix.Apply[SsisPackageResponse](o, func(v SsisPackageResponse) *string { return v.Description })
}

// Folder id which contains package.
func (o SsisPackageResponseOutput) FolderId() pulumix.Output[*float64] {
	return pulumix.Apply[SsisPackageResponse](o, func(v SsisPackageResponse) *float64 { return v.FolderId })
}

// Metadata id.
func (o SsisPackageResponseOutput) Id() pulumix.Output[*float64] {
	return pulumix.Apply[SsisPackageResponse](o, func(v SsisPackageResponse) *float64 { return v.Id })
}

// Metadata name.
func (o SsisPackageResponseOutput) Name() pulumix.Output[*string] {
	return pulumix.Apply[SsisPackageResponse](o, func(v SsisPackageResponse) *string { return v.Name })
}

// Parameters in package
func (o SsisPackageResponseOutput) Parameters() pulumix.GArrayOutput[SsisParameterResponse, SsisParameterResponseOutput] {
	value := pulumix.Apply[SsisPackageResponse](o, func(v SsisPackageResponse) []*SsisParameterResponse { return v.Parameters })
	return pulumix.GArrayOutput[SsisParameterResponse, SsisParameterResponseOutput]{OutputState: value.OutputState}
}

// Project id which contains package.
func (o SsisPackageResponseOutput) ProjectId() pulumix.Output[*float64] {
	return pulumix.Apply[SsisPackageResponse](o, func(v SsisPackageResponse) *float64 { return v.ProjectId })
}

// Project version which contains package.
func (o SsisPackageResponseOutput) ProjectVersion() pulumix.Output[*float64] {
	return pulumix.Apply[SsisPackageResponse](o, func(v SsisPackageResponse) *float64 { return v.ProjectVersion })
}

// The type of SSIS object metadata.
// Expected value is 'Package'.
func (o SsisPackageResponseOutput) Type() pulumix.Output[string] {
	return pulumix.Apply[SsisPackageResponse](o, func(v SsisPackageResponse) string { return v.Type })
}

// Ssis parameter.
type SsisParameterResponse struct {
	// Parameter type.
	DataType *string `pulumi:"dataType"`
	// Default value of parameter.
	DefaultValue *string `pulumi:"defaultValue"`
	// Parameter description.
	Description *string `pulumi:"description"`
	// Design default value of parameter.
	DesignDefaultValue *string `pulumi:"designDefaultValue"`
	// Parameter id.
	Id *float64 `pulumi:"id"`
	// Parameter name.
	Name *string `pulumi:"name"`
	// Whether parameter is required.
	Required *bool `pulumi:"required"`
	// Whether parameter is sensitive.
	Sensitive *bool `pulumi:"sensitive"`
	// Default sensitive value of parameter.
	SensitiveDefaultValue *string `pulumi:"sensitiveDefaultValue"`
	// Parameter value set.
	ValueSet *bool `pulumi:"valueSet"`
	// Parameter value type.
	ValueType *string `pulumi:"valueType"`
	// Parameter reference variable.
	Variable *string `pulumi:"variable"`
}

// Ssis parameter.
type SsisParameterResponseArgs struct {
	// Parameter type.
	DataType pulumix.Input[*string] `pulumi:"dataType"`
	// Default value of parameter.
	DefaultValue pulumix.Input[*string] `pulumi:"defaultValue"`
	// Parameter description.
	Description pulumix.Input[*string] `pulumi:"description"`
	// Design default value of parameter.
	DesignDefaultValue pulumix.Input[*string] `pulumi:"designDefaultValue"`
	// Parameter id.
	Id pulumix.Input[*float64] `pulumi:"id"`
	// Parameter name.
	Name pulumix.Input[*string] `pulumi:"name"`
	// Whether parameter is required.
	Required pulumix.Input[*bool] `pulumi:"required"`
	// Whether parameter is sensitive.
	Sensitive pulumix.Input[*bool] `pulumi:"sensitive"`
	// Default sensitive value of parameter.
	SensitiveDefaultValue pulumix.Input[*string] `pulumi:"sensitiveDefaultValue"`
	// Parameter value set.
	ValueSet pulumix.Input[*bool] `pulumi:"valueSet"`
	// Parameter value type.
	ValueType pulumix.Input[*string] `pulumi:"valueType"`
	// Parameter reference variable.
	Variable pulumix.Input[*string] `pulumi:"variable"`
}

func (SsisParameterResponseArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*SsisParameterResponse)(nil)).Elem()
}

func (i SsisParameterResponseArgs) ToSsisParameterResponseOutput() SsisParameterResponseOutput {
	return i.ToSsisParameterResponseOutputWithContext(context.Background())
}

func (i SsisParameterResponseArgs) ToSsisParameterResponseOutputWithContext(ctx context.Context) SsisParameterResponseOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SsisParameterResponseOutput)
}

func (i *SsisParameterResponseArgs) ToOutput(ctx context.Context) pulumix.Output[*SsisParameterResponseArgs] {
	return pulumix.Val(i)
}

// Ssis parameter.
type SsisParameterResponseOutput struct{ *pulumi.OutputState }

func (SsisParameterResponseOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*SsisParameterResponse)(nil)).Elem()
}

func (o SsisParameterResponseOutput) ToSsisParameterResponseOutput() SsisParameterResponseOutput {
	return o
}

func (o SsisParameterResponseOutput) ToSsisParameterResponseOutputWithContext(ctx context.Context) SsisParameterResponseOutput {
	return o
}

func (o SsisParameterResponseOutput) ToOutput(ctx context.Context) pulumix.Output[SsisParameterResponse] {
	return pulumix.Output[SsisParameterResponse]{
		OutputState: o.OutputState,
	}
}

// Parameter type.
func (o SsisParameterResponseOutput) DataType() pulumix.Output[*string] {
	return pulumix.Apply[SsisParameterResponse](o, func(v SsisParameterResponse) *string { return v.DataType })
}

// Default value of parameter.
func (o SsisParameterResponseOutput) DefaultValue() pulumix.Output[*string] {
	return pulumix.Apply[SsisParameterResponse](o, func(v SsisParameterResponse) *string { return v.DefaultValue })
}

// Parameter description.
func (o SsisParameterResponseOutput) Description() pulumix.Output[*string] {
	return pulumix.Apply[SsisParameterResponse](o, func(v SsisParameterResponse) *string { return v.Description })
}

// Design default value of parameter.
func (o SsisParameterResponseOutput) DesignDefaultValue() pulumix.Output[*string] {
	return pulumix.Apply[SsisParameterResponse](o, func(v SsisParameterResponse) *string { return v.DesignDefaultValue })
}

// Parameter id.
func (o SsisParameterResponseOutput) Id() pulumix.Output[*float64] {
	return pulumix.Apply[SsisParameterResponse](o, func(v SsisParameterResponse) *float64 { return v.Id })
}

// Parameter name.
func (o SsisParameterResponseOutput) Name() pulumix.Output[*string] {
	return pulumix.Apply[SsisParameterResponse](o, func(v SsisParameterResponse) *string { return v.Name })
}

// Whether parameter is required.
func (o SsisParameterResponseOutput) Required() pulumix.Output[*bool] {
	return pulumix.Apply[SsisParameterResponse](o, func(v SsisParameterResponse) *bool { return v.Required })
}

// Whether parameter is sensitive.
func (o SsisParameterResponseOutput) Sensitive() pulumix.Output[*bool] {
	return pulumix.Apply[SsisParameterResponse](o, func(v SsisParameterResponse) *bool { return v.Sensitive })
}

// Default sensitive value of parameter.
func (o SsisParameterResponseOutput) SensitiveDefaultValue() pulumix.Output[*string] {
	return pulumix.Apply[SsisParameterResponse](o, func(v SsisParameterResponse) *string { return v.SensitiveDefaultValue })
}

// Parameter value set.
func (o SsisParameterResponseOutput) ValueSet() pulumix.Output[*bool] {
	return pulumix.Apply[SsisParameterResponse](o, func(v SsisParameterResponse) *bool { return v.ValueSet })
}

// Parameter value type.
func (o SsisParameterResponseOutput) ValueType() pulumix.Output[*string] {
	return pulumix.Apply[SsisParameterResponse](o, func(v SsisParameterResponse) *string { return v.ValueType })
}

// Parameter reference variable.
func (o SsisParameterResponseOutput) Variable() pulumix.Output[*string] {
	return pulumix.Apply[SsisParameterResponse](o, func(v SsisParameterResponse) *string { return v.Variable })
}

// Ssis project.
type SsisProjectResponse struct {
	// Metadata description.
	Description *string `pulumi:"description"`
	// Environment reference in project
	EnvironmentRefs []*SsisEnvironmentReferenceResponse `pulumi:"environmentRefs"`
	// Folder id which contains project.
	FolderId *float64 `pulumi:"folderId"`
	// Metadata id.
	Id *float64 `pulumi:"id"`
	// Metadata name.
	Name *string `pulumi:"name"`
	// Parameters in project
	Parameters []*SsisParameterResponse `pulumi:"parameters"`
	// The type of SSIS object metadata.
	// Expected value is 'Project'.
	Type string `pulumi:"type"`
	// Project version.
	Version *float64 `pulumi:"version"`
}

// Ssis project.
type SsisProjectResponseArgs struct {
	// Metadata description.
	Description pulumix.Input[*string] `pulumi:"description"`
	// Environment reference in project
	EnvironmentRefs pulumix.Input[[]*SsisEnvironmentReferenceResponseArgs] `pulumi:"environmentRefs"`
	// Folder id which contains project.
	FolderId pulumix.Input[*float64] `pulumi:"folderId"`
	// Metadata id.
	Id pulumix.Input[*float64] `pulumi:"id"`
	// Metadata name.
	Name pulumix.Input[*string] `pulumi:"name"`
	// Parameters in project
	Parameters pulumix.Input[[]*SsisParameterResponseArgs] `pulumi:"parameters"`
	// The type of SSIS object metadata.
	// Expected value is 'Project'.
	Type pulumix.Input[string] `pulumi:"type"`
	// Project version.
	Version pulumix.Input[*float64] `pulumi:"version"`
}

func (SsisProjectResponseArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*SsisProjectResponse)(nil)).Elem()
}

func (i SsisProjectResponseArgs) ToSsisProjectResponseOutput() SsisProjectResponseOutput {
	return i.ToSsisProjectResponseOutputWithContext(context.Background())
}

func (i SsisProjectResponseArgs) ToSsisProjectResponseOutputWithContext(ctx context.Context) SsisProjectResponseOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SsisProjectResponseOutput)
}

func (i *SsisProjectResponseArgs) ToOutput(ctx context.Context) pulumix.Output[*SsisProjectResponseArgs] {
	return pulumix.Val(i)
}

// Ssis project.
type SsisProjectResponseOutput struct{ *pulumi.OutputState }

func (SsisProjectResponseOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*SsisProjectResponse)(nil)).Elem()
}

func (o SsisProjectResponseOutput) ToSsisProjectResponseOutput() SsisProjectResponseOutput {
	return o
}

func (o SsisProjectResponseOutput) ToSsisProjectResponseOutputWithContext(ctx context.Context) SsisProjectResponseOutput {
	return o
}

func (o SsisProjectResponseOutput) ToOutput(ctx context.Context) pulumix.Output[SsisProjectResponse] {
	return pulumix.Output[SsisProjectResponse]{
		OutputState: o.OutputState,
	}
}

// Metadata description.
func (o SsisProjectResponseOutput) Description() pulumix.Output[*string] {
	return pulumix.Apply[SsisProjectResponse](o, func(v SsisProjectResponse) *string { return v.Description })
}

// Environment reference in project
func (o SsisProjectResponseOutput) EnvironmentRefs() pulumix.GArrayOutput[SsisEnvironmentReferenceResponse, SsisEnvironmentReferenceResponseOutput] {
	value := pulumix.Apply[SsisProjectResponse](o, func(v SsisProjectResponse) []*SsisEnvironmentReferenceResponse { return v.EnvironmentRefs })
	return pulumix.GArrayOutput[SsisEnvironmentReferenceResponse, SsisEnvironmentReferenceResponseOutput]{OutputState: value.OutputState}
}

// Folder id which contains project.
func (o SsisProjectResponseOutput) FolderId() pulumix.Output[*float64] {
	return pulumix.Apply[SsisProjectResponse](o, func(v SsisProjectResponse) *float64 { return v.FolderId })
}

// Metadata id.
func (o SsisProjectResponseOutput) Id() pulumix.Output[*float64] {
	return pulumix.Apply[SsisProjectResponse](o, func(v SsisProjectResponse) *float64 { return v.Id })
}

// Metadata name.
func (o SsisProjectResponseOutput) Name() pulumix.Output[*string] {
	return pulumix.Apply[SsisProjectResponse](o, func(v SsisProjectResponse) *string { return v.Name })
}

// Parameters in project
func (o SsisProjectResponseOutput) Parameters() pulumix.GArrayOutput[SsisParameterResponse, SsisParameterResponseOutput] {
	value := pulumix.Apply[SsisProjectResponse](o, func(v SsisProjectResponse) []*SsisParameterResponse { return v.Parameters })
	return pulumix.GArrayOutput[SsisParameterResponse, SsisParameterResponseOutput]{OutputState: value.OutputState}
}

// The type of SSIS object metadata.
// Expected value is 'Project'.
func (o SsisProjectResponseOutput) Type() pulumix.Output[string] {
	return pulumix.Apply[SsisProjectResponse](o, func(v SsisProjectResponse) string { return v.Type })
}

// Project version.
func (o SsisProjectResponseOutput) Version() pulumix.Output[*float64] {
	return pulumix.Apply[SsisProjectResponse](o, func(v SsisProjectResponse) *float64 { return v.Version })
}

// Ssis variable.
type SsisVariableResponse struct {
	// Variable type.
	DataType *string `pulumi:"dataType"`
	// Variable description.
	Description *string `pulumi:"description"`
	// Variable id.
	Id *float64 `pulumi:"id"`
	// Variable name.
	Name *string `pulumi:"name"`
	// Whether variable is sensitive.
	Sensitive *bool `pulumi:"sensitive"`
	// Variable sensitive value.
	SensitiveValue *string `pulumi:"sensitiveValue"`
	// Variable value.
	Value *string `pulumi:"value"`
}

// Ssis variable.
type SsisVariableResponseArgs struct {
	// Variable type.
	DataType pulumix.Input[*string] `pulumi:"dataType"`
	// Variable description.
	Description pulumix.Input[*string] `pulumi:"description"`
	// Variable id.
	Id pulumix.Input[*float64] `pulumi:"id"`
	// Variable name.
	Name pulumix.Input[*string] `pulumi:"name"`
	// Whether variable is sensitive.
	Sensitive pulumix.Input[*bool] `pulumi:"sensitive"`
	// Variable sensitive value.
	SensitiveValue pulumix.Input[*string] `pulumi:"sensitiveValue"`
	// Variable value.
	Value pulumix.Input[*string] `pulumi:"value"`
}

func (SsisVariableResponseArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*SsisVariableResponse)(nil)).Elem()
}

func (i SsisVariableResponseArgs) ToSsisVariableResponseOutput() SsisVariableResponseOutput {
	return i.ToSsisVariableResponseOutputWithContext(context.Background())
}

func (i SsisVariableResponseArgs) ToSsisVariableResponseOutputWithContext(ctx context.Context) SsisVariableResponseOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SsisVariableResponseOutput)
}

func (i *SsisVariableResponseArgs) ToOutput(ctx context.Context) pulumix.Output[*SsisVariableResponseArgs] {
	return pulumix.Val(i)
}

// Ssis variable.
type SsisVariableResponseOutput struct{ *pulumi.OutputState }

func (SsisVariableResponseOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*SsisVariableResponse)(nil)).Elem()
}

func (o SsisVariableResponseOutput) ToSsisVariableResponseOutput() SsisVariableResponseOutput {
	return o
}

func (o SsisVariableResponseOutput) ToSsisVariableResponseOutputWithContext(ctx context.Context) SsisVariableResponseOutput {
	return o
}

func (o SsisVariableResponseOutput) ToOutput(ctx context.Context) pulumix.Output[SsisVariableResponse] {
	return pulumix.Output[SsisVariableResponse]{
		OutputState: o.OutputState,
	}
}

// Variable type.
func (o SsisVariableResponseOutput) DataType() pulumix.Output[*string] {
	return pulumix.Apply[SsisVariableResponse](o, func(v SsisVariableResponse) *string { return v.DataType })
}

// Variable description.
func (o SsisVariableResponseOutput) Description() pulumix.Output[*string] {
	return pulumix.Apply[SsisVariableResponse](o, func(v SsisVariableResponse) *string { return v.Description })
}

// Variable id.
func (o SsisVariableResponseOutput) Id() pulumix.Output[*float64] {
	return pulumix.Apply[SsisVariableResponse](o, func(v SsisVariableResponse) *float64 { return v.Id })
}

// Variable name.
func (o SsisVariableResponseOutput) Name() pulumix.Output[*string] {
	return pulumix.Apply[SsisVariableResponse](o, func(v SsisVariableResponse) *string { return v.Name })
}

// Whether variable is sensitive.
func (o SsisVariableResponseOutput) Sensitive() pulumix.Output[*bool] {
	return pulumix.Apply[SsisVariableResponse](o, func(v SsisVariableResponse) *bool { return v.Sensitive })
}

// Variable sensitive value.
func (o SsisVariableResponseOutput) SensitiveValue() pulumix.Output[*string] {
	return pulumix.Apply[SsisVariableResponse](o, func(v SsisVariableResponse) *string { return v.SensitiveValue })
}

// Variable value.
func (o SsisVariableResponseOutput) Value() pulumix.Output[*string] {
	return pulumix.Apply[SsisVariableResponse](o, func(v SsisVariableResponse) *string { return v.Value })
}

// An access key for the storage account.
type StorageAccountKeyResponse struct {
	// Creation time of the key, in round trip date format.
	CreationTime string `pulumi:"creationTime"`
	// Name of the key.
	KeyName string `pulumi:"keyName"`
	// Permissions for the key -- read-only or full permissions.
	Permissions string `pulumi:"permissions"`
	// Base 64-encoded value of the key.
	Value string `pulumi:"value"`
}

// An access key for the storage account.
type StorageAccountKeyResponseArgs struct {
	// Creation time of the key, in round trip date format.
	CreationTime pulumix.Input[string] `pulumi:"creationTime"`
	// Name of the key.
	KeyName pulumix.Input[string] `pulumi:"keyName"`
	// Permissions for the key -- read-only or full permissions.
	Permissions pulumix.Input[string] `pulumi:"permissions"`
	// Base 64-encoded value of the key.
	Value pulumix.Input[string] `pulumi:"value"`
}

func (StorageAccountKeyResponseArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*StorageAccountKeyResponse)(nil)).Elem()
}

func (i StorageAccountKeyResponseArgs) ToStorageAccountKeyResponseOutput() StorageAccountKeyResponseOutput {
	return i.ToStorageAccountKeyResponseOutputWithContext(context.Background())
}

func (i StorageAccountKeyResponseArgs) ToStorageAccountKeyResponseOutputWithContext(ctx context.Context) StorageAccountKeyResponseOutput {
	return pulumi.ToOutputWithContext(ctx, i).(StorageAccountKeyResponseOutput)
}

func (i *StorageAccountKeyResponseArgs) ToOutput(ctx context.Context) pulumix.Output[*StorageAccountKeyResponseArgs] {
	return pulumix.Val(i)
}

// An access key for the storage account.
type StorageAccountKeyResponseOutput struct{ *pulumi.OutputState }

func (StorageAccountKeyResponseOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*StorageAccountKeyResponse)(nil)).Elem()
}

func (o StorageAccountKeyResponseOutput) ToStorageAccountKeyResponseOutput() StorageAccountKeyResponseOutput {
	return o
}

func (o StorageAccountKeyResponseOutput) ToStorageAccountKeyResponseOutputWithContext(ctx context.Context) StorageAccountKeyResponseOutput {
	return o
}

func (o StorageAccountKeyResponseOutput) ToOutput(ctx context.Context) pulumix.Output[StorageAccountKeyResponse] {
	return pulumix.Output[StorageAccountKeyResponse]{
		OutputState: o.OutputState,
	}
}

// Creation time of the key, in round trip date format.
func (o StorageAccountKeyResponseOutput) CreationTime() pulumix.Output[string] {
	return pulumix.Apply[StorageAccountKeyResponse](o, func(v StorageAccountKeyResponse) string { return v.CreationTime })
}

// Name of the key.
func (o StorageAccountKeyResponseOutput) KeyName() pulumix.Output[string] {
	return pulumix.Apply[StorageAccountKeyResponse](o, func(v StorageAccountKeyResponse) string { return v.KeyName })
}

// Permissions for the key -- read-only or full permissions.
func (o StorageAccountKeyResponseOutput) Permissions() pulumix.Output[string] {
	return pulumix.Apply[StorageAccountKeyResponse](o, func(v StorageAccountKeyResponse) string { return v.Permissions })
}

// Base 64-encoded value of the key.
func (o StorageAccountKeyResponseOutput) Value() pulumix.Output[string] {
	return pulumix.Apply[StorageAccountKeyResponse](o, func(v StorageAccountKeyResponse) string { return v.Value })
}

func init() {
	pulumi.RegisterOutputType(BastionShareableLinkOutput{})
	pulumi.RegisterOutputType(SsisEnvironmentReferenceResponseOutput{})
	pulumi.RegisterOutputType(SsisEnvironmentResponseOutput{})
	pulumi.RegisterOutputType(SsisFolderResponseOutput{})
	pulumi.RegisterOutputType(SsisPackageResponseOutput{})
	pulumi.RegisterOutputType(SsisParameterResponseOutput{})
	pulumi.RegisterOutputType(SsisProjectResponseOutput{})
	pulumi.RegisterOutputType(SsisVariableResponseOutput{})
	pulumi.RegisterOutputType(StorageAccountKeyResponseOutput{})
}
