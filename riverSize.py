import unittest

def riverSizes(matrix):
    	# Since this would be likely a graph problem, we will
	# visit each node of the graph with either BFS or DFS algorithm.
	# Each node has 4 neighbours: if the node is zero, or if already beign visited,
	# return the recursive function.
	# Therefore, in this problem (AND MANY OTHER FROM GRAPH) we should use the visitor pattern
	# where we visit each node and marked as True. This can be implemented with an auxiliar array
	# or better as a hash table. 
	
	sizes = []
	# then we initialize a visited matrix, which in our case is just a matrix of boolean for each node
	visited = [[False for value in row] for row in matrix]
	
	# TIP: how to traverse a matrix 
	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			# If we already visited the node, just continue
			if visited[i][j]:
				continue
			# if not, we call a helper function to traverse the nodes:
			traverseNode(i,j,matrix,visited,sizes)
	return sizes

def traverseNode(i,j,matrix,visited,sizes):
	# potentially a new river
	currentRiverSize = 0;
	
	# DFS:
	# we solve this iteratively. How?
	# we treat the nodes to be explored as a stack. when we visit one we pop it
	# this will be in a while - stack structure
	nodesToExplore = [[i,j]]
	while len(nodesToExplore):
		currentNode = nodesToExplore.pop()
		i = currentNode[0]
		j = currentNode[1]
		
		# if already visited, skip it:
		if visited[i][j]:
			continue
		visited[i][j] = True
		
		# if the node is a cero, i.e. land, skip it
		# and not looking the neighbours
		if matrix[i][j]==0:
			continue
		
		# the node is a river and not visited:
		# update river size and add the nodes to explore!
		currentRiverSize+=1
		unvisitiedNeighbours = getUnvisitedNeighbours(i,j,matrix, visited)
		
		for neighbour in unvisitiedNeighbours:
			nodesToExplore.append(neighbour)
	
	if currentRiverSize > 0:
		sizes.append(currentRiverSize)


def getUnvisitedNeighbours(i,j,matrix, visited):
	unvisitedNeighbours = []
	
	# check node below - AND we're not in the upmost part (i=0)
	if i >0 and not visited[i-1][j]:
		unvisitedNeighbours.append([i-1, j])
	
	# check node above- AND we're not in the bottom part (matrix-1)
	if i < len(matrix) - 1 and not visited[i+1][j]:
		unvisitedNeighbours.append([i+1, j])
		
	if j > 0 and not visited[i][j-1]:
		unvisitedNeighbours.append([i, j-1])
	
	if j < len(matrix[0]) - 1 and not visited[i][j+1]:
		unvisitedNeighbours.append([i, j+1])
	
	return unvisitedNeighbours

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        testInput = [[1, 0, 0, 1, 0], [1, 0, 1, 0, 0], [0, 0, 1, 0, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 0]]
        expected = [1, 2, 2, 2, 5]
        self.assertEqual(sorted(riverSizes(testInput)), expected)

if __name__ == "__main__":
    unittest.main()