while True:
    try:
        a = input().lower().split()
        letrasIniciais = [x[0] for x in a]
        qntdAlit = 0
        numaAlit = False
        letraPassada = letrasIniciais.pop(0)
        for x in letrasIniciais:
            if x == letraPassada and numaAlit == False:
                numaAlit = True
                qntdAlit += 1
            elif x != letraPassada:
                letraPassada = x
                numaAlit = False
        print(qntdAlit)
    except EOFError:
        break