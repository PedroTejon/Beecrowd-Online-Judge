fib = [0, 1]
for x in range(46):
    b = fib[-2] + fib[-1]
    fib.append(b)

print(' '.join(list(map(str, fib[:int(input())]))))
