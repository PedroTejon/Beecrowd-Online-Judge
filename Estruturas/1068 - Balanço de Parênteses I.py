while True:
    try:
        try:
            i = [x for x in input().split()[0]]
        except IndexError:
            print('correct')
            continue
        a = ''
        y = 0
        p, f = 0, 0
        for x in i:
            if x == '(':
                a += '('
                p += 1
            elif x == ')':
                a += ')'
                f += 1
        try:
            if len(a) % 2 == 0 and p == f and a[-1] != '(':
                for x in a:
                    if x == '(':
                        y = a.index(')', y + 1)
                    elif x == ')' and y == 0:
                        raise ValueError
                print('correct')
            else:
                print('incorrect')
        except ValueError:
            print('incorrect')
        except IndexError:
            print('correct')
    except EOFError:
        break
