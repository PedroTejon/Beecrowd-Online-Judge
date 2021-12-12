n = int(input())

for _ in range(n):
    inp = input()
    primeiroSeg = inp[:len(inp) // 2] 
    segundoSeg = inp[len(inp) // 2:]
    print(f'{primeiroSeg[::-1]}{segundoSeg[::-1]}')
