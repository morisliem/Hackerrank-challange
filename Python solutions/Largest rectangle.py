def left(arr, index):
    con = True
    temp = index
    count = 0
    while con:
        if index > 0:
            if arr[temp] <= arr[index - 1]:
                count += 1
                index -= 1
            else:
                con = False
        else:
            con = False
    
    return count


def right(arr, index):
    con = True
    temp = index
    count = 0 
    while con:
        if index < len(arr)-1:
            if arr[temp] <= arr[index+1]:
                count +=1
                index += 1
            else:
                con = False
        else:
            con = False
    return count


n = int(input())
arr = list(map(int, input().split()))

max = -1
for i in range(len(arr)):
    r = right(arr, i)
    l = left(arr, i)

    tmp = (r + l + 1) * arr[i]

    if max < tmp:
        max = tmp

print(max)
