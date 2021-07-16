# O(j +d) Time and space
def topologicalSort(jobs, deps):

	# We will use a class to define the graph:
	jobGraph = createJobGraph(jobs, deps)
	
	# Helper function:
	return getOrderedJobs(jobGraph)

def getOrderedJobs(jobGraph):
	orderedJobs = []
	
	# In this case, we need to take the nodes with NO prereqs
	nodesWithNoPrereqs = list(filter(lambda node: node.numbOfPrereqs == 0, jobGraph.nodes))
	
	# so long as we have a list with elements of no prereqs, we append it directly to ordered jobs,
	# AND remove the deps
	while len(nodesWithNoPrereqs):
		node = nodesWithNoPrereqs.pop()
		orderedJobs.append(node.jobs)
		removeDeps(node, nodesWithNoPrereqs)
	
	# here, we know for a fact that we will have at least one node where the num of dependecies is zero
	# therefore if any of the nodes have a truthy value, return 
	graphHasEdges = any(node.numbOfPrereqs for node in jobGraph.nodes)
	return [] if graphHasEdges else orderedJobs

def removeDeps(node, nodesWithNoPrereqs):
	# remove the deps of the current node, since we are deleting it
	while len(node.deps):
		dep = node.deps.pop() # same technique; we pop the deps and do -1 to all of them until finished
		dep.numbOfPrereqs -= 1
		if dep.numbOfPrereqs == 0:
			nodesWithNoPrereqs.append(dep)
		
def createJobGraph(jobs, deps):
	# initialize graph with: list of JobNodes and a dictionary that maps the the jobNode with a job
	graph = JobGraph(jobs)
	
	# (x,y) -> y depends on x, so we use this approach now, and using the addDep the pre-reqs of x is +1
	for job, deps in deps:
		#add a prereq in the job seen 
		graph.addDep(job, deps)
	return graph
	
class JobGraph:
	# IMPORTANT: Job is the element itself; the Node contains more info, such as prereqs, if visited or not, etc.
	def __init__(self,jobs):
		self.nodes = [] # will contain the graph itself, with the edges and dependencies
		self.graph = {} # will map values to other values, map jobs to their nodes
		
		# basically graph lists {1: <JobNode 1>, 2: <JobNode 2>,...} and node=[<JobNode 1>, <JobNode 2>...]
		
		for job in jobs:
			# for each job [1,2,...] we will add the nodes , which contains the info of the job and pre-requisites
			# from a JobNode object. 
			self.addNode(job)
	
	def addNode(self, job):
		
		self.graph[job] = JobNode(job)
		self.nodes.append(self.graph[job])
	
	def addDep(self, job, dep):
		# get the node from job; get the node that reference to the prereq and simply append the latter to the job prereq field. 
		jobNode = self.getNode(job)
		depNode = self.getNode(dep)
		jobNode.deps.append(depNode)
		# include the new prereq number
		depNode.numbOfPrereqs += 1
	
	def getNode(self, job):
		if job not in self.graph:
			self.addNode(job)
			
		# the method simply serves a lookup dictionary
		# and returns a JobNode object
		return self.graph[job]

class JobNode:
	def __init__(self, job):
		self.jobs = job
		# now, we use dependencies instead of pre-reqs (is an inversion of what we had before)
		self.deps = []
		# we define the number of pre-reqs of the current Node
		self.numbOfPrereqs = 0
		