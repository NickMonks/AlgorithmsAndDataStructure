import unittest


# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

# O(h) time | O(1) space
def findSuccessor(tree, node):
    # since we are following the sequence left - root - right, we know for a fact
	# that the next node to be visited is going to the leftmost node of the right subtree. This
	# will always be the case. If we don't have a child node, that means the parent is the successor.
	# However, we need to make sure that the parent is not already being visited; we can do this by
	# simply doing an IF condition: if node.parent.right = node then node = node.parent and repeat logic
	
	if node.right is not None:
		return getLeftmostChild(node)
	
	return getRightmostParent(node)

def getLeftmostChild(node):
	currentNode = node.right
	
	# we will recursively check the leftmost child of the right subtree (since we are doing in-order, we need to get the one of the left)
	while currentNode.left is not None:
		currentNode = currentNode.left
	
	return currentNode

def getRightmostParent(node):
	currentNode = node
	
	# First check if we have a parent; if not, we return None. otherwise, check also
	# that the currentnode is not the right of the parent. if it is, then keep bubbling up
	while currentNode.parent is not None and currentNode.parent.right == currentNode:
		currentNode = currentNode.parent
	
	# return parent, since when we break the condition it didnt update the value
	# AND it will return none if parent is empty anyways
	return currentNode.parent


# O(n) time | O(n) space
def findSuccessor2(tree, node):
    # node: the node we want to find]
	
	# perform in order traversal (left-node-right)
	inOrderTraversalOrder = getInOrderTraversal2(tree)
	
	for idx, currentNode in enumerate(inOrderTraversalOrder):
		if currentNode != node:
			continue
		
		# -1 because there won't be any successor (remeber previous condition)
		if idx == len(inOrderTraversalOrder) -1 :
			return None
		
		# if not reaching the guards, we will return the next value
		return inOrderTraversalOrder[idx+1]

def getInOrderTraversal2(node, order=[]):
	if node is None:
		return order
	
	# We store the nodes in the order where are visited. So we will traverse to the left, then
	# there's no more nodes we simply return and add to our list the current node visited. we
	# traverse to the right following the same logic (not storing since we just want to keep looping)
	getInOrderTraversal2(node.left, order)
	
	# we append the node, not the value - to compare it directly as a node object
	order.append(node)
	getInOrderTraversal2(node.right, order)
	
	# doesnt matter if we keep it or not, since we just mutate the list over and over
	return order

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        root = BinaryTree(1)
        root.left = BinaryTree(2)
        root.left.parent = root
        root.right = BinaryTree(3)
        root.right.parent = root
        root.left.left = BinaryTree(4)
        root.left.left.parent = root.left
        root.left.right = BinaryTree(5)
        root.left.right.parent = root.left
        root.left.left.left = BinaryTree(6)
        root.left.left.left.parent = root.left.left
        node = root.left.right
        expected = root
        actual = findSuccessor(root, node)
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
