while True:
    inp = input().split()
    v, n, m = float(inp[0]), inp[1], inp[2]
    if v == 0 and int(n) == 0 and int(m) == 0:
        break

    premio = 0
    grupos = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16], [17, 18, 19, 20], [21, 22, 23, 24], [25, 26, 27, 28], [29, 30, 31, 32], [33, 34, 35, 36], [37, 38, 39, 40], [41, 42, 43, 44], [45, 46, 47, 48], [49, 50, 51, 52], [53, 54, 55, 56], [57, 58, 59, 60], [61, 62, 63, 64], [65, 66, 67, 68], [69, 70, 71, 72], [73, 74, 75, 76], [77, 78, 79, 80], [81, 82, 83, 84], [85, 86, 87, 88], [89, 90, 91, 92], [93, 94, 95, 96], [97, 98, 99, 00]]
    if int(n[-4:]) == int(m[-4:]):
        premio = v * 3000
    elif int(n[-3:]) == int(m[-3:]):
        premio = v * 500
    elif int(n[-2:]) == int(m[-2:]):
        premio = v * 50
    else:
        grupon = int(n[-2:]) // 4 if int(n[-2:]) % 4 != 0 else int(n[-2:]) // 4 - 1
        grupom = int(m[-2:]) // 4 if int(m[-2:]) % 4 != 0 else int(m[-2:]) // 4 - 1
        if n[-2:] == '00' and grupom == 24:
            premio = v * 16
        elif m[-2:] == '00' and grupon == 24:
            premio = v * 16
        elif grupom == grupon:
            premio = v * 16

    print(f'{premio:.2f}')
