import unittest

# O(n) time | O(n) space
def maxSubsetSumNoAdjacent(array):
    if not len(array):
        return 0
    elif len(array)==1:
        return array[0]
    
    # First, we build an auxiliar array which will store each maxsum
    # value, from left to right (IMPORTANT! IF YOU CANT SOLVE FROM LEFT TO RIGHT, taking the elements from right to left)
    
    maxSums = array[:]
    maxSums[1] = max(array[0], array[1])
    
    for i in range(2, len(array)):
        maxSums[i] = max(maxSums[i-1], maxSums[i-2]+ array[i])
    
    # to return last value in python, use "-1 " index
    return maxSums[-1]


# --- USING MEMOIZATION
# O(n) time | O(n) space
def maxSubsetSumNoAdjacent(array):
    if not len(array):
        return 0
    elif len(array)==1:
        return array[0]
    
    # First, we build an auxiliar array which will store each maxsum
    # value, from left to right (IMPORTANT! IF YOU CANT SOLVE FROM LEFT TO RIGHT, taking the elements from right to left)
    
    second = array[0]
    first = max(array[0], array[1])
    
    for i in range(2, len(array)):
        current = max(first, second + array[i])
        second = first
        first = current
    
    return first

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(maxSubsetSumNoAdjacent([75, 105, 120, 75, 90, 135]), 330)

if __name__ == "__main__":
    unittest.main()