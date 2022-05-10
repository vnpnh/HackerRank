#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    maxScore = []
    minScore = []
    for i in range(len(scores)):
        if i == 0:
            maxScore.append(scores[i])
            minScore.append(scores[i])
            continue
        
        if scores[i] > max(maxScore):
            maxScore.append(scores[i])
        
        elif scores[i] < min(minScore):
            minScore.append(scores[i]) 
    return [len(maxScore)-1, len(minScore)-1]
            
        
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
