a = 234.345
b = 45.698
print(f'{a:.6f} - {b:.6f}')
print(f'{a:.0f} - {b:.0f}')
print(f'{a:.1f} - {b:.1f}')
print(f'{a:.2f} - {b:.2f}')
print(f'{a:.3f} - {b:.3f}')
print(f'{a:e} - {b:e}')
print(f'{a:E} - {b:E}')
la = [len(f'{a:E}'), len(f'{a:e}'), len(str(a))]
lb = [len(f'{b:E}'), len(f'{b:e}'), len(str(b))]
lista = [f'{a:E}', f'{a:e}', a]
listb = [f'{b:E}', f'{b:e}', b]
print(f'{lista[la.index(min(la))]} - {listb[lb.index(min(lb))]}')
print(f'{lista[la.index(min(la))]} - {listb[lb.index(min(lb))]}')