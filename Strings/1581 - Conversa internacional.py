for x in range(int(input())):
    k = int(input())
    linguas = set([input() for y in range(k)])
    print('ingles' if len(linguas) > 1 else list(linguas)[0])
