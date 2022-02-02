import sys
import csv

"""
Method to train the neural network model.

weights: weights map to store previous and current iteration weights
trainData: training data
alpha: alpha value
returns: weights map and indexes to access them
"""
def trainModel(weights, trainData, alpha):
	clip = 0.5
	sum_of_squared_errors = float(0)
	previous_weight_index, updated_weight_index = None, None
	for each_row in range(0, len(trainData)):
		previous_weight_index, updated_weight_index = [0, 1] if (each_row % 2) == 0 else [1, 0]
		input_word_value = float(trainData[each_row][0])
		y_2 = weights[(0,2)][previous_weight_index] + weights[(1,2)][previous_weight_index] * input_word_value
		y_3 = weights[(0,3)][previous_weight_index] + weights[(1,3)][previous_weight_index] * input_word_value
		y_4 = weights[(0,4)][previous_weight_index] + weights[(1,4)][previous_weight_index] * input_word_value
		y_5 = weights[(0,5)][previous_weight_index] + weights[(2,5)][previous_weight_index] * y_2 + weights[(3,5)][previous_weight_index] * y_3 + weights[(4,5)][previous_weight_index] * y_4
		actual_value = float(trainData[each_row][1])
		print("Train: Predicted Value={} Actual Value={}".format(y_5, actual_value))
		sum_of_squared_errors += (y_5 - actual_value) ** 2
		initial_gradient_term = 2 * alpha * (y_5 - actual_value)
		hidden_layer_gradient_term = initial_gradient_term * input_word_value
		weights[(0,5)][updated_weight_index] = min(clip, weights[(0,5)][previous_weight_index] - initial_gradient_term)
		weights[(0,2)][updated_weight_index] = min(clip, weights[(0,2)][previous_weight_index] - initial_gradient_term)
		weights[(0,3)][updated_weight_index] = min(clip, weights[(0,3)][previous_weight_index] - initial_gradient_term)
		weights[(0,4)][updated_weight_index] = min(clip, weights[(0,4)][previous_weight_index] - initial_gradient_term)
		weights[(1,2)][updated_weight_index] = min(clip, weights[(1,2)][previous_weight_index] - hidden_layer_gradient_term)
		weights[(1,3)][updated_weight_index] = min(clip, weights[(1,3)][previous_weight_index] - hidden_layer_gradient_term)
		weights[(1,4)][updated_weight_index] = min(clip, weights[(1,4)][previous_weight_index] - hidden_layer_gradient_term)
		weights[(2,5)][updated_weight_index] = min(clip, weights[(2,5)][previous_weight_index] - (initial_gradient_term * (weights[(0,2)][previous_weight_index] + weights[(1,2)][previous_weight_index] * input_word_value)))
		weights[(3,5)][updated_weight_index] = min(clip, weights[(3,5)][previous_weight_index] - (initial_gradient_term * (weights[(0,3)][previous_weight_index] + weights[(1,3)][previous_weight_index] * input_word_value)))
		weights[(4,5)][updated_weight_index] = min(clip, weights[(4,5)][previous_weight_index] - (initial_gradient_term * (weights[(0,4)][previous_weight_index] + weights[(1,4)][previous_weight_index] * input_word_value)))
	print("Final Performance Of Trained Data:- " + str(sum_of_squared_errors))
	return [weights, updated_weight_index]

"""
Method to test the neural network model.

weights: weights map to store previous and current iteration weights
accessIndex: index to access the updated weights
testData: testing data
alpha: alpha value
"""
def testModel(weights, accessIndex, testData, alpha):
	sum_of_squared_errors = float(0)
	for each_row in range(0, len(testData)):
		input_word_value = float(testData[each_row][0])
		y_2 = weights[(0,2)][accessIndex] + weights[(1,2)][accessIndex] * input_word_value
		y_3 = weights[(0,3)][accessIndex] + weights[(1,3)][accessIndex] * input_word_value
		y_4 = weights[(0,4)][accessIndex] + weights[(1,4)][accessIndex] * input_word_value
		y_5 = weights[(0,5)][accessIndex] + weights[(2,5)][accessIndex] * y_2 + weights[(3,5)][accessIndex] * y_3 + weights[(4,5)][accessIndex] * y_4
		actual_value = float(testData[each_row][1])
		print("Test: Predicted Value={} Actual Value={}".format(y_5, actual_value))
		sum_of_squared_errors += (y_5 - actual_value) ** 2
	print("Final Performance Of Tested Data:- " + str(sum_of_squared_errors))

"""
Method to perfrom I/O operations and to trigger a neural network construction.
"""
def parseInput():
	trainData = []
	testData = []
	alpha = float(sys.argv[1])
	weights = dict.fromkeys([(0,2),(0,3),(0,4),(0,5),(1,2),(1,3),(1,4),(2,5),(3,5),(4,5)], [1, 0])
	with open(sys.argv[2], 'r') as trainFile:
		csvreader = csv.reader(trainFile, delimiter = ',', lineterminator = '\n')
		for row in csvreader:
			trainData.append(row)
	trainFile.close()
	weights, updated_weight_index = trainModel(weights, trainData, alpha)
	with open(sys.argv[3], 'r') as testFile:
		csvreader = csv.reader(testFile, delimiter = ',', lineterminator = '\n')
		for row in csvreader:
			testData.append(row)
	testFile.close()
	testModel(weights, updated_weight_index, testData, alpha)

"""
Main method.
"""
if __name__ == '__main__':
	parseInput()
