def average(array):
    setArray = set(array)
    ans = sum(setArray)/len(setArray)
    return ans
    # your code goes here

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
