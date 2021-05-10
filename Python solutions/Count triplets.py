def countTriplets(arr, r):
        count = 0
        left = {}
        right = {}

        for i in arr:
            if i in right:
                right[i] += 1
            else:
                right[i] = 1

        for i in range(len(arr)):
            right[arr[i]] -= 1
            if arr[i]%r == 0:
                count += left.get(arr[i]/r,0)*right.get(arr[i]*r,0)
            left[arr[i]] = left.get(arr[i],0) + 1

        return count

if __name__ == '__main__':
    n, r = input().split()
    n = int(n)
    r = int(r)
    arr = list(map(int, input().split()))

    print(countTriplets(arr, r))
