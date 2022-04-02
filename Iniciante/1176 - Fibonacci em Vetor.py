fib = [0, 1]
for x in range(60):
    b = fib[-2] + fib[-1]
    fib.append(b)

vzs = int(input())
i = [int(input()) for x in range(vzs)]

[print(f'Fib({x}) = {fib[x]}') for x in i]