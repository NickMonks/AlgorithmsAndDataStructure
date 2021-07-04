import unittest

# O(V^2 + E) Time | O(V) Space
def dijkstrasAlgorithm(start, edges):
    # Unoptimal solution: using Array instead of a min heap
	# Our input will be the adjacency list, alled "edges", the length of this adjacency list is the #nodes
	# [
	# 0 [],
	# 1 [],
	# ...
	#
	# ]
	
	numberOfVertices = len(edges)
	# initialise all distances (unknow) as infinity, and initialise the first value as 0,
	# which is the min distances (the entire row in the notebook notes)
	minDistances = [float("inf") for _ in range(numberOfVertices)]
	minDistances[start] = 0
	
	# unordered list of set, we don't care the order (want we will do is put the nodes visited here)
	visited = set()
	
	# when we visited all vertices we found all vertices
	while len(visited) != numberOfVertices:
		# array will take at least O(V^2 + E) time
		
		# for each vertex/node (first row), we will obtain the minimum current distance 
		#(for each row/vertex, obtain the column value), and start with it. If we don't do it, we wont know 
		# if it's indeed the shortest path!
		# e.g {0,1,4}... we find the smallest between the node
		vertex, currentMinDistance = getVertexWithMinDistance(minDistances, visited)
		
		# if the distance is infinity, that means we can't reach it (it will actually return it in the end, when other vertex have been returned)
		# so we just simply break the while loop ahead of time. 
		if currentMinDistance == float('inf'):
			break
		
		# Once this node is visited, we mark it as visited (so we don't try to re-visit it)
		visited.add(vertex)
		
		# we will traverse a list of all edges for the vertex of interest; notice the edges are a pair of values
		# where the first element if the node and the second is the distance/weight
		for edge in edges[vertex]:
			destination, distanceToDestination = edge
			
			# If the destination is already visited, then ignore it; we wont find a better path because we actually already visited it
			if destination in visited:
				continue
			
			# once found, we calculate the path distance between current min distance (previous row) with the edge weight
			newPathDistance = currentMinDistance + distanceToDestination
			currentDestinationDistance = minDistances[destination]
			
			# we compare both of them; if it's less than the previous distance, we update it. 
			if newPathDistance < currentDestinationDistance:
				minDistances[destination] = newPathDistance
			
	
	# Before returning, we need to push a -1 to the vertex that have a infinity distance, to mark them as unreachable:
	# WE USE A MAP FUNCTION FOR THIS, REVIEW FUNCTIONAL PROGRAMMING 
	return list(map(lambda x: -1 if x== float("inf") else x, minDistances))
	
	
def getVertexWithMinDistance(distances, visited):

	# initialise variables
	currentMinDistance = float("inf")
	vertex = -1

	# for each distances element (which is the the row), we will get the index (vertex), and value (distance)
	# then, we will check which has the MINIMUM DISTANCE (first part of the algorithm; we will first check the nodes with minimum distance)
	for vertexIdx, distance in enumerate(distances):
		if vertexIdx in visited:
			# If it's visited, that means the shortest path is already found, so we ignore it
			continue
		# if any of the distance (the value) is less than currentValue, update the minDistance 
		if distance <= currentMinDistance:
			vertex = vertexIdx
			currentMinDistance = distance

	return vertex, currentMinDistance

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        start = 0
        edges = [[[1, 7]], [[2, 6], [3, 20], [4, 3]], [[3, 14]], [[4, 2]], [], []]
        expected = [0, 7, 13, 27, 10, -1]
        actual = dijkstrasAlgorithm(start, edges)
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()