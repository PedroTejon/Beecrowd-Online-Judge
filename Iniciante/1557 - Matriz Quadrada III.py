while True:
    i = int(input())
    if i == 0:
        break
    else:
        matriz = []
        m = 1
        for linha in range(i):
            line = []
            for coluna in range(i):
                if coluna == 0:
                    line.append(2 ** linha)
                else:
                    line.append(line[-1] * 2)
                if max(line) > m:
                    m = len(f'{max(line)}')
            matriz.append(line)
        foi = False
        for linha in matriz:
            for coluna in linha:
                if coluna == linha[0] and foi is False:
                    print(f'{str(coluna).rjust(m)}', end='')
                    foi = True
                else:
                    print(f' {str(coluna).rjust(m)}', end='')
            foi = False
            print()
        print()
