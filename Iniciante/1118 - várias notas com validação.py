# stop = False
# a2 = float(input())
#
# while stop != True:
#     a1 = float(input())
#
#     if 0 <= a1 <= 10 and not(0 <= a2 <= 10):
#         a2 = a1
#         print(f'nota invalida')
#
#     elif 0 <= a1 <= 10 and 0 <= a2 <= 10:
#         print(f'media = {(a1 + a2) / 2:.2f}')
#
#         while stop not in [1, 2]:
#             print(f'novo calculo (1-sim 2-nao)')
#             stop = True if int(input()) == 2 else False
#
#     else:
#         print(f'nota invalida')
#
#

s = 0
c = 0
parar = False
while parar is False:
    a = float(input())
    if 0.0 <= a <= 10:
        s += a
        c += 1
        if c == 2:
            print(f'media = {s / 2:.2f}')
            c = 0
            s = 0
            while True:
                print("novo calculo (1-sim 2-nao)")
                continuar = int(input())
                if continuar == 2:
                    parar = True
                    break
                elif continuar == 1:
                    parar = False
                    break
    else:
        print("nota invalida")
