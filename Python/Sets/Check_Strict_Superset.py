# Enter your code here. Read input from STDIN. Print output to STDOUT
A = set(input().split())
N = int(input())
count = 0

for i in range(N):
    otherSets = set(input().split())
    if len(list(A.intersection(otherSets))) == len(list(otherSets)):
        count += 1
    
if count == N:
    print(True)
else:
    print(False)