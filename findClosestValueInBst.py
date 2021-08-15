def findClosestValueInBst(tree, target):
    return findClosestValueInBstHelper(tree, target, float("inf"))

def findClosestValueInBstHelper(tree,target, closest):
	if tree is None:
		return closest
	
	if abs(target - closest) > abs(target - tree.value):
		closest = tree.value
	
	# compare current value with the target, and see where we want to go in thr bst:
	if target < tree.value:
		return findClosestValueInBstHelper(tree.left, target, closest)
	elif target > tree.value:
		return findClosestValueInBstHelper(tree.right, target, closest)
	else:
		# if the value is equal to target, then there's no need to keep looping, because the diff is zero.
		return closest

# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None