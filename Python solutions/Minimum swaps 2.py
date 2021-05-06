def swap(arr, n, m):
    temp = arr[n]
    arr[n] = arr[m]
    arr[m] = temp

def minSwap(arr, n):
    temp = arr.copy()
    temp.sort()
    numOfSwap = 0

    h = {}
    for i in range(n):
        h[arr[i]] = i
    
    init = 0

    for i in range(n):
        if arr[i] != temp [i]:
            numOfSwap += 1
            init = arr[i]
            swap(arr, i, h[temp[i]])
            h[init] = h[temp[i]]
            h[temp[i]] = i

    return numOfSwap

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    print(minSwap(arr, len(arr)))
