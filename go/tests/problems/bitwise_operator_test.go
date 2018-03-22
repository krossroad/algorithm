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

func TestUniqueElement(t *testing.T) {
	assert.Equal(t, 3, problems.UniqueElement([]int{0, 1, 0, 1, 2, 3, 2}))
}
