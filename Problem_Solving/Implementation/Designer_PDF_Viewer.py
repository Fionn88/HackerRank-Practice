"""
這道題目的意思是給你一個長度為26的整數數列h，數列中的第i個元素表示字母表中第i個字母的高度。例如，h[0]表示字母表中第一個字母'a'的高度，
h[1]表示字母表中第二個字母'b'的高度，以此類推。因此，如果h[25]=7，這意味著字母表中最後一個字母'z'的高度為7。
在這道問題中，給定一個字符串word，我們需要找到該字符串中高度最高的字母對應的高度，假設該高度為h_max，
然後計算矩形高亮區域的面積。因為每個字母的寬度都是1mm，所以矩形高亮區域的寬度等於word的長度。高亮區域的高度等於h_max，因此矩形高亮區域的面積等於word的長度乘以h_max，
即word.length * h_max。在給定的例子中，字母表中最高的字母'z'的高度為7，因此矩形高亮區域的面積等於word.length * h_max = 4 * 7 = 28。
"""


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'designerPdfViewer' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h
#  2. STRING word
#

def designerPdfViewer(h, word):
    # Write your code here
    temp = []
    for i in word:
        temp.append(h[ord(i) - ord('a')])
    maxTemp = max(temp)
    ans = len(word) * maxTemp
    return ans
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
