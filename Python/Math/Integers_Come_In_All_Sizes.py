# Enter your code here. Read input from STDIN. Print output to STDOUT

a = 0
b = 0
c = 0
d = 0
for i in range(4):
    n = int(input())
    if i == 0:
        a = n
    if i == 1:
        b = n
    if i == 2:
        c = n
    if i == 3:
        d = n
print(a**b + c**d)
