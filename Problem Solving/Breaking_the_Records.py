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
    Max = 0
    MaxValue = scores[0]
    MinValue = scores[0]
    Min = 0
    for i in range(len(scores)):
        if scores[i] < MinValue:
            MinValue = scores[i]
            Min += 1
        elif scores[i] > MaxValue:
            MaxValue = scores[i]
            Max += 1
    
    return Max,Min
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()