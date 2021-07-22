import unittest

# Time complexity: O(N^2 * ((2*N)!/((N+1)!*N!))) | space: O(N^2 * ((2*N)!/((N+1)!*N!))) 
def generateDivTags(numberOfTags):
	# To solve this problem, we use recursion since another approach that involve use all posible combinations of strings
	# So, we use recursion and we will use two properties: 1) you can have as many open tags <div> as you want and 2) if the number of
	# open tags is less than close, we can add a closing tag </div> 3) once we have zero open tags, we need to close. With that, we can
	# do a recursive formula, where the base case is that the closing tag left is zero (i.e we have a valid string)
	matchedDivTags = []
	generateDivTagsFromPrefix(numberOfTags,numberOfTags, "", matchedDivTags)
	return matchedDivTags
	
def generateDivTagsFromPrefix(openingTagsNeeded, closingTagsNeeded, prefix, result):
	if openingTagsNeeded > 0:
		newPrefix = prefix + "<div>"
		
		# recursively call the function with the new prefix and one less opening tag
		generateDivTagsFromPrefix(openingTagsNeeded-1,closingTagsNeeded, newPrefix, result)
	
	if openingTagsNeeded < closingTagsNeeded:
		newPrefix = prefix + "</div>"
		generateDivTagsFromPrefix(openingTagsNeeded,closingTagsNeeded-1, newPrefix, result)

	#Base case
	if closingTagsNeeded == 0:
		result.append(prefix)


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = 3
        expected = [
            "<div><div><div></div></div></div>",
            "<div><div></div><div></div></div>",
            "<div><div></div></div><div></div>",
            "<div></div><div><div></div></div>",
            "<div></div><div></div><div></div>",
        ]
        actual = generateDivTags(input)
        self.assertEqual(actual, expected)

if __name__=="__main__":
    unittest.main()