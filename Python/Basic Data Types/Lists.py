if __name__ == '__main__':
    N = int(input())
    list = []
    for i in range(N):
        inplist = (input().split())
        if inplist[0] == 'insert':
            list.insert(int(inplist[1]), int(inplist[2]))
            
        elif inplist[0] == 'append':
            list.append(int(inplist[1]))
        elif inplist[0] == 'print':
            print(list)
        elif inplist[0] == 'remove':
            list.remove(int(inplist[1]))
        elif inplist[0] == 'pop':
            list.pop()
        elif inplist[0] == 'sort':
            list.sort()
        elif inplist[0] == 'reverse':
            list.reverse()
