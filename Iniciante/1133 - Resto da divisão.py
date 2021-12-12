n1 = int(input())
n2 = int(input())

a = n1 if n1 <= n2 else n2
b = n2 if n1 <= n2 else n1

a += 1
while a < b:
    if a % 5 == 2 or a % 5 == 3:
        print(a)
    a = a + 1