dia1, dia2, dia3 = map(int, input().split())


if dia1 > dia2 <= dia3 or (dia1 < dia2 < dia3 and dia2 - dia1 <= dia3 - dia2) or (dia1 > dia2 > dia3 and dia1 - dia2 > dia2 - dia3):
    print(':)')
elif dia1 < dia2 >= dia3 or (dia1 < dia2 < dia3 and dia2 - dia1 > dia3 - dia2) or (dia1 > dia2 > dia3 and dia1 - dia2 <= dia2 - dia3):
    print(':(')
elif dia1 == dia2 and dia2 < dia3:
    print(':)')
elif dia1 == dia2 and dia2 > dia3:
    print(':(')
elif dia1 == dia2 == dia3:
    print(':(')