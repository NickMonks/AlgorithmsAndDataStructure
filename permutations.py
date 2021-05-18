import unittest

# Upper bound: O(N^2 * N!) Time | O(N*N!) space
def getPermutations(array):
	permutations = []
	permutationsHelper(array,[], permutations)
	return permutations

def permutationsHelper(array, currentPermutation, permutations):
	
	# Base case
	if not len(array) and len(currentPermutation):
		# A good trick to define if an array is empty in Python
		permutations.append(currentPermutation)
	
	else:
		# Recursive Case
		for i in range(len(array)):
			# REVIEW SLICING !
			# We are concatenating two arrays without the element i
			# E.g [1,2,3] -> we take [2,3]
			# then , we concatenate our currentPermutation with 
			# the element that we did NOT include before. Eg. [1]
			
			newArray = array[:i] + array[i + 1:]
			newPermutation = currentPermutation + [array[i]]
			
			# then, we pass our new array and our new permutation
			permutationsHelper(newArray, newPermutation, permutations)
			
			'''
			To visualise this better:
			
			- 1st call, i = 0: newPerm = [1], newArray = [2,3] -> helper([2,3], [1])
				- 2nd call, i = 0: [1,2], [3] -> helper([3],[1,2])
					- 3rd call, i = 0: [1,2,3], [0] -> helper(null, [1,2,3])
					APPEND PERMUTATION
					- 3rd call : END -> Return 2nd call
				- 2nd call, i = 1: perm [1,3], newArray = [2] 
				.....
			'''
def getPermutations_2(array):
    permutations = []
    permutationsHelper_2(0, array, permutations)
    return permutations

def permutationsHelper_2(i, array, permutations):
    # Check if we are at the end of our array
    # i is the index
    if i == len(array) -1:
        # Append array elements with the ":" operator
        permutations.append(array[:])
    else:
        # swap all the numbers with the number of our current position
        # for every index j in (i, end)
        for j in range(i, len(array)):
            # in this first iteration , j == i
            # so the first time we wont swap anything... until last permutation appends!
            # tthen after that snapshot (the 2nd swap wont be called neither), we change j
            
            # so j == i +1 
            swap(i,j, array)
            # we swap i->j and pass the array to the method
            permutationsHelper(i+1, array, permutations)
            # we un-swap the value of the iteration so the next permutation has a clean slate
            swap(i, j, array)
    
def swap(i,j, array):
    array[i], array[j] = array[j], array[i]

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        perms = getPermutations([1, 2, 3])
        self.assertTrue(len(perms) == 6)
        self.assertTrue([1, 2, 3] in perms)
        self.assertTrue([1, 3, 2] in perms)
        self.assertTrue([2, 1, 3] in perms)
        self.assertTrue([2, 3, 1] in perms)
        self.assertTrue([3, 1, 2] in perms)
        self.assertTrue([3, 2, 1] in perms)

if __name__=='__main__':
    unittest.main()