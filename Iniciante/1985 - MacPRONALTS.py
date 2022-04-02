n = int(input())
r = 0
for x in range(n):
    a, b = input().split()
    if a == '1001':
        r += 1.50 * int(b)
    elif a == '1002':
        r += 2.50 * int(b)
    elif a == '1003':
        r += 3.50 * int(b)
    elif a == '1004':
        r += 4.50 * int(b)
    elif a == '1005':
        r += 5.50 * int(b)
print(f'{r:.2f}')