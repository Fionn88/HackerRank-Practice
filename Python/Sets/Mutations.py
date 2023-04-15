# Enter your code here. Read input from STDIN. Print output to STDOUT
aElement = int(input())
aList = set(input().split())
N = int(input())

x = 0
for i in range(N):
    event = input().split()
    bList = set(input().split())
    if event[0] == 'intersection_update':
        aList.intersection_update(bList)
    elif event[0] == 'symmetric_difference_update':
        aList.symmetric_difference_update(bList)
    elif event[0] == 'difference_update':
        aList.difference_update(bList)
    else:
        aList.update(bList)
        
print(sum(map(int,list(aList))))