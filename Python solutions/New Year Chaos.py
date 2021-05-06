def swap(temp, n, m):
    tmp = temp[n]
    temp[n] = temp[m]
    temp[m] = tmp

def solution(arr, n):
    temp = arr.copy()
    temp.sort()

    ans = 0
    h = {}
    for i in range(n):
        h[temp[i]] = i

    for i in range(n):
        if arr[i] != temp[i]:
            locTarget = h[arr[i]]
            if abs(locTarget - i) < 3:
                while arr[i] != temp[i]:
                    ans += 1
                    swap(temp, locTarget, locTarget-1)
                    h[temp[locTarget - 1]] = locTarget-1
                    h[temp[locTarget]] = locTarget
                    locTarget -= 1 

            else:
                return 'Too chaotic'
    
    return ans


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        print(solution(arr, len(arr)))
