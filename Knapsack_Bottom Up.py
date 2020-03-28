# Nate Tomlin
# 3/20/2019
# CS 445 Algorithms
# Knapsack Problem Bottom Up - This code is takes items which hold a weight and value and tries to put as many items into a knapsack with the highest value.  This starts at the last possible case and builds up to the first case.
# Code is adpated from https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/
# And code from website was orginonal contributed by Nikhil Bhavya Jain 


import random
import time
from statistics import mean


def knapSack(MaxWeight, weight, value, size):
    # Sets up two dimensional array hold the weights and number of the item in size
    K = [[0 for x in range(MaxWeight+1)] for x in range(size+1)] 
  
    # Build table K[][] in bottom up manner 
    for i in range(size+1): 
        for j in range(MaxWeight+1):
            # Fills array with zeros as bases case
            if i==0 or j==0: 
                K[i][j] = 0
            # Compares the weight of the last item to the max weight
            elif weight[i-1] <= j: 
                K[i][j] = max(value[i-1] + K[i-1][j-weight[i-1]],  K[i-1][j]) # Takes max value of when the iteam is included and when it is not included in the knapsack
            else: 
                K[i][j] = K[i-1][j]     # Only includes the value of the item previously in the knapsack
    return K[size][MaxWeight] 

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
    score = knapSack(MaxWeight, weight, value, size) # Function call
    print(score)            # Prints Score
    end = time.time()       # End Time

    t = end - start         # Sets Time Value
    timeList.append(t)      # Adds time to List of Times

avgTime = mean(timeList)    # Averages all times in list
print(avgTime)              # Prints Average run time
