import unittest

# O(n) Time | O(n) Space
def sunsetViews(buildings, direction):
    # There are two solutions optimals: the first is to go to the OPPOSITE direction on where the sun sets.
	# If we do this, we can track the maximum height of the building; if the maximum height is less than our 
	# current, that means we can se the sun so we add it in our sunset list. else, is blocking and we skip it
	
	buildingsWithSunsetViews = []
	
	# If sunset starts in the west, the beam is going L->R, so we start at 0; otherwise start at index len(building) -1
	startIdx = 0 if direction == "WEST" else len(buildings) -1
	
	step = 1 if direction == "WEST" else -1
	
	idx = startIdx
	runningMaxHeight = 0 # no negative values, so this is ok
	
	# because we can be running this either LR or RL, we set the boundaries
	while idx >= 0 and idx < len(buildings):
		buildingHeight = buildings[idx]
		
		if buildingHeight > runningMaxHeight:
			buildingsWithSunsetViews.append(idx)
		
		# compare current building with maxheight
		runningMaxHeight = max(runningMaxHeight, buildingHeight)
		
		#increment our counter by the step:
		idx+=step
	
	# finally, in case the sunset is in the EAST, that means the array is reversed; so we reverse it (either way this is O(n) so is fine)
	if direction == "EAST":
		return buildingsWithSunsetViews[::-1]
	return buildingsWithSunsetViews

# O(n) Time | O(n) Space
def sunsetViews2(buildings, direction):
    # this solution uses a stack (LIFO structure), that basically stores the array height and check if any 
	# of the buildings are smaller or equal to this one; if it is, then pop the values iteratively until finding a bigger one,
	# then push the building. If is smaller, then put it in the stack.
	
	candidateBuildings = []
	
	startIdx = 0 if direction == "EAST" else len(buildings) -1 
	step = 1 if direction == "EAST" else -1
	
	idx = startIdx
	while idx >=0 and idx < len(buildings):
		buildingHeight = buildings[idx]
		
		# use a while loop to pop values at the stack. We check first if the candidate list contains
		# any elements AND then we check the last element of the buildings list and see if is less than the current building
		while len(candidateBuildings) > 0 and buildings[candidateBuildings[-1]] <= buildingHeight:
			candidateBuildings.pop()
		# Once finish to pop all buildings, we append
		candidateBuildings.append(idx)
		
		# increase index
		idx += step
		
	# correct order of the stack
	if direction == "WEST":
		return candidateBuildings[::-1]
	return candidateBuildings

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        buildings = [3,5,4,4,3,1,3,2]
        direction = "EAST"
        expected = [1,3,6,7]
        actual_1= sunsetViews(buildings, direction)
        self.assertEqual(actual_1, expected)
    
    def test_case_2(self):
        buildings = [3,5,4,4,3,1,3,2]
        direction = "EAST"
        expected = [1,3,6,7]
        actual_2= sunsetViews2(buildings, direction)
        self.assertEqual(actual_2, expected)

if __name__ == "__main__":
    unittest.main()
        