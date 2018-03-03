from collections import deque


class Stack(object):
    def __init__(self, items=[], size=0):
        self.items = items
        self.size = len(items)

    def push(self, item):
        self.size += 1
        self.items.append(item)

    def peek(self):
        if self.size > 0:
            return self.items[-1]

    def pop(self):
        if self.size > 0:
            self.size -= 1
            return self.items.pop()

    def is_empty(self):
        return  self.size <= 0


class Queue(object):
    def __init__(self, items=[], size=0):
        self.items = deque(items)
        self.size = len(items)

    def enqueue(self, item):
        self.size += 1
        self.items.append(item)

    def de_queue(self):
        if self.size > 0:
            self.size -= 1
            return self.items.popleft()

    def peek(self):
        if self.size > 0:
            return self.items[0]

    def is_empty(self):
        return self.size <= 0
