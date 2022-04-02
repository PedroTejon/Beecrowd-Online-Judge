a = 0
b = 1
for i in range(1, 40, 2):
    a += i / b
    b *= 2
print(f'{a:.2f}')
