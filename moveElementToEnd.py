import unittest

def moveElementToEnd(array, toMove):
    # use of two pointers; one at the end, j, and another at the beginning, i
	# j is len(array) -1 because [0,...,n] -> len(array) = n +1 -> array[n] !!Outbound exception
	i = 0
	j = len(array)-1
	
	while i < j:
		# CAREFUL! we want to keep moving j until finding a diferent number of toMove
		# an if statement is not enough; we need to ensure array[j] is inot toMove
        # why using i < j??? : because we are looping on the end until finding a different number of toMove, if
        # we don't encounter it we want to ensure it will break the loop! (i.e. imagine we are looping 2's until j=i... if we dont put this
        # condition it will loop over and surpass i and keep swaping)
		while i < j and array[j] == toMove:
			j-=1
		if array[i] == toMove:
			array[i], array[j] = array[j], array[i]
		# you want to add +1 either way if we didnt swap it, since it means is not toMove so we can progress
		# Otherwise, we swap it AND add the +1
		i += 1
	
	return array

class TestmoveElementToEnd(unittest.TestCase):
    def test_case(self):
        # given
        array = [2,1,2,2,2,3,4,2]
        toMove = 2
        
        #when
        expectedStart = [1, 3, 4]
        expectedEnd = [2, 2, 2, 2, 2]
        output = moveElementToEnd(array, toMove)
        outputStart = sorted(output[0:3])
        outputEnd = output[3:]
        self.assertEqual(outputStart, expectedStart)
        self.assertEqual(outputEnd, expectedEnd)

if __name__ == "__main__":
    unittest.main()