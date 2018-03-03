class Node(object):
    def __init__(self, val, left_child=None, right_child=None):
        self.value = val
        self.left_child = left_child
        self.right_child = right_child


def height(node):
    return 0 if not node else 1 + max(height(node.left_child),
                                        height(node.right_child))

def insert_bst(parent_node, value):
    if not parent_node:
        return Node(value)

    if (value < parent_node.value):
        parent_node.left_child = insert_bst(parent_node.left_child, value)

    else:
        parent_node.right_child = insert_bst(parent_node.right_child, value)

    return parent_node

def traverse_in_order(node):
    if not node:
        return

    if node.left_child:
        traverse_in_order(node.left_child)

    print "Value=%d, Height=%d" % (node.value,height(node))

    if node.right_child:
        traverse_in_order(node.right_child)
