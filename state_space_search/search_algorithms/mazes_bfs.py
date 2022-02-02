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
		self.visited = False
		"""
		fScore: f(n) which indicates the estimated distance to the end
		from current node (i.e heuristic value) f(n) = h(n)
		"""
		self.fScore = float("inf")
		self.parentNode = None

"""
Customized minheap class to heapify based on fScore f(n) = h(n).
"""
class MinHeap:

	"""
	Init method to create a heap and to keep track of their positions which
	will be used for updating later.

	array: array to be heapified
	"""
	def __init__(self, array):
		self.heap = self.buildHeap(array)

	"""
	Method to build heap.

	array: array to be heapified
	returns heapified array
	"""
	def buildHeap(self, array):
		firstParentIndex = (len(array) - 2) // 2
		for index in range(firstParentIndex, -1, -1):
			self.shiftDown(array, index, len(array) - 1)
		return array

	"""
	Method to heapify from parent to child nodes.

	array: array to be heapified
	currentIndex: parent node index to heapify all its child nodes
	endIndex: end node index
	"""
	def shiftDown(self, array, currentIndex, endIndex):
		while(currentIndex <= endIndex):
			leftChild = currentIndex * 2 + 1
			rightChild = currentIndex * 2 + 2
			index = currentIndex
			if(leftChild <= endIndex and array[leftChild].fScore < array[currentIndex].fScore):
				index = leftChild
			if(rightChild <= endIndex and array[rightChild].fScore < array[index].fScore):
				index = rightChild
			if(index != currentIndex):
				self.swap(index, currentIndex, array)
				currentIndex = index
			else:
				return

	"""
	Method to heapify from child to parent nodes.

	array: array to be heapified
	currentIndex: child node index to heapify all its parent nodes
	"""
	def shiftUp(self, array, currentIndex):
		parentIndex = (currentIndex - 1) // 2
		while(currentIndex > 0 and array[parentIndex].fScore > array[currentIndex].fScore):
			self.swap(parentIndex, currentIndex, array)
			currentIndex = parentIndex
			parentIndex = (currentIndex - 1) // 2

	"""
	Method to remove a node from the heap.

	returns the removed node
	"""
	def remove(self):
		if(self.isEmpty()):
			return

		self.swap(0, len(self.heap) - 1, self.heap)
		nodeToRemove = self.heap.pop()
		self.shiftDown(self.heap, 0, len(self.heap) - 1)

		return nodeToRemove

	"""
	Method to insert a node from the heap.

	node: node to be inserted
	"""
	def insert(self, node):
		self.heap.append(node)
		self.shiftUp(self.heap,  len(self.heap) - 1)

	"""
	Method to check if the heap is empty or not.

	returns True or False
	"""
	def isEmpty(self):
		return len(self.heap) == 0

	"""
	Method to swap 2 nodes.

	firstIndex: first node index to be swapped
	secondIndex: second node index to be swapped
	array: heap array
	"""
	def swap(self, firstIndex, secondIndex, array):
		array[firstIndex], array[secondIndex] = array[secondIndex], array[firstIndex]

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
			jumpValue = 0 if value == 'G' else int(value)
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
Method to calculate Heuristic value. We are using manhattan distance
to determine our heuristic value.

startNode: start node
endNode: target node
returns manhattan distance between two points
"""
def calculateHeuristicValue(startNode, endNode):
	startRow = startNode.rowIndex
	startColumn = startNode.columnIndex
	endRow = endNode.rowIndex
	endColumn = endNode.columnIndex

	return abs(startRow - endRow) + abs(startColumn - endColumn)

"""
Method to find the position of goal in inputFile.To perform a informed
search we will need to have some knowledge about the goal to compute
our heuristic function.

inputMaze: input 2d array read from inputFile
returns coordinates of the goal
"""
def getEndPosition(inputMaze):
	for row in range(len(inputMaze)):
		for column in range(len(inputMaze[0])):
			if(inputMaze[row][column] == 'G'):
				return (row, column)

	return (-1, -1)

"""
Best first search algorithm implementation.

inputMaze: input 2d array read from inputFile
startRow: row index of the start point
startColumn: column index of the end point
endRow: row index of the target point
endColumn: column index of the target point
returns the path from source to destination
"""
def bestFirstSearch(inputMaze, startRow, startColumn, endRow, endColumn):
	nodeMatrix = generateNodeMatrix(inputMaze)
	startNode = nodeMatrix[startRow][startColumn]
	endNode = nodeMatrix[endRow][endColumn]
	startNode.visited = True
	startNode.fScore = calculateHeuristicValue(startNode, endNode)
	minHeap = MinHeap([startNode])
	statesExpanded = []

	while not minHeap.isEmpty():
		currentNode = minHeap.remove()
		statesExpanded.append((currentNode.rowIndex, currentNode.columnIndex))
		if currentNode == endNode:
			break
		nextNodes = getNextNodes(currentNode, nodeMatrix)
		for nextNode in nextNodes:
			if not nextNode.visited:
				nextNode.visited = True
				nextNode.fScore = calculateHeuristicValue(nextNode, endNode)
				nextNode.parentNode = currentNode
				minHeap.insert(nextNode)

	return (tracePath(endNode), statesExpanded)

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

	endPosition = getEndPosition(inputMaze)
	minCostPath, statesExpanded = bestFirstSearch(inputMaze, 0, 0, endPosition[0], endPosition[1])
	print("Intermediate states expanded: " + str(statesExpanded))
	print("Total number of intermediate states expanded: " + str(len(statesExpanded)))

	outputFileName = sys.argv[1].split('.')[0] + '-solution-bfs-vchalla2.txt'
	with open(outputFileName, 'w') as outputFile:
		csvwriter = csv.writer(outputFile)
		csvwriter.writerows(minCostPath)
	outputFile.close()

"""
Main method.
"""
if __name__ == '__main__':
	findMinCostPath()
