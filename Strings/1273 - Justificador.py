result = []
while True:
    n = int(input())
    if n == 0:
        break

    inps = [input() for x in range(n)]
    maior = max(inps, key=lambda x: len(x))
    result.append([f'{" " * (len(maior) - len(x))}{x}' for x in inps])

for x, caso in enumerate(result):
    for resultado in caso:
        print(resultado)
    if x != len(result) - 1:
        print()