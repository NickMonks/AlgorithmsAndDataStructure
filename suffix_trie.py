import unittest

class SuffixTrie:
    def __init__(self, string):
        self.root = {} # python dictionary / hash table
        self.endSymbol = "*"
        self.populateSuffixTrieFrom(string)
    
    # O(n^2) time | O(n^2) space
    def populateSuffixTrieFrom(self, string):
        # To build a suffix trie, we iterate through every character
        # of the suffix trie 	
        for i in range(len(string)):
            self.insertSubstringStartingAt(i,string)
    
    def insertSubstringStartingAt(self, index, string):
        # checks if a character is already stored or not in the tree and everything
        # we will always start at the root node
        node = self.root
        
        # iterate every character in our substring STARTING FROM INDEX
        for j in range(index, len(string)):
            letter = string[j]
            
            # check if letter exists or not
            # In python, you can check a key just by doing this
            if letter not in node:
                # if not in node, create "a": {} , which will contain another dictionary inside
                node[letter] = {}
            
            # then, we update the node to be the inserted one (if it exists, it will access to it anyway)
            node = node[letter]
            
        # When we ended the suffix trie, we want to add an asterisk
        # since we have defined it as a property, we set a boolean to be true
        node[self.endSymbol] = True
    
    # O(M) time | O(1) space
    def contains(self, string):
        node = self.root
        
        for letter in string:
            if letter not in node:
                return False
            node = node[letter]
        
        # check if the end of the suffix trie
        # as in many examples in python, we return the assertion of whether
        # self.endSymbol is true in node
        return self.endSymbol in node


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        trie = SuffixTrie("babc")
        expected = {
            "c": {"*": True},
            "b": {"c": {"*": True}, "a": {"b": {"c": {"*": True}}}},
            "a": {"b": {"c": {"*": True}}},
        }
        self.assertEqual(trie.root, expected)
        self.assertTrue(trie.contains("abc"))

if __name__ == "__main__":
    unittest.main()