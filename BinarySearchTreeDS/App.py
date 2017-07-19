from BinarySearchTreeDS.BinarySearchTree import BST

bst = BST()

bst.insert(10)
bst.insert(13)
bst.insert(2)
bst.insert(65)

bst.traverse()

bst.remove(10)
bst.remove(65)

print "After removal!!"

bst.traverse()