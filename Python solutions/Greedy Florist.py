n, m = input().split()
n = int(n)
m = int(m)

arr = list(map(int, input().split()))
arr.sort(reverse=True)

ans = 0
index = 0
count = 0

for i in arr:
    if count == m:
        count = 0
        index += 1
    
    ans += (index + 1) * i 

    count += 1

print(ans)
