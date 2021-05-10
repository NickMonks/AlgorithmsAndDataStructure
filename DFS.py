import unittest

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        graph = Node("A")
        graph.addChild("B").addChild("C").addChild("D")
        graph.children[0].addChild("E").addChild("F")
        graph.children[2].addChild("G").addChild("H")
        graph.children[0].children[1].addChild("I").addChild("J")
        graph.children[2].children[0].addChild("K")
        self.assertEqual(graph.depthFirstSearch([]), ["A", "B", "E", "F", "I", "J", "C", "D", "G", "K", "H"])

# Complexity time: O(V+E)
# Space complexity: O (V)
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        
		# We can solve this DFS algorithm by using a recursive approach.
        # For every child in the Node, we will perform a breahforsearch and append the node
        # every time. 
		
        array.append(self.name)
        for child in self.children:
            child.depthFirstSearch(array)
        return array


if __name__ == '__main__':
    unittest.main()