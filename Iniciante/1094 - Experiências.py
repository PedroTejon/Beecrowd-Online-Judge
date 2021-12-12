a = int(input())

i = [input() for x in range(a)]
t = c = r = s = 0

for x in i:
    v = x.split()
    if v[1] == 'C':
        c += int(v[0])
    elif v[1] == 'R':
        r += int(v[0])
    elif v[1] == 'S':
        s += int(v[0])
    t += int(v[0])

print(f'Total: {t} cobaias\n'
      f'Total de coelhos: {c}\n'
      f'Total de ratos: {r}\n'
      f'Total de sapos: {s}\n'
      f'Percentual de coelhos: {c * 100 / t:.2f} %\n'
      f'Percentual de ratos: {r * 100 / t:.2f} %\n'
      f'Percentual de sapos: {s * 100 / t:.2f} %')
