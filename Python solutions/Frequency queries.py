if __name__ == "__main__":
    n = int(input())
    map = {}
    ans = []
    for _ in range(n):
        a, b = input().split()
        a = int(a)
        b = int(b)

        if a == 1:
            if b in map:
                map[b] += 1
            else:
                map[b] = 1
        
        if a == 2:
            if b in map and map[b] > 0:
                map[b] -= 1

        if a == 3:
            ans.append(1 if b in set(map.values()) else 0)
    
    for i in ans:
        print(i)

