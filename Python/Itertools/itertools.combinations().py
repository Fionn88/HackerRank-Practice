# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
string = input().split()
N = int(string[1])
S = string[0]

for i in range(1,N+1):
    ansTuple = list(combinations(sorted(S),i))
    for i in ansTuple:
        ans = ''.join(i)
        print(ans)
