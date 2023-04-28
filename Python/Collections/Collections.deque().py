# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
d = deque()
N = int(input())
for i in range(N):
    s = input().split()
    if s[0] == 'append':
        d.append(int(s[1]))
    elif s[0] == 'appendleft':
        d.appendleft(int(s[1]))
    elif s[0] == 'pop':
        d.pop()
    elif s[0] == 'reverse':
        d.reverse()
    elif s[0] == 'popleft':
        d.popleft()
for i in list(d):
    print(i,end=' ')