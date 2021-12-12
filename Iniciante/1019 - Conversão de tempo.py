from math import floor
a = int(input())
h = floor(a / 3600)
a = floor(a % 3600)
m = floor(a / 60)
s = floor(a % 60)

print(f'{h:.0f}:{m:.0f}:{s:.0f}')
