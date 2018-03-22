package stack

type Stack struct {
	top, size, capacity int
	collection          []interface{}
}

func Construct(capacity int) Stack {
	return Stack{
		capacity:   capacity,
		size:       0,
		top:        -1,
		collection: make([]interface{}, capacity),
	}
}

func (this *Stack) Push(value interface{}) *Stack {
	if this.size >= this.capacity {
		panic("Stack-overflow")
	}
	this.top++
	this.size++
	this.collection[this.top] = value

	return this
}

func (this *Stack) Pop() interface{} {
	if !this.IsEmpty() {
		value := this.collection[this.top]
		this.top--
		this.size--

		return value
	}

	return nil
}

func (this *Stack) IsEmpty() bool {
	return this.size <= 0
}

func (this *Stack) Peek() interface{} {
	if !this.IsEmpty() {
		return this.collection[this.top]
	}

	return nil
}
