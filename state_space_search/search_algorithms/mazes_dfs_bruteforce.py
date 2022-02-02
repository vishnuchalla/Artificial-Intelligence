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
searchPattern: search pattern to search neighbour nodes
returns all possible next nodes of a given nodes
"""
def getNextNodes(currentNode, nodeMatrix, searchPattern):
	nextNodes = []
	rows = len(nodeMatrix)
	columns = len(nodeMatrix[0])
	currentRow = currentNode.rowIndex
	currentColumn = currentNode.columnIndex
	jumpValue = currentNode.value

	for search in searchPattern:
		if(search == 'R' and currentColumn + jumpValue < columns):
			nextNodes.append(nodeMatrix[currentRow][currentColumn + jumpValue])
		if(search == 'B' and currentRow + jumpValue < rows):
			nextNodes.append(nodeMatrix[currentRow + jumpValue][currentColumn])
		if(search == 'U' and currentRow - jumpValue >= 0):
			nextNodes.append(nodeMatrix[currentRow - jumpValue][currentColumn])
		if(search == 'L' and currentColumn - jumpValue >= 0):
			nextNodes.append(nodeMatrix[currentRow][currentColumn - jumpValue])

	return nextNodes

"""
Method to generate all possible search patterns for dfs brute force.

moves: array containing all moves
start: start index of the array
allPossibleMoves: all possible combinations of the search patterns.
In our case its 4! combinations
"""
def generateSearchPatterns(moves, start, allPossibleMoves):
	if(start == len(moves) - 1):
		allPossibleMoves.append(moves[:])
		return

	for currentIndex in range(start, len(moves)):
		moves[currentIndex], moves[start] =  moves[start], moves[currentIndex]
		generateSearchPatterns(moves, start + 1, allPossibleMoves)
		moves[currentIndex], moves[start] =  moves[start], moves[currentIndex]

"""
Depth first search algorithm implementation.

inputMaze: input 2d array read from inputFile
searchPattern: search pattern to search
returns the path from source to destination
"""
def depthFirstSearch(inputMaze, searchPattern):
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
		nextNodes = getNextNodes(currentNode, nodeMatrix, searchPattern)
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
	initialSearchPattern = ['L', 'R', 'U', 'B']
	possiblePaths = {}
	possibleUniquePaths = []
	uniquePathStates = []
	minCostPath = []
	minCostPathTransitions = float("inf")
	totalNumberOfUniquePaths = 0
	totalNumberOfStatesExpanded = 0

	with open(sys.argv[1], 'r') as inputFile:
		csvreader = csv.reader(inputFile, delimiter = ',', lineterminator = '\n')
		for row in csvreader:
			inputMaze.append(row)
	inputFile.close()

	if(len(inputMaze) == 6 and len(inputMaze[0]) == 6):
		allPossiblePatterns = []
		generateSearchPatterns(initialSearchPattern, 0, allPossiblePatterns)
		for searchPattern in allPossiblePatterns:
			pathTrace, statesExpanded = depthFirstSearch(inputMaze, searchPattern)
			if str(pathTrace) not in possiblePaths.keys():
				possibleUniquePaths.append(pathTrace)
				uniquePathStates.append((str(statesExpanded) + ":" + str(len(statesExpanded))))
				possiblePaths[str(pathTrace)] = str(statesExpanded)
				if len(pathTrace) < minCostPathTransitions:
					minCostPathTransitions = len(pathTrace)
					minCostPath = pathTrace
			else:
				continue
			totalNumberOfUniquePaths += 1
			totalNumberOfStatesExpanded += len(statesExpanded)
		print("Total unique paths: ")
		print(possibleUniquePaths)
		print("And their corresponding states with expansion count: ")
		print(uniquePathStates)
		print("Total number of unique paths: " + str(totalNumberOfUniquePaths))
		print("Total number of intermediate states expanded: " + str(totalNumberOfStatesExpanded))

		outputFileName = sys.argv[1].split('.')[0] + '-solution-dfs-brute-force-vchalla2.txt'
		with open(outputFileName, 'w') as outputFile:
			csvwriter = csv.writer(outputFile)
			csvwriter.writerows(minCostPath)
		outputFile.close()
	else:
		print("Brute force is specific to a 6x6 matrix. Please check the input file")

"""
Main method.
"""
if __name__ == '__main__':
	findMinCostPath()
