import unittest

# O(n) time | O(1) space
def isValidSubsequence(array, sequence):
    
    seqIdx = 0;
    
    for i in range(len(array)):
        
        if (seqIdx >= len(sequence)):
            return True
            
        if (sequence[seqIdx] == array[i]):
            seqIdx +=1
    
    # IMPORTANT: Return an assertion whether is true or false the result
    # It is crucial to understand what is the ouput of a member or function
    return seqIdx == len(sequence)

# ---- Unit test

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        array = [5, 1, 22, 25, 6, -1, 8, 10]
        sequence = [1, 6, -1, 10]
        self.assertTrue(isValidSubsequence(array, sequence))

if __name__ == '__main__':
    unittest.main()