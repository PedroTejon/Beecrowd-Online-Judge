n = int(input())
r = 0
a = [input() for x in range(n)]
for x in a:
    x.split()
    r += int(x.split()[0]) * int(x.split()[1])
print(r)
