from math import floor
d = int(input())

ano = floor(d / 365)
d = floor(d % 365)
m = floor(d / 30)
d = floor(d % 30)

print(f'{ano} ano(s)\n'
      f'{m} mes(es)\n'
      f'{d} dia(s)')