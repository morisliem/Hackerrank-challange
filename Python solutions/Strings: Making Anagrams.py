str1 = input()
str2 = input()

a = set(str1) & set(str2)

total = len(str2) + len(str1)

mp1 = {}
mp2 = {}

for i in a:
    for j in str1:
        if i == j:
            if i not in mp1:
                mp1[i] = 1
            else:
                mp1[i] += 1

for i in a:
    for j in str2:
        if i == j:
            if i not in mp2:
                mp2[i] = 1
            else:
                mp2[i] += 1

intersect = 0

for i in mp1:
    if mp1[i] < mp2[i]:
        intersect += min(mp1[i], mp2[i])
    elif mp1[i] > mp2[i]:
        intersect += min(mp1[i], mp2[i])
    else:
        intersect += mp1[i]

print(total - (intersect * 2))
