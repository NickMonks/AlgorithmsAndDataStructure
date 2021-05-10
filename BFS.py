import unittest

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        graph = program.Node("A")
        graph.addChild("B").addChild("C").addChild("D")
        graph.children[0].addChild("E").addChild("F")
        graph.children[2].addChild("G").addChild("H")
        graph.children[0].children[1].addChild("I").addChild("J")
        graph.children[2].children[0].addChild("K")
        self.assertEqual(graph.breadthFirstSearch([]), ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"])


class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    # Time: O (v + e) | space: O (v)
    def breadthFirstSearch(self, array):
        #initialize our queue:
		# IMPORTANT to initialize with the first node, which is the root 
        # and which allocates the object
	    queue = [self]
		
		# Adv. : for knowing is queue is/not empty, just check the length
	    while len(queue) > 0:
			# when we pop in Python, we return the actual object. 
		    currentNode = queue.pop(0)
		    array.append(currentNode.name)
            # for every child in the queue element, we will append it 
		    for child in currentNode.children:
		    	queue.append(child)
	    return array
 
if __name__ == '__main__':
    unittest.main()