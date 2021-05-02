if __name__ == '__main__':
    n, k = input().split()
    n = int(n)
    k = int(k)
    arr = list(map(str, input().split()))
    rem = k % n
    left = arr[0 : rem]
    right = arr[rem : len(arr)]
    arr = right + left

    for i in range(len(arr)):
        print(arr[i], end=" ")
