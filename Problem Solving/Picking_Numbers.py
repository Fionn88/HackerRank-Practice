#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#
from collections import Counter
def pickingNumbers(a):
    # Count The Numbers Show Up How Many Times
    c = Counter(a) # Counter({3: 2, 4: 1, 6: 1, 5: 1, 1: 1}) 
    maxi = 0
    for k in sorted(c):
        # c[k] get the value, get the grater than one value, if not return 0
        m = c[k]+c.get(k+1,0)
        # find the max value, using max function time complexcity going to O(n^2), but this case is O(n)
        if maxi<m:
            maxi=m
    return maxi
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
