# O(j +d) Time and space, because is a DFS at the end
def topologicalSort(jobs, deps):
    # Topological sorts aims to create a topological list where the jobs are connected by satisfying the dependencies
	# Topological sorts need to be a DAG to be completed, otherwise we will have weird dependencies.
	# The first solution is to use DFS approach, where we track the pre-requisities of each nodes (i.e. A->B, A depends on B; B is a pre-requisite on A)
	
	# We will use a class to define the graph:
	jobGraph = createJobGraph(jobs, deps)
	
	# Helper function:
	return getOrderedJobs(jobGraph)

def getOrderedJobs(jobGraph):
	orderedJobs = []
	
	# we store the nodes directly to provide an easy an simple iterator
	nodes = jobGraph.nodes
	
	#DFS approach
	while len(nodes):
		# take the node from the list; this will be our exit condition; when nodes is empty len(nodes) = 0
		node = nodes.pop()
		# pass the orderedJobs list and the node , so it can add it there and track if visited or visiting
		containsCycle = depthFirstTraverse(node, orderedJobs)
		
		if containsCycle:
			return []
		
	return orderedJobs
	
def depthFirstTraverse(node,orderedJobs):
	# here, order matters
	if node.visited:
		return False # if it's false that means we just want to skip it; it wont break the recursive call
	if node.visiting: 
		# we are in a cycle; 
		# TRICK: return true so in the other recursive call we ended there and not just here!
		return True
	
	node.visiting = True
	
	# traverse to all the pre-requisites:
	for prereqNode in node.prereqs:
		containsCycle = depthFirstTraverse(prereqNode, orderedJobs) # we return the containsCycle to break the chain!
		if containsCycle:
			return True
	
	#once finished, we're safe to assume we are at the end and there are no prereqs in the node
	node.visited = True
	node.visiting = False
	orderedJobs.append(node.jobs)
		
def createJobGraph(jobs, deps):
	# initialize graph with: list of JobNodes and a dictionary that maps the the jobNode with a job
	graph = JobGraph(jobs)
	
	# apart from instantiate the graph itself, we need to define the pre-requisites and dependencies of each, i.e add edges node
	# the structure of [[x,y]...] is prereq and the job (oyu can read this either y is a dependency of x, or x is a pre-requisite of y!)
	for prereq, job in deps:
		#add a prereq in the job seen 
		graph.addPrereq(job, prereq)
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
	
	def addPrereq(self, job, prereq):
		# get the node from job; get the node that reference to the prereq and simply append the latter to the job prereq field. 
		jobNode = self.getNode(job)
		prereqNode = self.getNode(prereq)
		jobNode.prereqs.append(prereqNode)
	
	def getNode(self, job):
		if job not in self.graph:
			self.addNode(job)
			
		# the method simply serves a lookup dictionary
		# and returns a JobNode object
		return self.graph[job]

class JobNode:
	def __init__(self, job):
		self.jobs = job
		self.prereqs = []
		# we will track also if the node is visited & completed (visited) or if is in progress (visiting)
		self.visited = False
		self.visiting = False