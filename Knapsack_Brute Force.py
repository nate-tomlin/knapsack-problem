# Nate Tomlin
# 3/20/2019
# CS 445 Algorithms
# Knapsack Problem Brute Force - This code is takes items which hold a weight and value and tries to put as many items into a knapsack with the highest value.
# Function randomWV() and knapsack() is adapted from https://www.youtube.com/watch?v=EdLw7hjAyNU
# Function powerSet() is adapted from https://rosettacode.org/wiki/Power_set#Python

import random
import time
from statistics import mean


# This function sets up the the weights and values for each item in a list
def randomWV(size):
    WVList = []
    for i in range(size):
        WVList.append((int(random.randrange(1,101,1)),int(random.randrange(1,101,1))))  #Sets random weights and values
    return WVList

# Creates a power set of all the possible combinations of the weights and values
def powerSet(WVList):
    result = [[]]
    for x in WVList:
        result.extend([subset + [x] for subset in result])
    return result

# Main function that compares all of the weights and values and returns the best value
def knapsack(VWList, MaxWeight):
    knapsack = []
    bestWeight = 0
    bestValue = 0
    for i in powerSet(WVList):
        # Adds all of the weights and all of the values
        sumWeight = sum([x[0] for x in i])
        sumValue = sum([x[1] for x in i])
        # Compares the running sum value to the best existing value while making sure that it is under the max weight
        if sumValue > bestValue and sumWeight <= MaxWeight:
            bestValue = sumValue
            #bestWeight = sumWeight
            #knapsack = i
    return bestValue


# Number of times function runs
numIterations = 1
# Sets up list for run times to be entered into 
timeList = []   
# Loop that runs programs based on numIterations
for x in range(0, numIterations):
    size = 25
    MaxWeight = 100
    WVList = randomWV(size)

    start = time.time()                 # Start Time
    score = knapsack(WVList, MaxWeight) # Function Call
    print(score)                        # Prints Score
    end = time.time()                   # End Time

    t = end - start                     # Sets Time Value
    timeList.append(t)                  # Adds time to List of Times

avgTime = mean(timeList)                # Averages all times in list
print(avgTime)                          # Prints Average run time
                       
