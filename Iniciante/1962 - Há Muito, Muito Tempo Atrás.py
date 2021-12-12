n = int(input())
anos = [int(input()) for _ in range(n)]

[print(f'{ano - 2014} A.C.' if ano >= 2015 else f'{2015 - ano} D.C.') for ano in anos]