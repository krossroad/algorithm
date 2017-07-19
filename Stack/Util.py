class Stack(object):
    def __init__(self, items=[], size=0):
        self.size = size
        self.items = items

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
