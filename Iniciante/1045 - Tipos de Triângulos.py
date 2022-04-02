i = input().split()
i = sorted([float(x) for x in i])
a, b, c = i[2], i[1], i[0]

if a >= b + c:
    print('NAO FORMA TRIANGULO')
elif (a ** 2) > int((b ** 2) + (c ** 2)):
    print('TRIANGULO OBTUSANGULO')
elif a ** 2 < b ** 2 + c ** 2:
    print('TRIANGULO ACUTANGULO')
elif a ** 2 == b ** 2 + c ** 2:
    print('TRIANGULO RETANGULO')


if a == b == c:
    print('TRIANGULO EQUILATERO')
elif a == b != c or a != b == c or a == c != b:
    print('TRIANGULO ISOSCELES')
