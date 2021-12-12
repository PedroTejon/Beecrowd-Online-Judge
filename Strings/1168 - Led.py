n = int(input())
for x in range(n):
    r = 0
    a = input()
    for y in a:
        if y == '1':
            r += 2
        elif y == '2':
            r += 5
        elif y == '3':
            r += 5
        elif y == '4':
            r += 4
        elif y == '5':
            r += 5
        elif y == '6':
            r += 6
        elif y == '7':
            r += 3
        elif y == '8':
            r += 7
        elif y == '9':
            r += 6
        elif y == '0':
            r += 6
    print(f'{r} leds')