for _ in range(int(input())):
    a = input()
    if sum(map(lambda x: x[1] == 'three'[x[0]], enumerate(a))) >= 4:
        print(3)
    elif sum(map(lambda x: x[1] == 'one'[x[0]], enumerate(a))) >= 2:
        print(1)
    elif sum(map(lambda x: x[1] == 'two'[x[0]], enumerate(a))) >= 2:
        print(2)