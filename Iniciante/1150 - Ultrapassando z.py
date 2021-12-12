x = int(input())
z = int(input())

i = 2
s = 1
while z <= x:
    z = int(input())

while x <= z:
    x += x + s
    if x <= z:
        i = i + 1
        s = s + 1
print(i) 