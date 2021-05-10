import unittest

# O(n^2) time | O (1) Space
def bubbleSort(array):
    isSorted = False # this boolean will track whether the array is or not sorted
    counter = 0 # since we now the biggest value will be sorted at the end, we can reduce the size of the for loop
    while not isSorted:
        isSorted = True
        for i in range(len(array)-1-counter):
            if array[i] > array[i+1]:
                swap(i, i+1, array)
                isSorted = False # it's better not to put the isSorted in an else
            
            # when the for loop is finish, we increment the counter
        counter +=1
    return array

def swap(i,j, array):
    array[i], array[j] = array[j], array[i]
    
# ----- UNIT TEST

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(bubbleSort([8, 5, 2, 9, 5, 6, 3]), [2, 3, 5, 5, 6, 8, 9])

if __name__ == '__main__':
    unittest.main()