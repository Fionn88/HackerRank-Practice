n = int(input())
s = set(map(int, input().split()))
stepN = int(input())
for i in range(stepN):
    step = input().split()
    if step[0] == 'remove':
        s.remove(int(step[1]))
    elif step[0] == 'discard':
        s.discard(int(step[1]))
    else:
        s.pop()

print(sum(list(s)))