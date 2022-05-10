#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr):
    data = []
    for row in range(len(arr)-2):
        temp = []
        for col in range(len(arr)-2):
            for shift in range(col, col+3):
                temp.append(arr[row][shift])
                temp.append(arr[row+1][shift])
                temp.append(arr[row+2][shift])
            temp.pop(7)
            temp.pop(1)
            data.append(sum(temp))
            temp = []
    return max(data)
                
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
