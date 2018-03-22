package problems

import (
	"algorithm/go/problems"
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestShouldRunBalancedBraces(t *testing.T) {
	problems.BalancedBraces("foo-bar")
}

func TestShouldReturnTrueOnEmpty(t *testing.T) {
	assert.True(t, problems.BalancedBraces(""))
}

func TestShouldReturnFalseOnSingleBraces(t *testing.T) {
	assert.False(t, problems.BalancedBraces("("))
	assert.False(t, problems.BalancedBraces("}"))
}

func TestShouldCheckBalancedBraces(t *testing.T) {
	assert.True(t, problems.BalancedBraces("()"))
	assert.True(t, problems.BalancedBraces("((aaa()))()"))
	assert.False(t, problems.BalancedBraces("({)}"))
	assert.True(t, problems.BalancedBraces("{[()]}"))
	assert.False(t, problems.BalancedBraces("{[(])}"))
	assert.False(t, problems.BalancedBraces("((((((())"))
	assert.True(t, problems.BalancedBraces("{{[[(())]]}}"))
}
