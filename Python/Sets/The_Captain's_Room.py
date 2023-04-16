"""
每個團體成員住的房間號碼都出現了K次，而隊長住的房間號碼只出現了一次，因此可以得到以下公式：
總房間號碼和 = 隊長房間號碼 + 團體成員房間號碼和
其中，團體成員房間號碼和等於(k-1)倍的房間號碼集合和，因此可以得到以下公式：

總房間號碼和 = 隊長房間號碼 + (k-1) * 房間號碼集合和

把這個公式稍微變形一下，即可得到以下公式：

隊長房間號碼 = (k * 房間號碼集合和) - 總房間號碼和)/(k-1)

這個公式就是程式碼中用來計算隊長房間號碼的那一行代碼，因此只需要用這個公式就可以得到隊長住的房間號碼。
"""


# Enter your code here. Read input from STDIN. Print output to STDOUT
k = int(input())
rooms = list(map(int, input().split()))
roomSet = set(rooms)
roomSum = sum(rooms)
roomSetSum = sum(roomSet) * k
captiansRoom = (roomSetSum - roomSum) // (k - 1)
print(captiansRoom)