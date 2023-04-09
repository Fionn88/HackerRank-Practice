# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())
country = set([])
for i in range(N):
    s = input() 
    country.add(s)
print(len(list(country)))