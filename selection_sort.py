import unittest   
    
# O(1) Space | O(N^2) time - Solution 1
def selectionSort(array):
    for i in range(len(array)-1):
        sortedIdx = i
        for j in range(i+1, len(array)):
            if array[sortedIdx] > array[j]:
                sortedIdx = j
        swap(sortedIdx, i, array)
    return array

# Solution 2 - Using while loops

def swap(i,j,array):
    array[i], array[j] = array[j], array[i]
    
# --- UNIT TESTS
class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(selectionSort([8, 5, 2, 9, 5, 6, 3]), [2, 3, 5, 5, 6, 8, 9])

if __name__=='__main__':
    unittest.main()