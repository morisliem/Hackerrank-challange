arr = input()
n = int(input())

number_of_a = 0
string_length = len(arr)

for i in arr:
    if i == 'a':
        number_of_a += 1

if n % string_length == 0:
    print((n // string_length) * number_of_a)
else:
    rem = n % string_length
    ans = n // string_length * number_of_a
    number_of_a = 0
    for i in range(0, rem):
        if arr[i] == 'a':
            number_of_a += 1
    print(ans + number_of_a)


