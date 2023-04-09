#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def viralAdvertising(n):
    # Write your code here
    Shared = [5]
    Liked = [2]
    ans = 0
    for i in range(50):
        Shared.insert(i+1,Liked[i]*3)
        Liked.insert(i+1,Shared[i+1]//2)
    for j in range(n):
        ans += Liked[j]
    print(ans)
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
