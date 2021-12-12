fir = [i for i in input().split()]
a1, b1, c1 = int(fir[0]), int(fir[1]), float(fir[2])
sec = [i for i in input().split()]
a2, b2, c2 = int(sec[0]), int(sec[1]), float(sec[2])
print('VALOR A PAGAR: R$ {:.2f}'.format((b1*c1) + (b2*c2)))
