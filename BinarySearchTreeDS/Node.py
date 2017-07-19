class Node(object):
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

    def insert(self, data):
        if data < self.data:
            if not self.leftChild:
                self.leftChild = Node(data)

            else:
                self.leftChild.insert(data)

        else:
            if not self.rightChild:
                self.rightChild = Node(data)

            else:
                self.rightChild.insert(data)

    def getMin(self):
        if not self.leftChild:
            return self.data

        else:
            return  self.leftChild.getMin()

    def getMax(self):
        if not self.rightChild:
            return  self.data

        else:
            return  self.rightChild.getMax()

    def remove(self, data, parentNode):
        if data < self.data:
            if self.leftChild is not None:
                self.leftChild.remove(data, self)

        elif data > self.data:
            if self.rightChild is not None:
                self.rightChild.remove(data, self)

        else:
            if self.leftChild is not None and self.rightChild is not None:
                self.data = self.rightChild.getMax()
                self.rightChild.remove(self.data, self)

            else:
                tempNode = self.leftChild if self.leftChild is not None else self.rightChild

                if parentNode.leftChild == self:
                    parentNode.leftChild = tempNode

                elif parentNode.rightChild == self:
                    parentNode.rightChild = tempNode


    def traverseInOrder(self):
        if self.leftChild:
            self.leftChild.traverseInOrder()

        print self.data

        if self.rightChild:
            self.rightChild.traverseInOrder()