if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    setArr = set(arr)
    maxArr = max(setArr)
    setArr.remove(maxArr)
    print(max(setArr))