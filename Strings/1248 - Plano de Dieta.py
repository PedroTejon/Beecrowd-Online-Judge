n = int(input())

for _ in range(n):
    alimentos = input()
    cafe = input()
    almoco = input()
    jacomeu = cafe + almoco
    trapaceou = 0
    for x in set(jacomeu):
        if x not in alimentos:
            trapaceou = 1
            break
        elif jacomeu.count(x) > 1:
            trapaceou = 1
            break

    if trapaceou:
        print('CHEATER')
        continue

    print(''.join([x for x in sorted(alimentos) if x not in jacomeu]))

