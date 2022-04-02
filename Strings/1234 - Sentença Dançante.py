# while True:
#     try:
#         a = True
#         i = input()
#         r = ''
#         for x in i:
#             if x == ' ':
#                 r += ' '
#                 continue
#             if a:
#                 r += x.upper()
#                 a = False
#             else:
#                 r += x.lower()
#                 a = True
#         print(r)
#     except EOFError:
#         break
# while True:
#     try:
#         linha_new = ""
#         linha = input()
#
#         maiuscula = True
#
#         for l in linha:
#             if l == ' ':
#                 linha_new += ' '
#                 continue
#             if maiuscula:
#                 linha_new += l.upper()
#                 maiuscula = False
#             else:
#                 linha_new += l.lower()
#                 maiuscula = True
#         print(linha_new)
#     except EOFError:
#         break
while True:
    try:
        linha_new = ""
        linha = input()

        maiuscula = True

        for l in linha:
            if l == ' ':
                linha_new += ' '
                continue
            if maiuscula:
                linha_new += l.upper()
                maiuscula = False
            else:
                linha_new += l.lower()
                maiuscula = True
        print(linha_new)
    except EOFError:
        break