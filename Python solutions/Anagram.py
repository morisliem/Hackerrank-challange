from collections import defaultdict

n = int(input())
for _ in range(n):
    s = input()
    if len(s) % 2 == 1:
        print(-1)
    else:
        mapLeft = defaultdict(int)
        mapRight = defaultdict(int)
        count = 0
        left = s[0:len(s)//2]
        right = s[len(s)//2:len(s)]
        for i in left:
            mapLeft[i] += 1
        
        for i in right:
            mapRight[i] += 1

        # print('Right ',mapRight)
        # print('Left', mapLeft)

        for i in mapLeft:
            if i in mapRight:
                if mapLeft[i] < mapRight[i]:
                    count += 0
                elif mapLeft[i] > mapRight[i]:
                    count += abs(mapLeft[i] - mapRight[i])
                else:
                    count += 0
            else:
                count += mapLeft[i]

        print(count)
