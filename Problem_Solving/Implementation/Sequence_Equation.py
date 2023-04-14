# 13542
# p[1] = 1 => p[p[1]] = 1
# p[2] = 3 => p[p[5]] = 3
# p[3] = 5 => p[p[2]] = 5
# p[4] = 4 => p[p[4]] = 4
# p[5] = 2 => p[p[3]] = 2

# dict 取 = 後面的value變成key

# { 1: ,3: ,5: ,4: ,2: }
# => 找1 在List的哪個位置：1
# { 1:1,3: ,5: ,4: ,2: }
# => 找2 在List的哪個位置：5
# { 1:1, 3:5,5: ,4: ,2: }
# => 找3 在List的哪個位置：2
# { 1:1, 3:5, 5:2,4: ,2: }
# => 找4 在List的哪個位置：4
# { 1:1, 3:5, 5:2, 4:4,2:}
# => 找5在List的哪個位置：3
# { 1:1, 3:5, 5:2, 4:4, 2:3}

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import OrderedDict
#
# Complete the 'permutationEquation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY p as parameter.
#


def permutationEquation(p):
    # Write your code here
    dictTemp = {}
    ans = []
    for i in range(len(p)):
        dictTemp[p[i]] = p.index(i+1)+1
    dict1 = OrderedDict(sorted(dictTemp.items()))
    for j in dict(dict1).values():
        ans.append(j)
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

