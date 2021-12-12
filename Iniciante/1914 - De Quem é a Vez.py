n = int(input())
for _ in range(n):
    pessoas = {}
    inp = input().split()
    pessoas[inp[1]] = inp[0]
    pessoas[inp[3]] = inp[2]

    numero = sum(map(int, input().split()))

    print(pessoas['PAR'] if numero % 2 == 0 else pessoas['IMPAR'])