n, m = input().split()
n = int(n)
m = int(m)
dic = {}
count = 0

arr = list(map(int, input().split()))

for i in arr:
    if i not in dic:
        dic[i] = 1

for i in range(len(arr)):
    diff = arr[i] + m
    if diff in dic:
        count += 1

print(count)
