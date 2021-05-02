def answer(arr):
    index = 0
    max = sum(arr[0][0:3]) + arr[1][1] + sum(arr[2][0:3])
    while(index < 4):
        for i in range(4):
            top = sum(arr[index][i:i+3])
            mid = arr[index+1][i+1]
            bot = sum(arr[index+2][i:i+3])
            if (top + mid + bot) > max:
                max = top + mid + bot
        index+=1
    return max

if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().split())))

    print(answer(arr))
