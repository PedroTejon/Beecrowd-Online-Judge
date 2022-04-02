from math import floor
b = int(input())
g = int(input())
print('Amelia tem todas bolinhas!' if floor(g/2) <= b else f'Faltam {floor(g/2) - b} bolinha(s)')
