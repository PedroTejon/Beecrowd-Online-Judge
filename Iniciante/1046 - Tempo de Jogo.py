hi, hf = map(int, input().split())

if 0 <= hf <= 24:
    durh = hf - hi
    if durh == 0:
        durh = 24
    elif durh < 0:
        durh = 24 + durh

    print(f'O JOGO DUROU {durh} HORA(S)')
