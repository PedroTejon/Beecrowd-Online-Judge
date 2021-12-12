di = int(input().split()[1])
hi, mi, si = map(int, input().split(':'))
df = int(input().split()[1])
hf, mf, sf = map(int, input().split(':'))

durs = sf - si
durm = mf - mi
durh = hf - hi
durd = df - di

durs, durm = (60 + durs, durm - 1) if durs < 0 else (durs, durm)
durm, durh = (60 + durm, durh - 1) if durm < 0 else (durm, durh)
durh, durd = (24 + durh, durd - 1) if durh < 0 else (durh, durd)

print(f'{durd} dia(s)\n'
      f'{durh} hora(s)\n'
      f'{durm} minuto(s)\n'
      f'{durs} segundo(s)')
