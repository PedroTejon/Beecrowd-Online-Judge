t = int(input())
g = input()
gs = g.split()
c = 0
for x in gs:
    if int(x) == t:
        c += 1
print(c)
