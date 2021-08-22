import unittest


class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# O(N^2) Time | O(h) Space
def reconstructBst(preOrderTraversalValues):
    # to reconstruct a bst using in-order transversal (lef-visit-right) we have two solutions: the first one i sbasically treat each element of the array
	# as the root of its subtree. If we do need, we loop on the subarray that is contained between the [currentIdx, rightIdx], where rightIdx is the previous right node of the parent.
	# this takes O(n^2) time since we need to potentially loop over and over several subarrays.
	# the other solution is to keep track the upper and lower bound for each element of the subarray, check if the element if between those values first for the left, and then for the right.
	
	# base case - when we dont have limits
	if len(preOrderTraversalValues) == 0:
		return None
	
	# initialisation
	currentValue = preOrderTraversalValues[0]
	
	# first find the right value of the node
	rightSubtreeRootIdx = len(preOrderTraversalValues)
	
	# we check on the right on the subtree (WITHOUT INCLUDING THE CURRENT ELEMENT, THAT'S WHY WE USE THE 1)
	# to see if there is an element bigger than current value. 
	for idx in range(1, len(preOrderTraversalValues)):
		value = preOrderTraversalValues[idx]
		if value >= currentValue:
			rightSubtreeRootIdx = idx
			break
		
	# then find the left subtree and right subtree. Basically, we slice the preorder array from 1 (i.e. second index of the right, it will be always the left element),
	# and the rightSubtreeRoot index (the upper bound). For the right subtree, is the other subarray. This will keep looking
	# until hitting the base case, where the preorder is an empty array; that case we return None and None 
	leftSubtree = reconstructBst(preOrderTraversalValues[1:rightSubtreeRootIdx])
	rightSubtree = reconstructBst(preOrderTraversalValues[rightSubtreeRootIdx:])
	return BST(currentValue, leftSubtree, rightSubtree)


class TreeInfo:
	def __init__(self, rootIdx):
		self.rootIdx = rootIdx

# O(N) time | O(h) space
def reconstructBst2(preOrderTraversalValues):
    treeInfo = TreeInfo(0)
    return reconstructBstFromRange(float('-inf'), float('inf'),preOrderTraversalValues, treeInfo)

def reconstructBstFromRange(lowerBound, upperBound, preOrderTraversalValues, currentSubtreeInfo):
	# base case - we will increment the root idx, until we hit the len of the pre-Order array. In that case,
	# we simply return none
	if currentSubtreeInfo.rootIdx == len(preOrderTraversalValues):
		return None
	
	#find the current root value of the subtree and check if we are between the range defined.
	# if the node is not included in the range, we simply return none (that means the value, for that subtree doesnt work out)
	rootValue = preOrderTraversalValues[currentSubtreeInfo.rootIdx]
	if rootValue < lowerBound or rootValue >= upperBound:
		return None
	
	# if its valid to be added, then we can keep looping, so we increment the root node
	currentSubtreeInfo.rootIdx += 1
	# for the left subtree, we define the upperbound as the rootValue of the previous node (this is important)
	#
	leftSubtree = reconstructBstFromRange(lowerBound, rootValue, preOrderTraversalValues, currentSubtreeInfo)
	rightSubtree = reconstructBstFromRange(rootValue, upperBound, preOrderTraversalValues, currentSubtreeInfo)
	
	return BST(rootValue, leftSubtree,rightSubtree)
