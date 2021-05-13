n = int(input())
k = int(input())
arr = []

for _ in range(n):
    tmp = int(input())
    arr.append(tmp)


arr.sort()
ans = arr[k-1] - arr[0]

for i in range(len(arr) - k + 1):
    temp = arr[i+k-1] - arr[i]

    if ans > temp:
        ans = temp

print(ans)

    
