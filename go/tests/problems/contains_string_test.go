package tests

import (
	"algorithm/go/problems"
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestShouldRun(*testing.T) {
	problems.ContainsString("", "")
}

func TestShouldReturnFalseOnEmpty(t *testing.T) {
	assert.False(t, problems.ContainsString("", "some random"))
	assert.False(t, problems.ContainsString("some tst", ""))
}

func TestShouldPassWhenContains(t *testing.T) {
	assert.True(t, problems.ContainsString("l", "hello"))
	assert.True(t, problems.ContainsString("ll", "hello"))
	assert.True(t, problems.ContainsString("le", "helleo"))
}

func TestShouldReturnFalseOnReverse(t *testing.T) {
	assert.False(t, problems.ContainsString("le", "hello"))
	assert.False(t, problems.ContainsString("lex", "hello"))
	assert.False(t, problems.ContainsString("le", "helxeo"))
}
