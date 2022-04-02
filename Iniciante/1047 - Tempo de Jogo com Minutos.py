hi, mi, hf, mf = map(int, input().split())

if 0 <= hf <= 24 and 0 <= mf <= 59:
    durh = hf - hi
    durm = mf - mi
    if durh == 0 and durm <= 0:
        durh = 24
    elif durh < 0:
        durh = 24 + durh

    if durm < 0:
        durm = 60 + durm
        durh -= 1

    print(f'O JOGO DUROU {durh} HORA(S) E {durm} MINUTO(S)')
