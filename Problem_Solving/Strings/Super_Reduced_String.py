#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superReducedString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#
# import collections
def superReducedString(s):
    # Write your code here
    stack=["#"]  
    for i in s:
        print(stack[-1],i)
        if stack[-1]==i:    #If the element is same as top of stack
            stack.pop()     
        else:
            stack.append(i)     #Else push the element in the stack
    ans=""
    for i in stack[1:]:     #Ignoring the first index
        ans+=i              #Store the answer in the variable 'ans'
    if ans:
        return ans          #If string is not empty return it
    return "Empty String"   #Else return "Empty String"
 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
