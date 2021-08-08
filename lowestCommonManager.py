import unittest

def getLowestCommonManager(topManager, reportOne, reportTwo):
    # To solve this problem, we need to understand a key thing: when we point to a node or a manager, and we start from the bottom,
	# if that manager counts 2 of the managers, is the lowest common manager. Imagine we have a tree as the notebook;
	# if we recursively do a for loop for all the directReports and then, once we get a base case (no reports), verify if it's a report type
	# if yes return 1, if not return 0. Once all the direct reports of the manager have been counted, we will check if we got 2 (IMPORTANT: 
	# we need to count the CURRENT MANAGER! also), if yes then we simply return that node; if not, this will recursively return the number of reports
	# of that subtree
	
	return getOrgInfo(topManager, reportOne, reportTwo).lowestCommonManager
	
def getOrgInfo(manager, reportOne, reportTwo):
	# initialize variables
	numImportantReports = 0
	
	# for each directReport we recursively check all potential reports 
	for directReport in manager.directReports:
		# It is important to note that we create a variable for the return type, which we need to keep track
		# it will return the orgInfo value
		orgInfo = getOrgInfo(directReport, reportOne, reportTwo)

		#once the recursive call ends up, we need to verify if a) the orgInfo has already a commonManager 
		# if it exists, just return the orgInfo; it will recursively assign the return to orgInfo over and over
		if orgInfo.lowestCommonManager is not None:
			return orgInfo
		
		# if not, we sum the numImportantReports for that subtree; if we have any, we want to accumulate it!
		numImportantReports += orgInfo.numImportantReports
	
	# This is an important step; we need to check if the manager (or root) of the subtree is a importantreport
	# AND this is, in fact, the base case!, because if we are a leaf and we dont enter in the for loop we will end here anyway
	if manager == reportOne or manager == reportTwo:
		numImportantReports +=1
	
	# Finally, check if we are a lowestCommonManager if we got 2 reports; if not, then return none
	lowestCommonManager = manager if numImportantReports == 2 else None
	return OrgInfo(lowestCommonManager, numImportantReports)
	
# use a class as a data structure
class OrgInfo:
	def __init__(self, lowestCommonManager, numImportantReports):
		self.lowestCommonManager = lowestCommonManager
		self.numImportantReports = numImportantReports

class OrgChart:
    def __init__(self, name):
        self.name = name
        self.directReports = []

ALPHABET = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")


def getOrgCharts():
    orgCharts = {}
    for letter in ALPHABET:
        orgCharts[letter] = OrgChart(letter)
    return orgCharts

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        orgCharts = getOrgCharts()
        orgCharts["A"].addDirectReports([orgCharts["B"], orgCharts["C"]])
        orgCharts["B"].addDirectReports([orgCharts["D"], orgCharts["E"]])
        orgCharts["C"].addDirectReports([orgCharts["F"], orgCharts["G"]])
        orgCharts["D"].addDirectReports([orgCharts["H"], orgCharts["I"]])

        lcm = getLowestCommonManager(orgCharts["A"], orgCharts["E"], orgCharts["I"])
        self.assertEqual(lcm.name, "B")

if __name__ == "__main__":
    unittest.main();