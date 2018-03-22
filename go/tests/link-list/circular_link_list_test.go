package list

import (
	"algorithm/go/linklist"
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestShouldCreate(t *testing.T) {
	var head *linklist.ListNode
	first := linklist.CreateCircularLL(head, 5)
	second := linklist.CreateCircularLL(first, 4)

	assert.Equal(t, 5, first.Data)
	assert.Equal(t, 4, first.Next.Data)
	assert.Equal(t, second.Next.Next, first)
}

func TestShouldBeAbleToAddToBegining(t *testing.T) {
	var head *linklist.ListNode

	first := linklist.CreateCircularLL(head, 5)
	second := linklist.AddToBeginingOfCircularLL(first, 4)

	assert.Equal(t, second.Next, first)
}

func TestShouldBeAbleToAddToEnd(t *testing.T) {
	var head *linklist.ListNode

	first := linklist.CreateCircularLL(head, 5)
	second := linklist.AddToEndOfCircularLL(first, 4)

	assert.Equal(t, second.Next.Next, first)
}

func TestShouldBeAbleToDeleteFromStart(t *testing.T) {
	var head *linklist.ListNode

	first := linklist.CreateCircularLL(head, 5)
	second := linklist.AddToBeginingOfCircularLL(first, 4)

	assert.Equal(t, first, linklist.DeleteBeginingOfCircularLL(second))
}

func TestShouldBeAbleToDeleteFromStartForNil(t *testing.T) {
	var head *linklist.ListNode

	assert.Equal(t, head, linklist.DeleteBeginingOfCircularLL(head))
}
