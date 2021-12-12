a, b = map(int, input().split())
r = range(0, b + 1)
for x in range(1, b, a):
    print(' '.join(list(map(str, r[x:x + a]))))

# range(0, b + 1)
# [0,1,2,3,4,5,6,7,8,9,10]
# range(1, b, a)
# [1, 3, 5, 7, 9]
