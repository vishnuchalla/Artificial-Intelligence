import sys
import csv

"""
Class to create a Node with all the required attributes.
"""
class Node:
	"""
	Init method to create a node.

	rowIndex: row index
	columnIndex: column index
	value: value at the above provided row and column
	"""
	def __init__(self, rowIndex, columnIndex, value):
		self.rowIndex = rowIndex
		self.columnIndex = columnIndex
		self.value = value
		self.expanded = False
		self.parentNode = None

"""
Method to generate a 2d array of Nodes.

inputMaze: input 2d array read from inputFile
returns 2d array of Nodes
"""
def generateNodeMatrix(inputMaze):
	nodeMatrix = []
	for rowIndex, row in enumerate(inputMaze):
		nodeMatrix.append([])
		for columnIndex, value in enumerate(row):
			jumpValue = -1 if value == 'G' else int(value)
			nodeMatrix[rowIndex].append(Node(rowIndex, columnIndex, jumpValue))

	return nodeMatrix

"""
Method to trace back the path from a given node to its oldest parent.

childNode: child node
returns the entire path from parent to the child node
"""
def tracePath(childNode):
	if not childNode.parentNode:
		return []

	pathTrace = []
	while childNode is not None:
		pathTrace.append((childNode.rowIndex, childNode.columnIndex))
		childNode = childNode.parentNode

	return pathTrace[::-1]

"""
Method to get all possible next nodes for a given node. Here we are only
considering transitions in Up, Bottom, Left and Right directions.

currentNode: current node
nodeMatrix: 2d array with nodes
returns all possible next nodes of a given nodes
"""
def getNextNodes(currentNode, nodeMatrix):
	nextNodes = []
	rows = len(nodeMatrix)
	columns = len(nodeMatrix[0])
	currentRow = currentNode.rowIndex
	currentColumn = currentNode.columnIndex
	jumpValue = currentNode.value

	if(currentColumn + jumpValue < columns):
		nextNodes.append(nodeMatrix[currentRow][currentColumn + jumpValue])
	if(currentRow + jumpValue < rows):
		nextNodes.append(nodeMatrix[currentRow + jumpValue][currentColumn])
	if(currentRow - jumpValue >= 0):
		nextNodes.append(nodeMatrix[currentRow - jumpValue][currentColumn])
	if(currentColumn - jumpValue >= 0):
		nextNodes.append(nodeMatrix[currentRow][currentColumn - jumpValue])

	return nextNodes

"""
Depth first search algorithm implementation.

inputMaze: input 2d array read from inputFile
returns the path from source to destination
"""
def depthFirstSearch(inputMaze):
	nodeMatrix = generateNodeMatrix(inputMaze)
	startNode = nodeMatrix[0][0]
	startNode.expanded = True
	stack = [startNode]
	statesExpanded = []
	pathTrace = []

	while len(stack) > 0:
		currentNode = stack.pop()
		statesExpanded.append((currentNode.rowIndex, currentNode.columnIndex))
		if currentNode.value == -1:
			pathTrace = tracePath(currentNode)
			break
		nextNodes = getNextNodes(currentNode, nodeMatrix)
		for nextNode in nextNodes:
			if not nextNode.expanded:
				nextNode.expanded = True
				nextNode.parentNode = currentNode
				stack.append(nextNode)

	return (pathTrace, statesExpanded)

"""
Method to perfrom I/O operations and to trigger the search algorithm.
"""
def findMinCostPath():
	inputMaze = []

	with open(sys.argv[1], 'r') as inputFile:
		csvreader = csv.reader(inputFile, delimiter = ',', lineterminator = '\n')
		for row in csvreader:
			inputMaze.append(row)
	inputFile.close()

	minCostPath, statesExpanded = depthFirstSearch(inputMaze)
	print("Intermediate states expanded: " + str(statesExpanded))
	print("Total number of intermediate states expanded: " + str(len(statesExpanded)))

	outputFileName = sys.argv[1].split('.')[0] + '-solution-dfs-vchalla2.txt'
	with open(outputFileName, 'w') as outputFile:
		csvwriter = csv.writer(outputFile)
		csvwriter.writerows(minCostPath)
	outputFile.close()

"""
Main method.
"""
if __name__ == '__main__':
	findMinCostPath()
