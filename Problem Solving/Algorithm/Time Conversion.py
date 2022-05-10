#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    conversion = ""
    if s[-2:].lower() == 'am':
        if s[:2] == '12':
            conversion += "00"
        else:
            conversion += s[:2]

    else:
        if s[:2] == '12':
            conversion += "12"
        else:
            conversion += str(12 + int(s[:2]))
                
    conversion += s[2:-2]     
    return conversion 
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
