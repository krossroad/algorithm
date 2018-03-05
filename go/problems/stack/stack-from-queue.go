package stack

import (
	"algorithm/go/queue"
)

const stackSize = 10

type MyStack struct {
	queue1 queue.Queue
	queue2 queue.Queue
}

/** Initialize your data structure here. */
func Constructor() MyStack {
	return MyStack{
		queue1: queue.Construct(stackSize),
		queue2: queue.Construct(stackSize),
	}
}

/** Push element x onto stack. */
func (this *MyStack) Push(x int) {
	this.queue2.Enqueue(x)
QueueScanner:
	for {
		if this.queue1.IsEmpty() {
			break QueueScanner
		}

		value, _ := this.queue1.Dequeue()
		this.queue2.Enqueue(value)
	}

	this.queue1 = this.queue2
	this.queue2 = queue.Construct(stackSize)
}

/** Removes the element on top of the stack and returns that element. */
func (this *MyStack) Pop() interface{} {
	value, _ := this.queue1.Dequeue()
	return value
}

/** Get the top element. */
func (this *MyStack) Top() interface{} {
	return this.queue1.First()
}

/** Returns whether the stack is empty. */
func (this *MyStack) Empty() bool {
	return this.queue1.IsEmpty()
}
