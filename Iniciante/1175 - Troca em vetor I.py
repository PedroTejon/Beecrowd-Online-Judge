i = [int(input()) for x in range(20)]
i = list(reversed(i))

[print(f'N[{x}] = {i[x]}') for x in range(20)]