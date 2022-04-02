a = [int(input()) for x in range(int(input()))]

for x in a:
    eo = 'EVEN' if (x % 2) == 0 else 'ODD'
    pn = 'POSITIVE' if x >= 1 else 'NEGATIVE'
    print(f'{eo} {pn}' if x != 0 else 'NULL')
