package queue

import (
	"errors"
)

type Queue struct {
	front, rear, size, capacity int
	collection                  []interface{}
}

func Construct(capacity int) Queue {
	return Queue{
		size:       0,
		capacity:   capacity,
		front:      0,
		rear:       capacity - 1,
		collection: make([]interface{}, capacity),
	}
}

func (this *Queue) Enqueue(value interface{}) *Queue {
	if this.IsFull() {
		return this
	}

	this.rear = (this.rear + 1) % this.capacity
	this.collection[this.rear] = value
	this.size++

	return this
}

func (this *Queue) Dequeue() (interface{}, error) {
	if !this.IsEmpty() {
		value := this.collection[this.front]

		this.front = (this.front + 1) % this.capacity
		this.size--

		return value, nil
	}

	return nil, errors.New("Trying to dequeue empty Queue")
}

func (this *Queue) IsEmpty() bool {
	return this.size <= 0
}

func (this *Queue) IsFull() bool {
	return this.size >= this.capacity
}

func (this *Queue) First() interface{} {
	if !this.IsEmpty() {
		return this.collection[this.front]
	}

	return nil
}

func (this *Queue) Last() interface{} {
	if !this.IsEmpty() {
		return this.collection[this.rear]
	}

	return nil
}
