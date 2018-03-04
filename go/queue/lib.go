package queue

import (
	"errors"
	"math"
)

type Queue struct {
	front, rear, size, capacity int
	collection                  []int
}

func Construct(capacity int) Queue {
	return Queue{
		size:       0,
		capacity:   capacity,
		front:      0,
		rear:       capacity - 1,
		collection: make([]int, capacity),
	}
}

func (this *Queue) Enqueue(value int) *Queue {
	if this.IsFull() {
		return this
	}

	this.rear = (this.rear + 1) % this.capacity
	this.collection[this.rear] = value
	this.size++

	return this
}

func (this *Queue) Dequeue() (int, error) {
	if !this.IsEmpty() {
		value := this.collection[this.front]

		this.front = (this.front + 1) % this.capacity
		this.size--

		return value, nil
	}

	return math.MinInt16, errors.New("Trying to dequeue empty Queue")
}

func (this *Queue) IsEmpty() bool {
	return this.size <= 0
}

func (this *Queue) IsFull() bool {
	return this.size >= this.capacity
}

func (this *Queue) First() int {
	if !this.IsEmpty() {
		return this.collection[this.front]
	}

	return math.MinInt16
}

func (this *Queue) Last() int {
	if !this.IsEmpty() {
		return this.collection[this.rear]
	}

	return math.MinInt16
}
