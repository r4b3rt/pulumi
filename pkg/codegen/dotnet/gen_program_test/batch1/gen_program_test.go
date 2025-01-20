// Copyright 2016-2024, Pulumi Corporation.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

// Code generated by "codegen/gen_program_test/generate.go"; DO NOT EDIT.

package batch1

import (
	"os"
	"path/filepath"
	"testing"

	"github.com/stretchr/testify/require"

	codegen "github.com/pulumi/pulumi/pkg/v3/codegen/dotnet"
	"github.com/pulumi/pulumi/pkg/v3/codegen/testing/test"
)

func TestGenerateProgram(t *testing.T) {
	rootDir, err := filepath.Abs(filepath.Join("..", "..", "..", "..", ".."))
	require.NoError(t, err)

	// Change into pkg/codegen/dotnet
	os.Chdir(filepath.Join(rootDir, "pkg", "codegen", "dotnet"))
	test.GenerateProgramBatchTest("dotnet")(t, rootDir, codegen.GenerateProgram, test.ProgramTestBatch(1, 6))
}
