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

//go:generate go run ./generate.go

package main

import (
	"fmt"
	"os"
	"path/filepath"
)

// Split codegen tests into separate packages to extract greater parallelism, breaking up the
// slowest set(s) of tests.
func main() {
	template := `// Copyright 2016-2024, Pulumi Corporation.
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

package %s

import (
	"os"
	"path/filepath"
	"testing"

	"github.com/stretchr/testify/require"

	codegen "github.com/pulumi/pulumi/pkg/v3/codegen/%s"
	"github.com/pulumi/pulumi/pkg/v3/codegen/testing/test"
)

func TestGenerateProgram(t *testing.T) {
	rootDir, err := filepath.Abs(filepath.Join("..", "..", "..", "..", ".."))
	require.NoError(t, err)

	// Change into pkg/codegen/%[2]s
	os.Chdir(filepath.Join(rootDir, "pkg", "codegen", "%[2]s"))
	test.GenerateProgramBatchTest("%[2]s")(t, rootDir, codegen.GenerateProgram, test.ProgramTestBatch(%d, %d))
}`

	n := 6
	for _, lang := range []string{"dotnet", "go", "nodejs", "python"} {
		os.RemoveAll(filepath.Join("../", lang, "gen_program_test"))
		for i := 1; i <= n; i++ {
			packageName := fmt.Sprintf("batch%d", i)
			dir := filepath.Join("../", lang, "gen_program_test", packageName)
			err := os.MkdirAll(dir, 0o755)
			if err != nil {
				panic(fmt.Sprintf("unexpected error generating codegen tests: %v", err))
			}
			testPath := filepath.Join(dir, "gen_program_test.go")

			sourceCode := fmt.Sprintf(template, packageName, lang, i, n)
			err = os.WriteFile(testPath, []byte(sourceCode), 0o755) //nolint:gosec
			if err != nil {
				panic(fmt.Sprintf("unexpected error generating codegen tests: %v", err))
			}
		}
	}
}
