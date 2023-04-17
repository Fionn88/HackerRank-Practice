# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input())
for i in range(T):
    An = int(input())
    A = set(input().split())
    Bn = int(input())
    B = set(input().split())
    if len(list(A.intersection(B))) == An:
        print(True)
    else:
        print(False)
