"""
因不知道迴圈數，用While迴圈
List數列中 0 為 -1，1 為 -2 => 2 * c[i] 將可實現出
i = (i + k) % n => 取餘數
如 i 為 0 則走到原點即可跳出
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    energy = 100
    i = 0
    while True:
        energy = energy - 1 - 2 * c[i]
        i = (i + k) % n
        if i == 0:
            break
    return energy
    
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()
