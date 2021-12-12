while True:
    try:
        inp = input()
        while inp.count('_') != 0:
            inp = inp.replace('_', '<i>', 1)
            inp = inp.replace('_', '</i>', 1)
        while inp.count('*') != 0:
            inp = inp.replace('*', '<b>', 1)
            inp = inp.replace('*', '</b>', 1)
        print(inp)
    except EOFError:
        break
