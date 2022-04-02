n = int(input())
nums = [int(input()) for _ in range(n)]
pares = filter(lambda x: x % 2 == 0, nums)
impares = filter(lambda x: x % 2, nums)

[print(x) for x in sorted(pares) + sorted(impares, reverse=True)]
