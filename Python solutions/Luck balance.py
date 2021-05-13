n , m = input().split()
n = int(n)
m = int(m)

map = {}
contest = []
count = 0 

for _ in range(n):
    a, b = input().split()
    a = int(a)
    b = int(b)

    if b == 1:
        count += 1

    contest.append(a)

    if a in map:
        map[a] = b
    else:
        map[a] = b

contest.sort()

count = count - m

ans = sum(contest)

for i in contest:
    if count > 0:
        if map[i] == 1:
            count -= 1
            ans -= (i*2)
    else:
        break
    

print(ans)
    
    
