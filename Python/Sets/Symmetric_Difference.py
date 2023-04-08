# Enter your code here. Read input from STDIN. Print output to STDOUT
N1 = input()
l1 = set(map(int,input().split()))
N2 = input()
l2 = set(map(int,input().split()))

d1Ans = sorted(l1.difference(l2))
d2Ans = sorted(l2.difference(l1))
ans = []

for i in list(d1Ans):
    ans.append(i)
for j in list(d2Ans):
    ans.append(j)
for k in sorted(ans):
    print(k)