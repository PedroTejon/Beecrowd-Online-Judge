from numpy import arange

a = int(input())

for x in arange(1, 10001):
    if (x % a) == 2:
        print(x)
