#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'findMedian' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def findMedian(arr):
    # Write your code here
    sortArr = sorted(arr)
    if len(sortArr) % 2 != 0:
        index = len(sortArr) // 2 
        return sortArr[index]
    else:
        left = len(arr) / 2
        right = len(arr) / 2 - 1
        return (left+right)/2

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = findMedian(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
