#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
#
"""
INTEGER d => 加總的結果
INTEGER m => 多少index去加總，變成d
INTEGER_ARRAY 
必須判斷先判斷 m多少

s = [1,2,1,3,2]
d =3 m =2
1. 2 <= 5
s[0:2] => index(0)+index(1) => 3
    ans = 1
i+1,j+1 => 1,3
2. 3 <= 5
s[1:3] => index(1)+index(2) => 3
    ans = 2
i+1,j+1 = 2,4
3. 4 <= 5
s[2:4] => index(2)+index(3) => 4
i+1,j+1 = 3,5
4, 5 <= 5
s[3:5] => index(3)+index(4) => 5
5. m = 6, so return
"""


def birthday(s, d, m):
    i = 0
    ans = 0
    while m <= len(s):
        if sum(s[i:m]) == d:
            ans += 1
        i += 1
        m += 1
    return ans
        
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
