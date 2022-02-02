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
		y_5 = weights[(0,5)][previous_weight_index] + weights[(1,5)][previous_weight_index] * input_word_value
		y_6 = weights[(0,6)][previous_weight_index] + weights[(1,6)][previous_weight_index] * input_word_value
		y_7 = weights[(0,7)][previous_weight_index] + weights[(1,7)][previous_weight_index] * input_word_value
		y_8 = weights[(0,8)][previous_weight_index] + weights[(1,8)][previous_weight_index] * input_word_value
		y_9 = weights[(0,9)][previous_weight_index] + weights[(1,9)][previous_weight_index] * input_word_value
		y_10 = weights[(0,10)][previous_weight_index] + weights[(1,10)][previous_weight_index] * input_word_value
		y_11 = weights[(0,11)][previous_weight_index] + weights[(1,11)][previous_weight_index] * input_word_value
		y_12 = weights[(0,12)][previous_weight_index] + weights[(2,12)][previous_weight_index] * y_2 + weights[(3,12)][previous_weight_index] * y_3 + weights[(4,12)][previous_weight_index] * y_4 + weights[(5,12)][previous_weight_index] * y_5 + weights[(6,12)][previous_weight_index] * y_6 + weights[(7,12)][previous_weight_index] * y_7 + weights[(8,12)][previous_weight_index] * y_8 + weights[(9,12)][previous_weight_index] * y_9 + weights[(10,12)][previous_weight_index] * y_10 + weights[(11,12)][previous_weight_index] * y_11
		actual_value = float(trainData[each_row][1])
		print("Train: Predicted Value={} Actual Value={}".format(y_5, actual_value))
		sum_of_squared_errors += (actual_value - y_12) ** 2
		initial_gradient_term = 2 * alpha * (y_12 - actual_value)
		hidden_layer_gradient_term = initial_gradient_term * input_word_value
		weights[(0,12)][updated_weight_index] = min(clip, weights[(0,12)][previous_weight_index] - initial_gradient_term)
		weights[(0,2)][updated_weight_index] = min(clip, weights[(0,2)][previous_weight_index] - initial_gradient_term)
		weights[(0,3)][updated_weight_index] = min(clip, weights[(0,3)][previous_weight_index] - initial_gradient_term)
		weights[(0,4)][updated_weight_index] = min(clip, weights[(0,4)][previous_weight_index] - initial_gradient_term)
		weights[(0,5)][updated_weight_index] = min(clip, weights[(0,5)][previous_weight_index] - initial_gradient_term)
		weights[(0,6)][updated_weight_index] = min(clip, weights[(0,6)][previous_weight_index] - initial_gradient_term)
		weights[(0,7)][updated_weight_index] = min(clip, weights[(0,7)][previous_weight_index] - initial_gradient_term)
		weights[(0,8)][updated_weight_index] = min(clip, weights[(0,8)][previous_weight_index] - initial_gradient_term)
		weights[(0,9)][updated_weight_index] = min(clip, weights[(0,9)][previous_weight_index] - initial_gradient_term)
		weights[(0,10)][updated_weight_index] = min(clip, weights[(0,10)][previous_weight_index] - initial_gradient_term)
		weights[(0,11)][updated_weight_index] = min(clip, weights[(0,11)][previous_weight_index] - initial_gradient_term)
		weights[(1,2)][updated_weight_index] = min(clip, weights[(1,2)][previous_weight_index] - hidden_layer_gradient_term)
		weights[(1,3)][updated_weight_index] = min(clip, weights[(1,3)][previous_weight_index] - hidden_layer_gradient_term)
		weights[(1,4)][updated_weight_index] = min(clip, weights[(1,4)][previous_weight_index] - hidden_layer_gradient_term)
		weights[(1,5)][updated_weight_index] = min(clip, weights[(1,5)][previous_weight_index] - hidden_layer_gradient_term)
		weights[(1,6)][updated_weight_index] = min(clip, weights[(1,6)][previous_weight_index] - hidden_layer_gradient_term)
		weights[(1,7)][updated_weight_index] = min(clip, weights[(1,7)][previous_weight_index] - hidden_layer_gradient_term)
		weights[(1,8)][updated_weight_index] = min(clip, weights[(1,8)][previous_weight_index] - hidden_layer_gradient_term)
		weights[(1,9)][updated_weight_index] = min(clip, weights[(1,9)][previous_weight_index] - hidden_layer_gradient_term)
		weights[(1,10)][updated_weight_index] = min(clip, weights[(1,10)][previous_weight_index] - hidden_layer_gradient_term)
		weights[(1,11)][updated_weight_index] = min(clip, weights[(1,11)][previous_weight_index] - hidden_layer_gradient_term)
		weights[(2,12)][updated_weight_index] = min(clip, weights[(2,12)][previous_weight_index] - (initial_gradient_term * (weights[(0,2)][previous_weight_index] + weights[(1,2)][previous_weight_index] * input_word_value)))
		weights[(3,12)][updated_weight_index] = min(clip, weights[(3,12)][previous_weight_index] - (initial_gradient_term * (weights[(0,3)][previous_weight_index] + weights[(1,3)][previous_weight_index] * input_word_value)))
		weights[(4,12)][updated_weight_index] = min(clip, weights[(4,12)][previous_weight_index] - (initial_gradient_term * (weights[(0,4)][previous_weight_index] + weights[(1,4)][previous_weight_index] * input_word_value)))
		weights[(5,12)][updated_weight_index] = min(clip, weights[(5,12)][previous_weight_index] - (initial_gradient_term * (weights[(0,5)][previous_weight_index] + weights[(1,5)][previous_weight_index] * input_word_value)))
		weights[(6,12)][updated_weight_index] = min(clip, weights[(6,12)][previous_weight_index] - (initial_gradient_term * (weights[(0,6)][previous_weight_index] + weights[(1,6)][previous_weight_index] * input_word_value)))
		weights[(7,12)][updated_weight_index] = min(clip, weights[(7,12)][previous_weight_index] - (initial_gradient_term * (weights[(0,7)][previous_weight_index] + weights[(1,7)][previous_weight_index] * input_word_value)))
		weights[(8,12)][updated_weight_index] = min(clip, weights[(8,12)][previous_weight_index] - (initial_gradient_term * (weights[(0,8)][previous_weight_index] + weights[(1,8)][previous_weight_index] * input_word_value)))
		weights[(9,12)][updated_weight_index] = min(clip, weights[(9,12)][previous_weight_index] - (initial_gradient_term * (weights[(0,9)][previous_weight_index] + weights[(1,9)][previous_weight_index] * input_word_value)))
		weights[(10,12)][updated_weight_index] = min(clip, weights[(10,12)][previous_weight_index] - (initial_gradient_term * (weights[(0,10)][previous_weight_index] + weights[(1,10)][previous_weight_index] * input_word_value)))
		weights[(11,12)][updated_weight_index] = min(clip, weights[(11,12)][previous_weight_index] - (initial_gradient_term * (weights[(0,11)][previous_weight_index] + weights[(1,11)][previous_weight_index] * input_word_value)))
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
		y_5 = weights[(0,5)][accessIndex] + weights[(1,5)][accessIndex] * input_word_value
		y_6 = weights[(0,6)][accessIndex] + weights[(1,6)][accessIndex] * input_word_value
		y_7 = weights[(0,7)][accessIndex] + weights[(1,7)][accessIndex] * input_word_value
		y_8 = weights[(0,8)][accessIndex] + weights[(1,8)][accessIndex] * input_word_value
		y_9 = weights[(0,9)][accessIndex] + weights[(1,9)][accessIndex] * input_word_value
		y_10 = weights[(0,10)][accessIndex] + weights[(1,10)][accessIndex] * input_word_value
		y_11 = weights[(0,11)][accessIndex] + weights[(1,11)][accessIndex] * input_word_value
		y_12 = weights[(0,12)][accessIndex] + weights[(2,12)][accessIndex] * y_2 + weights[(3,12)][accessIndex] * y_3 + weights[(4,12)][accessIndex] * y_4 + weights[(5,12)][accessIndex] * y_5 + weights[(6,12)][accessIndex] * y_6 + weights[(7,12)][accessIndex] * y_7 + weights[(8,12)][accessIndex] * y_8 + weights[(9,12)][accessIndex] * y_9 + weights[(10,12)][accessIndex] * y_10 + weights[(11,12)][accessIndex] * y_11
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
	weights = dict.fromkeys([(0,2),(0,3),(0,4),(0,5),(0,6),(0,7),(0,8),(0,9),(0,10),(0,11),(0,12),(1,2),(1,3),(1,4),(1,5),(1,6),(1,7),(1,8),(1,9),(1,10),(1,11),(2,12),(3,12),(4,12),(5,12),(6,12),(7,12),(8,12),(9,12),(10,12),(11,12)], [1, 0])
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
