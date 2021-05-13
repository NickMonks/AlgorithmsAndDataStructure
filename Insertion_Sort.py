import unittest

# O(N^2) Time - O(N) Sorted array | O(1) Space
def insertionSort(array):
	
	# IMPORTANT: We define range to be from 1 since we assume 
	# first element to be "sorted"
	
	# HINT: Whenever we have a complicate for loop + if condition, try to
	# switch it to a while loop. 
	
	for i in range(1,len(array)):
		j = i
		# while the value we're inserting is bigger than 0 (is not a single element)
		# and the element at the end is less than the previous, swap and decrement. 
		# normally the loop will break in j > 0 
		# the j value will be restored in the i loop
		# HINT: if the index of i will be equal to another loop j, just use that index.
		
		while j > 0 and array[j] < array[j-1]:
			swap(j,j-1,array)
			j-=1
			
	return array

# Helper function 
def swap(i,j,array):
	array[i], array[j] = array[j], array[i]
 
 # --- Unit test 


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(insertionSort([8, 5, 2, 9, 5, 6, 3]), [2, 3, 5, 5, 6, 8, 9])
    

if __name__ == '__main__':
    unittest.main()