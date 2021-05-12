# O(n) time | O(1) space
def isPalindrome(string):
    leftIdx = 0
    rightIdx = len(string)-1
    
    
    while string[leftIdx] == string[rightIdx]:
        
        if rightIdx <= leftIdx:
            return True
        
        leftIdx += 1
        rightIdx -=1
    return False

# --- Unit test

import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(isPalindrome("abcdcba"), True)


if __name__ == '__main__':
    unittest.main()