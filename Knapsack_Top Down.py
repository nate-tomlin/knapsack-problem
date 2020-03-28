# Nate Tomlin
# 3/20/2019
# CS 445 Algorithms
# Knapsack Problem Top Down - This code is takes items which hold a weight and value and tries to put as many items into a knapsack with the highest value.
# Code is adpated from https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/
# And code for website was orginonal contributed by Nikhil Kumar Singh

import random
import time
from statistics import mean


def knapSack(MaxWeight, weight, value, size): 
    # Base Case when size or weight are 0
    if size == 0 or MaxWeight == 0 : 
        return 0
    # Compares the weight of the nth value to the max weight and if the nth value is more than the weight we call the function without the nth value
    if (weight[size-1] > MaxWeight): 
        return knapSack(MaxWeight, weight, value , size-1)
    else:
        # Key Point: Returns the max of either the item included or not included
        return max(value[size-1] + knapSack(MaxWeight - weight[size - 1], weight, value, size-1), knapSack(MaxWeight, weight, value, size-1)) 


# Number of times function runs
numIterations = 1000
# Sets up list for run times to be entered into
timeList = []
# Loop that runs programs based on numIterations
for x in range(0, numIterations):
    # Random Testcase  
    size = 50
    MaxWeight = 100
    value = []
    weight = []
    for i in range(size):
        value.append(random.randrange(1,101,1))     # Sets random values for the values
        weight.append(random.randrange(1,101,1))    # Sets random values for the weights

    start = time.time()     # Start Time
    score = knapSack(MaxWeight , weight , value , size) # Function call
    print(score)            # Prints Score
    end = time.time()       # End Time

    t = end - start         # Sets Time Value
    timeList.append(t)      # Adds time to List of Times

avgTime = mean(timeList)    # Averages all times in list
print(avgTime)              # Prints Average run time



