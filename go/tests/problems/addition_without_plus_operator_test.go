package problems

import (
	"algorithm/go/problems"
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestShouldRunAddWithoutPlus(t *testing.T) {
	problems.AddWithoutPlusOperator(23, 37)
}

func TestShouldBeAbleToAddTwoNumbers(t *testing.T) {
	assert.Equal(t, 60, problems.AddWithoutPlusOperator(23, 37))
}
