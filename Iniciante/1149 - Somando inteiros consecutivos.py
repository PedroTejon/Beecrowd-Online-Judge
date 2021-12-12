a, *b = map(int, input().split())
n = 0
r = 0
for x in b:
    if x > 0:
        n = x
        break
for x in range(0, n):
    r += a + x
print(r)