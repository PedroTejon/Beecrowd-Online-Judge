a = input().split()
b = input().split()
r = 0
if int(b[0]) > int(a[0]):
    r += int(b[0]) - int(a[0])
if int(b[1]) > int(a[1]):
    r += int(b[1]) - int(a[1])
if int(b[2]) > int(a[2]):
    r += int(b[2]) - int(a[2])
print(r)
