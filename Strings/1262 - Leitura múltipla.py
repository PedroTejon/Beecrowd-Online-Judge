while True:
    try:
        n = input()
        i = int(input())
        c = 0
        r = 0
        for x in n:
            if x == 'R':
                r += 1
                if r == i:
                    c += 1
                    r = 0
            elif x == 'W':
                c += 1
                if r != 0:
                    r = 0
                    c += 1
        if r != 0:
            r = 0
            c += 1
        print(c)
    except EOFError:
        break
