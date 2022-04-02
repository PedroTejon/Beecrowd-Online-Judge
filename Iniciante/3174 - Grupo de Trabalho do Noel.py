from math import floor
a = int(input())
i = [input() for x in range(a)]
hrself = [0, 0, 0, 0]
t = 0
for x in i:
    r = x.split()
    if r[1] == 'bonecos':
        hrself[0] += int(r[2])
    elif r[1] == 'arquitetos':
        hrself[1] += int(r[2])
    elif r[1] == 'musicos':
        hrself[2] += int(r[2])
    elif r[1] == 'desenhistas':
        hrself[3] += int(r[2])

t += floor(hrself[0] / 8) + floor(hrself[1] / 4) + floor(hrself[2] / 6) + floor(hrself[3] / 12)

print(t)
