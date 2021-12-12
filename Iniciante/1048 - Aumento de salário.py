a = float(input())

if 0 <= a <= 400:
    print(f'Novo salario: {a * 1.15:.2f}\n'
          f'Reajuste ganho: {a * 0.15:.2f}\n'
          f'Em percentual: 15 %')
elif a <= 800:
    print(f'Novo salario: {a * 1.12:.2f}\n'
          f'Reajuste ganho: {a * 0.12:.2f}\n'
          f'Em percentual: 12 %')
elif a <= 1200:
    print(f'Novo salario: {a * 1.10:.2f}\n'
          f'Reajuste ganho: {a * 0.10:.2f}\n'
          f'Em percentual: 10 %')
elif a <= 2000:
    print(f'Novo salario: {a * 1.07:.2f}\n'
          f'Reajuste ganho: {a * 0.07:.2f}\n'
          f'Em percentual: 7 %')
elif 2000 < a:
    print(f'Novo salario: {a * 1.04:.2f}\n'
          f'Reajuste ganho: {a * 0.04:.2f}\n'
          f'Em percentual: 4 %')