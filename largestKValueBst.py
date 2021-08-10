
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class TreeInfo:
	def __init__(self, numberOfNodesVisited, latestVisitedNodeValue):
		self.numberOfNodesVisited = numberOfNodesVisited
		self.latestVisitedNodeValue = latestVisitedNodeValue

# O(h + k) time | O(h) space, where h is the height/depth and k the kth largest element. 
def findKthLargestValueInBst(tree, k):
    # To solve this problem, what we do is to traverse from right - visit - left. And when we reach a visit element we add a counter and 
	# keep track of it's value. We will add +1 every time until counter = k. We create a DS to store the treeInfo value
	treeInfo = TreeInfo(0, -1)
	
	reverseInOrderTraverse(tree, k, treeInfo)
	
	return treeInfo.latestVisitedNodeValue

def reverseInOrderTraverse(node, k, treeInfo):
	# base case, when the node is none or the number of nodes visited is equal to k, we simply return until
	# find Kth largest value, where we return the latest visited node value. 
	if node == None or treeInfo.numberOfNodesVisited >= k:
		return
	
	# reverse in order: right - visited - left
	reverseInOrderTraverse(node.right, k, treeInfo)
	
	if treeInfo.numberOfNodesVisited < k:
		treeInfo.numberOfNodesVisited += 1
		treeInfo.latestVisitedNodeValue = node.value
		
		# if numberOfNodesVisited is less than k, we want to return; but if is equal to k we don't want, we want to inmediately return
		# otherwise it will update the value
		reverseInOrderTraverse(node.left, k, treeInfo)