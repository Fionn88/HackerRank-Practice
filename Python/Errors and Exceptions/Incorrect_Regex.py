# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
N = int(input())

for i in range(N):
    try:
      reg = re.compile(input())
    except: 
        print(False)
    else:
        print(True)
