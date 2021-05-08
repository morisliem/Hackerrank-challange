if __name__ == '__main__':
    n, m = input().split()
    n = int(n)
    m = int(m)

    map1 = {}
    str1 = input().split(' ')
    str2 = input().split(' ')
    
    for i in str1:
        if i in map1:
            map1[i] += 1
        else:
            map1[i] = 1

    con = True
    for i in str2:
        if i not in map1 or map1[i] == 0:
            con = False
            break
        else:
            map1[i] -= 1

    if con:
        print("Yes")
    else:
        print("No")
