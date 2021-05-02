n = int(input())
arr = input()
start = 0
count = 0
temp = []

for i in range(0,len(arr)):
    if arr[i] == 'U':
        start += 1
        temp.append(start)
    else:
        start -= 1
        temp.append(start)
    if start == 0 and temp[i-1] == -1:
        count += 1
        
print(count)
