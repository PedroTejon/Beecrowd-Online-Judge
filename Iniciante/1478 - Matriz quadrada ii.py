# while True:
#     i = int(input())
#     if i == 0:
#         break
#     else:
#         matriz = []
#
#         for linha in range(i):
#             line = []
#             for  in range(i):
#                 if linha == coluna:
#                     line.append(1)
#                 elif linha < coluna:
#                     line.append(coluna - linha + 1)
#                 elif linha > coluna:
#                     line.append(linha - coluna + 1)
#             matriz.append(line)
#         foi = False
#         for linha in matriz:
#             for coluna in linha:
#                 if coluna == linha[0] and foi is False:
#                     print(f'{coluna:>3}', end='')
#                     foi = True
#                 else:
#                     print(f' {coluna:>3}', end='')
#             foi = False
#             print()
#         print()
