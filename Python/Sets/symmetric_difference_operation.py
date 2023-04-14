# Enter your code here. Read input from STDIN. Print output to STDOUT
n1 = input()
s1 = set(input().split())
n2 = input()
s2 = set(input().split())

print(len(list(s1.symmetric_difference(s2))))