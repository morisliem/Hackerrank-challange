def findLoc(temp, x):
    for i in range(len(temp)):
        if x == temp[i]:
            return i + 1
        
t = int(input())
for _ in range(t):
    money = int(input())
    n = int(input())
    arr = list(map(int, input().split()))
    temp = arr.copy()
    mp = {}
    for i in range(len(arr)):
        if arr[i] not in mp:
            mp[arr[i]] = 1
        else:
            mp[arr[i]] += 1

    countBefore = 0
    countAfter = 0
    for i in range(len(arr)-1):
        countBefore += 1
        mp[arr[i]] -= 1
        temp.pop(0)
        countAfter += 1
        target = money - arr[i]
        if target in mp and mp[target] >= 1:
            loc = findLoc(temp, target)
            print(countBefore , loc + countAfter)
            break
