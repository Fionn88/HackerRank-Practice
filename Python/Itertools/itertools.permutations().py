# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
string = input().split()
N = string[1]

ansTuple = sorted(list(permutations(string[0],int(N))))


for i in ansTuple:
    ans = ''.join(i)
    print(ans)