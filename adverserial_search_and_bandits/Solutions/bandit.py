import argparse
import csv
import sys
from random import choices

"""
Class that provides functionality to perform stationary bandit algorithm.
"""
class Stat:
    """
    Initializes all the parameters of stationary bandit algorithm.
    """
    def __init__(self, args):
        self.decayRate = args.decay
        self.rewardWeightFunction = args.rwt

    """
    Equation that calculates the updated weight of a selected arm.

    previousWeight: previous weight of the selected arm
    currentReward: reward provided by the selected arm
    returns updated weight using stationary bandit algorithm equation
    """
    def calculateNewWeight(self, previousWeight, currentReward):

        return ((self.decayRate * previousWeight) + (self.rewardWeightFunction * currentReward))

"""
Class that provides functionality to perform rolling average bandit algorithm.
"""
class Roll:
    """
    Initializes all the parameters of rolling average bandit algorithm.
    """
    def __init__(self, armLength):
        self.armFrequencies = [0 for i in range(0, armLength)]

    """
    Equation that calculates the updated weight of a selected arm.

    previousWeight: previous weight of the selected arm
    currentReward: reward provided by the selected arm
    armIndex: index indicating the arm
    returns updated weight using rolling average bandit algorithm equation
    """
    def calculateNewWeight(self, previousWeight, currentReward, armIndex):
        armFrequency = self.armFrequencies[armIndex] + 1
        self.armFrequencies[armIndex] += 1
        return previousWeight + ((currentReward - previousWeight)/armFrequency)

"""
Class that provides functionality to perform exponential recency-weighted average bandit algorithm.
"""
class Rec:
    """
    Initializes all the parameters of exponential recency-weighted average bandit algorithm.
    """
    def __init__(self, armLength, initialWeight, args):
        self.decayRate = args.decay
        self.windowSize = 10
        self.trackRewards = [[] for idx in range(armLength)]
        self.trackWeights = [[initialWeight] for idx in range(armLength)]

    """
    Queue to maintain rewards with in a given window size.

    armIndex: armIndex indicating the arm
    currentReward: current reward of the selected arm
    """
    def modifyRewardQueue(self, armIndex, currentReward):
        if(len(self.trackRewards[armIndex]) == self.windowSize):
            self.trackRewards[armIndex].pop(0)
        self.trackRewards[armIndex].append(currentReward)

    """
    Queue to maintain weights with in a given window size.

    armIndex: armIndex indicating the arm
    currentWeight: current weight of the selected arm
    returns updated weight of the selected arm
    """
    def modifyWeightQueue(self, armIndex, currentWeight):
        weightToReturn = self.trackWeights[armIndex][0]
        if(len(self.trackWeights[armIndex]) == self.windowSize):
            self.trackWeights[armIndex].pop(0)
        self.trackRewards[armIndex].append(currentWeight)

        return weightToReturn

    """
    Equation that calculates the updated weight of a selected arm.

    currentWeight: current weight of the selected arm
    currentReward: current reward of the selected arm
    armIndex: armIndex indicating the arm
    currentStep: step number used to iterate over previous step within window size
    returns computed value from the recency-weighted average weight update equation
    """
    def calculateNewWeight(self, currentWeight, currentReward, armIndex, currentStep):
        decayRateComplement = (1 - self.decayRate)
        previousWeight = self.modifyWeightQueue(armIndex, currentWeight)
        queueIdx = len(self.trackRewards[armIndex]) - 1
        summation = 0
        j = currentStep - 1
        while (j >= 0 and j >= currentStep - self.windowSize):
            if(queueIdx < 0):
                break
            summation += self.decayRate * pow(decayRateComplement, currentStep - 1 - j) * float(self.trackRewards[armIndex][queueIdx])
            j -= 1
            queueIdx -= 1
        self.modifyRewardQueue(armIndex, currentReward)
        return pow(decayRateComplement, currentStep - 1) * previousWeight + summation

"""
Method to normalize a given set of probabilities so that they can sum up to 1.

probabilities: list of probabilities
lastUpdatedIndex: index of recently updated probability.
returns normalized probabilities
"""
def normalizeProbabilities(probabilities, lastUpdatedIndex):
    normalizedProbabilities = probabilities[:]
    if(normalizedProbabilities[lastUpdatedIndex] < 0):
        normalizedProbabilities = [probability + abs(normalizedProbabilities[lastUpdatedIndex]) for probability in normalizedProbabilities]
    probabilitySum = 0
    for probability in normalizedProbabilities:
        probabilitySum += probability
    for eachIndex in range(0, len(normalizedProbabilities)):
        normalizedProbabilities[eachIndex] = (normalizedProbabilities[eachIndex]) / (probabilitySum)
    return normalizedProbabilities

"""
Method to normalize a given weight so that it doesn't overload probability function.

weight: weight to noramlize
minimumWeight: minimum value among all the weights
maximumWeight: maximum value among all the weights
returns normalized weight that ranges in between 0 and 1
"""
def normalizeWeight(weight, minimumWeight, maximumWeight):
    if(maximumWeight == minimumWeight):
        return weight / maximumWeight
    else:
        return (weight - minimumWeight) / (maximumWeight - minimumWeight)

"""
Method to update minimum and maximum weights used for normalization.

weight: weight of a selected arm
minimumWeight: minimum weight among all the weights
maximumWeight: maximum value among all the weights
returns updated minimum and maximum values
"""
def updateMinMaxWeights(weight, minimumWeight, maximumWeight):
    if minimumWeight > weight:
        minimumWeight = weight
    if maximumWeight < weight:
        maximumWeight = weight

    return [minimumWeight, maximumWeight]

"""
Method to calculate probability of a arm to be selected.

normalizedWeight: normalized weight used to calculate probability
explorationRate: exploration rate given in the command line arguments
uniformDistributionParamater: uniform distribution paramater in the command line arguments
returns probability of the arm to be selected
"""
def updateProbability(normalizedWeight, explorationRate, uniformDistributionParamater):

    return ((normalizedWeight * (1 - explorationRate)) + (explorationRate * uniformDistributionParamater))

"""
Method to get the bandit algorithm to execute from the command line arguments.

args: command line arguments
armLength: number of arms in the given input data
initialWeight: initial weight of a selected arm
returns algorithm instance to execute
"""
def getAlgorithm(args, armLength, initialWeight):
    if(args.alg == "STAT"):
        return Stat(args)
    elif(args.alg == "ROLL"):
        return Roll(armLength)
    else:
        return Rec(armLength, initialWeight, args)

"""
Method to get updatedWeight based on the algorithm type.

executer: algorithm instance to trigger its methods
previousWeight: previous weight of a selected arm
currentReward: currentReward of the selected arm
armIndex: Index indicating the selected arm
currentStep: current step of exploration
algorithm: algorithm name to send relevant parameters
returns updated weight of a selected arm
"""
def getUpdatedWeight(executer, previousWeight, currentReward, armIndex,
currentStep, algorithm):
    if(algorithm == "STAT"):
        return executer.calculateNewWeight(previousWeight, currentReward)
    elif(algorithm == "ROLL"):
        return executer.calculateNewWeight(previousWeight, currentReward,
        armIndex)
    else:
        return executer.calculateNewWeight(previousWeight, currentReward,
        armIndex, currentStep)

"""
Method to execute bandit algorithm.

inputArmRewards: list rewards for all the corresponding arms provided in inputFile
args: command line arguments
"""
def executeBanditAlgo(inputArmRewards, args):
    armLength = len(inputArmRewards[0])
    weights = [args.w0 for i in range(0, armLength)]
    minimumWeight = maximumWeight = weights[0]
    probabilities = [1/armLength for i in range(0, armLength)]
    armIndex = choices(range(1, armLength + 1), probabilities)[0] - 1
    algorithm = getAlgorithm(args, armLength, weights[0])
    explorationRate = args.exp
    uniformDistributionParamater = args.dist
    cummulativeReward = 0
    step = 0

    for eachRow in inputArmRewards:
        step += 1
        previousWeight = weights[armIndex]
        currentReward = float(eachRow[armIndex])
        cummulativeReward += currentReward
        print()
        print("Current Step: " + str(step))
        print("Decision Made: Arm" + str(armIndex + 1))
        print("Current Reward: " + str(currentReward))
        print("Cummulative Reward: " + str(cummulativeReward))
        weights[armIndex] = getUpdatedWeight(algorithm, previousWeight,
        currentReward, armIndex, step, args.alg)
        minimumWeight, maximumWeight = updateMinMaxWeights(weights[armIndex], minimumWeight, maximumWeight)
        normalizedWeight = normalizeWeight(weights[armIndex], minimumWeight, maximumWeight)
        probabilities[armIndex] = updateProbability(normalizedWeight, explorationRate, uniformDistributionParamater)
        probabilities = normalizeProbabilities(probabilities, armIndex)
        armIndex = choices(range(1, armLength + 1), probabilities)[0] - 1

"""
Method to scan input data of arms and their corresponding rewards.

args: command line arguments
returns list of scanned input containing arms and their corresponding rewards
"""
def scanInputData(args):
    inputArmRewards = []
    with open(args.infile, 'r') as inputFile:
      csvreader = csv.reader(inputFile, delimiter = ',', lineterminator = '\n')
      next(csvreader)
      for row in csvreader:
        inputArmRewards.append(row)
    inputFile.close()

    return inputArmRewards

"""
Method to parse arguments and intiate the process.
"""
def initiateProcess():
    parser = argparse.ArgumentParser(prog='bandit.py')
    parser.add_argument('-a', '--alg', choices=['STAT', 'ROLL', 'REC'],
    help='--alg is one of ”STAT” ”ROLL” and ”REC” for the three types.',
    required=True)
    parser.add_argument('-e', '--exp', type=float,
    help='--exp is the exploration rate γ.', required=True)
    parser.add_argument('-u', '--dist', type=float,
    help='--dist is the uniform distribution parameter, use the same distribution for all values ξa.',
    required=True)
    parser.add_argument('-d', '--decay', type=float,
    help='--decay is the decay rate β. For the nonstationary REC or nonstationary version we use this for α.',
    required=True)
    parser.add_argument('-r', '--rwt', type=float,
    help='--rwt is the reward weight function η. Provide only in case of STAT algorithm',
    required=False)
    parser.add_argument('-w', '--w0', type=float,
    help='--w0 is the initial weight value for the arms wa0.',
    required=True)
    parser.add_argument('-i', '--infile', help='--infile is the appropriate ad data file.',
    required=True)
    args = parser.parse_args()
    if(args.alg == "STAT" and not args.rwt):
        print("Reward weight function is required for STAT bandit algorithm")
    else:
        inputArmRewards = scanInputData(args)
        executeBanditAlgo(inputArmRewards, args)

"""
Main method.
"""
if __name__ == '__main__':
	initiateProcess()
