# O(nm) time | O(nm) space
def levenshteinDistance(str1, str2):
	# the "+1" corresponds to empty array element
	edits = [[x for x in range(len(str1)+1)] for y in range(len(str2)+1)]
	# [0,1,2,3,...]
	# 1
	# 2
	# 3
	# ...
	
	for i in range(1, len(str2)+1):
		#first row, we will basically add 1 to each element
		edits[i][0] = edits[i-1][0]+1
		
	for i in range(1, len(str2)+1):
		for j in range(1,len(str1)+1):
			# Apply levenshtein distance formula
			if str2[i-1] == str1[j-1]:
				edits[i][j] = edits[i-1][j-1]
			else:
				edits[i][j]=1+min(edits[i-1][j-1], edits[i][j-1], edits[i-1][j])
	
	# REMEMBER: PYTHON RETURNS LAST ELEMENT WITH -1!
	return edits[-1][-1]