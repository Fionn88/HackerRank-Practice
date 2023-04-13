# Enter your code here. Read input from STDIN. Print output to STDOUT
n1 = input().split()
list1 = set(input().split())
n2 = input().split()
list2 = set(input().split())

print(len(list(list1.intersection(list2))))

