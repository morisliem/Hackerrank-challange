def swap(arr, i , j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

n = int(input())
arr = list(map(int, input().split()))

count =0
for i in range(len(arr)):
    for j in range(len(arr)-1):
        if arr[j] > arr[j+1]:
            swap(arr, j, j+1)
            count += 1

print("Array is sorted in", count, "swaps.")
print("First Element:", arr[0])
print("Last Element:", arr[len(arr)-1])
