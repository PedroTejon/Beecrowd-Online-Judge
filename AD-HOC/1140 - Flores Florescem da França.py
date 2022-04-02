inp = input()
while inp != '*':
    print('Y' if list(map(lambda x: x[0].lower(), inp.split())).count(inp[0].lower()) == len(inp.split()) else 'N')
    inp = input()