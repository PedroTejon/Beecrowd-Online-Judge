i = int(input())
inp = [input() for x in range(i)]
for i in inp:
    val = i
    for x in i:
        if not x.isdigit(): val = val.replace(x, ' ')

    print(sum(map(int, val.split())))
