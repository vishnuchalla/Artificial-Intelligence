import sys

"""
Class that defines a node structure.
"""
class Node:
	"""
	Constructor to initialize all the parameters while scanning a node from input.

	type: variable to indicate type of node
	name: name of the node
	childNodes: stores a list of child nodes
	value: value in the node
	"""
	def __init__(self, type, name, childNodes, value):
		self.number = None
		self.type = type
		self.name = name
		self.parent = None
		self.childNodes = childNodes
		self.choice = None
		self.value = value

	"""
	Method for debugging purposes.
	"""
	def __str__(self):
		return "number: %s, type: %s, name: %s, parent: %s, childNodes: %s, choice: %s, value: %s" % (self.number, self.type, self.name, self.parent, self.childNodes, self.choice, self.value)

"""
Method to perform DFS for the given graph input.

mapOfNodes: map of nodes as an input
returns the nodes expanded and the path trace for caluculating values of each node
"""
def performDFS(mapOfNodes):
	startNode = mapOfNodes['Start']
	nodeNumber = 1
	stack = [startNode]
	nodesExpanded = []
	mapOfNodesWithIndices = dict()

	while len(stack) > 0:
		currentNode = stack.pop()
		currentNode.number = nodeNumber
		nodeNumber += 1
		mapOfNodesWithIndices[currentNode.number] = currentNode
		nodesExpanded.append(currentNode.number)
		if currentNode.type == 'outcome':
			continue
		childNodes = currentNode.childNodes
		for eachChildNode in childNodes:
			if currentNode.type == 'choice':
				childNode = mapOfNodes[eachChildNode[1]]
			else:
				childNode = mapOfNodes[eachChildNode[2]]
			childNode.parent = currentNode.name
			stack.append(childNode)

	return nodesExpanded, mapOfNodesWithIndices

"""
Method to log nodes added into the decision tree.

nodesExpanded: nodes expanded from the input file
mapOfNodesWithIndices: map of the nodes with their unique indices.
"""
def logNodeAddition(nodesExpanded, mapOfNodesWithIndices):
	for eachNode in nodesExpanded:
		nodeDetails = mapOfNodesWithIndices[eachNode]
		print('Adding Node ' + str(eachNode) + ' ' + nodeDetails.type + ' ' + nodeDetails.name + ' ' + str(nodeDetails.parent))

"""
Method to log lottery nodes in the decision tree.

nodeDetails: node and its details
mapOfNodes: mapping of the nodes
nodeNumber: node number to log
"""
def logLotteryNode(nodeDetails, mapOfNodes, nodeNumber):
	sum = 0
	for eachChild in nodeDetails.childNodes:
		sum += float(eachChild[1]) * float(mapOfNodes[eachChild[2]].value)
	nodeDetails.value = str(sum)
	print('Expected Value Node:' + str(nodeNumber) + ', ' + nodeDetails.name + ' ' + nodeDetails.value)

"""
Method to log decision nodes in the decision tree.

nodeDetails: node and its details
mapOfNodes: mapping of the nodes
nodeNumber: node number to log
"""
def logDecisionNode(nodeDetails, mapOfNodes, nodeNumber):
	maxNum = float('-inf')
	choice = ''
	for eachChild in nodeDetails.childNodes:
		newMax = float(mapOfNodes[eachChild[1]].value)
		if maxNum < newMax:
			maxNum = newMax
			choice = eachChild[0]
	nodeDetails.value = str(maxNum)
	nodeDetails.choice = choice
	print('Decision Node:' + str(nodeNumber) + ', ' + nodeDetails.name + ' ' + nodeDetails.choice + ' ' + nodeDetails.value)


"""
Method to log nodes caculated while backtracking the dfs order.

nodesExpanded: nodes expanded from the input file
mapOfNodesWithIndices: map of the nodes with their unique indices.
mapOfNodes: map of nodes with node name as a key.
"""
def logNodeCalculation(nodesExpanded, mapOfNodesWithIndices, mapOfNodes):
	for eachNode in reversed(nodesExpanded):
		nodeDetails = mapOfNodesWithIndices[eachNode]
		if nodeDetails.type == 'lottery':
			logLotteryNode(nodeDetails, mapOfNodes, eachNode)
		elif nodeDetails.type == 'choice':
			logDecisionNode(nodeDetails, mapOfNodes, eachNode)

"""
Method to scan input file and perform operations on decision tree.
"""
def executeDecisionTree():
	with open(sys.argv[1], 'r') as inputFile:
		inputLines = inputFile.readlines()
	inputFile.close()
	removedEscapedChars = [each.strip() for each in inputLines]
	filteredLines = [each for each in removedEscapedChars if each != '']
	mapOfNodes = dict()
	eachIndex = 0
	while eachIndex < len(filteredLines):
		value = filteredLines[eachIndex]
		if 'CHOICE:' in value:
			nodeName = value.split()[1]
			eachIndex += 1
			childNodes = []
			while 'ENDCHOICE' not in filteredLines[eachIndex]:
				childValue = filteredLines[eachIndex]
				childNode = childValue.split()
				childName, childValue = childNode[1:3]
				childNodes.append((childName, childValue))
				eachIndex += 1
			nodeObject = Node('choice', nodeName, childNodes, None)
			mapOfNodes[nodeName] = nodeObject
		elif 'LOTTERY:' in value:
			nodeName = value.split()[1]
			eachIndex += 1
			childNodes = []
			while 'ENDLOTTERY' not in filteredLines[eachIndex]:
				childValue = filteredLines[eachIndex]
				childNode = childValue.split()
				childName, occuranceProbability, childValue = childNode[1:4]
				childNodes.append((childName, occuranceProbability, childValue))
				eachIndex += 1
			nodeObject = Node('lottery', nodeName, childNodes, None)
			mapOfNodes[nodeName] = nodeObject
		elif 'OUTCOME:' in value:
			nodeName, nodeValue = value.split()[1:3]
			nodeObject = Node('outcome', nodeName, None, nodeValue)
			mapOfNodes[nodeName] = nodeObject
		eachIndex += 1

	nodesExpanded, mapOfNodesWithIndices = performDFS(mapOfNodes)

	print()
	print("Nodes while building the decision tree:")
	print()
	logNodeAddition(nodesExpanded, mapOfNodesWithIndices)
	print()
	print("Nodes while updating the decision tree:")
	print()
	logNodeCalculation(nodesExpanded, mapOfNodesWithIndices, mapOfNodes)

"""
Main method to initiate the process.
"""
if __name__ == '__main__':
	executeDecisionTree()
