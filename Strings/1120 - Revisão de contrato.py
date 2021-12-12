i = []
while '0 0' not in i:
    i.append(input())
for x in i[0:-1]:
    v = x.split()
    r = v[1].replace(v[0], '')
    if r != '':
        print(int(r))
    else:
        print(0)
