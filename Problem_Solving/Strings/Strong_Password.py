#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumNumber' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING password
#

def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    j = 0
    ans = {"special": 0,"uppercase": 0, "lowercase":0,"digit":0}
    for i in range(n):
        if password[i] in ["!","@","#","$","%","^","&","*","(",")","-","+"]:
            special = ans.get("special")
            special += 1
            ans["special"] = special
        if password[i] in ["0","1","2","3","4","5","6","7","8","9","0"]:
            digit = ans.get("digit")
            digit += 1
            ans["digit"] = digit
        if password[i].islower():
            lowercase = ans.get("lowercase")
            lowercase += 1
            ans["lowercase"] = lowercase
        if password[i].isupper():
            uppercase = ans.get("uppercase")
            uppercase += 1
            ans["uppercase"] = uppercase
    lst = list(ans.values())
    k = lst.count(0)
    
    return max(k, 6 - n)
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
