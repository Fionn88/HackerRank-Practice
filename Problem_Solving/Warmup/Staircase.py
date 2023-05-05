#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    for i in range(n):
        i += 1
        string = "#"*i
        result = string.rjust(n, ' ')
        print(result)
    # Write your code here

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
