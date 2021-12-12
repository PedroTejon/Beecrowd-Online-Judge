a, b = 1, 1
while a != 0 and b != 0:
    a, b = input().split()
    a, b = int(a), int(b)
    if a != 0 and b != 0:
        print(a * b)
