# O(N log N) Time (traverse N nodes and insertion takes log N)
# Space O(N) (We insert N nodes in the new BST)
def minHeightBst(array):
	# First, we insert using the naive approach for this problem, using the insert function
	# As we know, the array is sorted; because we roughtly want to have same number of nodes
	# on right and left, we can assume the node we want to be the root is the middle. we would 
	# do this recursively. 
	
	# we define a new recursion function with more arguments: current bst, start index of the subarray
	# and end index of the subarray:
	return constructMinHeight(array, None, 0, len(array) -1)
	
def constructMinHeight(array, bst, startIdx, endIdx):
	
	# if endIdx < startIdx we have reach our base case
	if endIdx < startIdx:
		return
	# round it (doesnt matter which side we get, it wont affect height)
	midIdx = (startIdx + endIdx)//2
	valueToAdd = array[midIdx]
	
	# we use the insert method. However this is not optimal, because it costs us log N:
	if bst is None:
		# if we start iterating it will be none
		bst = BST(valueToAdd)
	else:
		bst.insert(valueToAdd)
	
	#recursively construct the bst sub-trees:
	constructMinHeight(array, bst, startIdx, midIdx -1)
	constructMinHeight(array, bst, midIdx + 1, endIdx)
	
	return bst

def constructMinHeight2(array, bst, startIdx, endIdx):
    	
	# if endIdx < startIdx we have reach our base case
	if endIdx < startIdx:
		return
	# round it (doesnt matter which side we get, it wont affect height)
	midIdx = (startIdx + endIdx)//2
	valueToAdd = array[midIdx]
	
	# manually create the new bst
	newBstNode = BST(array[midIdx])
	if bst is None:
		bst = newBstNode
	else:
		#insert to the left of right, depending of the BST condition
		if array[midIdx] < bst.value:
			bst.left = newBstNode
			# we need to move to the left subtree (because we recursively call and 
			# the node will be the root of that call), remember that we have several
			# clls in the stack
			bst = bst.left
		else:
			bst.right = newBstNode
			bst = bst.right
	
	#recursively construct the bst sub-trees:
	constructMinHeight(array, bst, startIdx, midIdx -1)
	constructMinHeight(array, bst, midIdx + 1, endIdx)
	
	return bst


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)


# ---- SIMPLIFICATION
def constructMinHeight(array, startIdx, endIdx):
    	
	# if endIdx < startIdx we have reach our base case
	if endIdx < startIdx:
		return None
	# round it (doesnt matter which side we get, it wont affect height)
	midIdx = (startIdx + endIdx)//2
	
	bst = BST(array[midIdx])
	#recursively construct the bst sub-trees. Then the recursive call will be equal to the left
	# value of the root node, and the same for the right. This will call until finished
	bst.left = constructMinHeight(array, startIdx, midIdx -1)
	bst.right = constructMinHeight(array, midIdx + 1, endIdx)
	
	return bst