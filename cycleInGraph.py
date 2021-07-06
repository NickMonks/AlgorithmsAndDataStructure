import unittest

# METHOD 1: DFS
def cycleInGraph(edges):
    	
	# Number of vertices 
	numberOfNodes = len(edges)
	
	# we initialise two data structure: visited (mark as visit nodes) and instack (to check if)
	# a node is in the recursive stack. this will allow us to check whether we have a back edge, a tree edge, cross edge or forward edge
	
	visited = [False for _ in range(numberOfNodes)]
	currentlyInStack = [False for _ in range(numberOfNodes)]
	
	# we check if the node is in the stack or not. We have this for loop to make sure we run for every node
	# even if the DFS will do it itself; imagine if we had two graphs for example. 
	for node in range(numberOfNodes):
		if visited[node]:
			continue
		
		# if not visited, we'll perform a depth first search; this function will return true or false
		# to know if we have a cycle
		containsCycle = isNodeInCycle(edges, node, visited, currentlyInStack)
		
		if containsCycle:
			return True
		
	# if not return false	
	return False


def isNodeInCycle(edges,node,visited, currentlyInStack):
	
	# First step, we need to mark as visited and in stack
	visited[node] = True
	currentlyInStack[node] = True
	
	#we check every neighbour/child of that node
	neighbors = edges[node]
	for neighbor in neighbors:
		
		# if it's visited, that means we want to check if is the stack. If not, then just continue 
		# we don't want to recurse on the same node visited again. 
		if not visited[neighbor]:
			
			# recursively call the same function using DFS
			containsCycle = isNodeInCycle(edges, neighbor, visited, currentlyInStack)
			
			# if we get the condition from visited AND currentlyInStack to be true, then it will
			# recursively return true again and again. 
			if containsCycle:
				return True
		elif currentlyInStack[neighbor]:
			return True
	
	# Once the function as returned and we can't find any children, mark as false:
	currentlyInStack[node] = False
 
 # method 2: AVL-like solution
 
WHITE, GREY, BLACK = 0,1,2
 
def cycleInGraph2(edges):
    numberOfNodes = len(edges)
    colors = [WHITE for _ in range(numberOfNodes)]
    
    for node in range(numberOfNodes):
        if colors[node] != WHITE:
            continue
        
        containsCycle = traverseAndColorNodes(node, edges, colors)
        
        if containsCycle:
            return True
    return False


def traverseAndColorNodes2(node, edges, colors):
    colors[node] = GREY
    
    neighbors = edges[node]
    for neighbor in neighbors:
        neighborColor = colors[neighbor]
        
        if neighborColor == GREY:
            return True
        
        # If is not White, it means is BLACK, so continue and ignore it 
        if neighborColor != WHITE:
            continue
        
        containsCycle = traverseAndColorNodes(neighbor, edges, colors)
        
        if containsCycle:
            return True
    
    # We mark as black the visited and out of the stack as black
    colors[node] = BLACK
    return False

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = [[1, 3], [2, 3, 4], [0], [], [2, 5], []]
        expected = True
        actual = cycleInGraph(input)
        self.assertEqual(actual, expected)
        
if __name__== "__main__":
    unittest.main()