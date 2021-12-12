from collections import Counter

n = int(input())

for x in range(n):
    c = Counter(input().lower())
    del c[' ']
    print(''.join(sorted([x for x in c if c[x] == max(c.values())])))

