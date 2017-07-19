from AVL.Support import height, Node, traverse_in_order, insert_bst


class BalancedBST(object):
    def __init__(self, root_node=None):
        self.root_node = root_node

    def balance_factor(self, root):
        left_height = height(root.left_child)
        right_height = height(root.right_child)

        return left_height - right_height

    def insert(self, value):
        self.root_node = self.insert_node(self.root_node, value)

    def insert_node(self, root, value):
        if not root:
            return Node(value)

        if value < root.value:
            root.left_child = self.insert_node(root.left_child, value)

        else:
            root.right_child = self.insert_node(root.right_child, value)

        root = self.rebalance(root)

        return root

    def traverse_in_order(self):
        if self.root_node:
            traverse_in_order(self.root_node)
            print "Height=%d" % height(self.root_node)

    def rebalance(self, root):
        balance_factor = self.balance_factor(root)

        print "Balance-factor=%d" % balance_factor

        if balance_factor > 1:
            internal_balance = (height(root.left_child.left_child) - height(root.left_child.right_child))
            if internal_balance >= 1:
                root = self.rotate_right(root)
            else:
                root = self.rotate_left_right(root)

        if balance_factor < -1:
            internal_balance = (height(root.right_child.right_child) - height(root.right_child.left_child))

            if internal_balance >= 1:
                root = self.rotate_left(root)

            else:
                root = self.rotate_right_left(root)


        print "Balance-factor(post-balance)=%d" % self.balance_factor(root)

        return root

    def rotate_right(self, root):
        temp_node = root.left_child
        root.left_child = temp_node.right_child

        temp_node.right_child = root
        return temp_node

    def rotate_left(self, root):
        temp_node = root.right_child
        root.right_child = temp_node.left_child

        temp_node.left_child = root
        return temp_node

    def rotate_left_right(self, root):
        root.left_child = self.rotate_left(root.left_child)

        return self.rotate_right(root)

    def rotate_right_left(self, root):
        root.right_child = self.rotate_right(root.right_child)

        return self.rotate_left(root)