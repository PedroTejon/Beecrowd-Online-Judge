i = int(input())
lista = [input() for x in range(i)]

for x in lista:
    if 1 <= len(x) <= 100 and x[:3].isupper() and len(x) == 8 and x[3:4] == '-' and x[4:8].isnumeric():
        if x[-1] in ['1', '2']:
            print('MONDAY')
        elif x[-1] in ['3', '4']:
            print('TUESDAY')
        elif x[-1] in ['5', '6']:
            print('WEDNESDAY')
        elif x[-1] in ['7', '8']:
            print('THURSDAY')
        elif x[-1] in ['0', '9']:
            print('FRIDAY')
    else:
        print('FAILURE')
