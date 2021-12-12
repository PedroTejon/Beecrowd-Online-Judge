for _ in range(int(input())):
    s = set(input().replace(',', '').replace(' ', ''))
    if len(s) == 26:
        print('frase completa')
    elif len(s) >= 12:
        print('frase quase completa')
    else:
        print('frase mal elaborada')