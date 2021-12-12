while True:
    try:
        string = input()
        [print(f'{" ".join(string[:x]):^{len(string) * 2}}').rstrip() for x in range(len(string), 0, -1)]
        print()
    except EOFError:
        break
