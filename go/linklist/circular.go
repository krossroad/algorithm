package linklist

func CreateCircularLL(head *ListNode, data int) *ListNode {
	newNode := ListNode{Data: data}

	if head == nil {
		newNode.Next = &newNode
		head = &newNode
		return head
	}

	ptr := head
	for ptr.Next != head {
		ptr = ptr.Next
	}

	ptr.Next = &newNode
	newNode.Next = head

	return head
}

func AddToBeginingOfCircularLL(head *ListNode, data int) *ListNode {
	newNode := &ListNode{Data: data}
	newNode.Next = head

	ptr := head
	for ptr.Next != head {
		ptr = ptr.Next
	}
	ptr.Next = newNode

	return newNode
}

func AddToEndOfCircularLL(head *ListNode, data int) *ListNode {
	ptr := head
	for ptr.Next != head {
		ptr = ptr.Next
	}
	newNode := ListNode{Data: data}
	newNode.Next = head
	ptr.Next = &newNode
	return head
}

func DeleteBeginingOfCircularLL(head *ListNode) *ListNode {
	if head != nil {
		tmp := head
		for tmp.Next != head {
			tmp = tmp.Next
		}
		head = head.Next
		tmp.Next = head
	}

	return head
}
