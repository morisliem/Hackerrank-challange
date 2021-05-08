if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        m = {}
        con = False
        str1 = input()
        str2 = input()

        for i in str1:
            m[i] = 1

        for i in str2:
            if i in m:
                con = True
                break

        if con:
            print("YES")
        else:
            print("NO")
