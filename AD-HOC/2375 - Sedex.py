n = int(input())
y, x, z = [int(x) for x in input().split()]
if x >= n and y >= n and z >= n:
    print('S')
else:
    print('N')
