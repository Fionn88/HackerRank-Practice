# Enter your code here. Read input from STDIN. Print output to STDOUT
s1N = int(input())
s1 = set(input().split())
s2N = int(input())
s2 = set(input().split())

print(len(list(s1.union(s2))))