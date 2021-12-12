while True:
    try:
        n = int(input())
        lesmas = list(map(int, input().split()))
        mlesma = max(lesmas)
        if mlesma < 10:
            print(1)
        elif 10 <= mlesma < 20:
            print(2)
        elif mlesma >= 20:
            print(3)
    except EOFError:
        break