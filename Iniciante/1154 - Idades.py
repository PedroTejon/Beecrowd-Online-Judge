a = []
while True:
    i = int(input())
    if i < 0:
        break
    a.append(i)
print(f'{sum(a)/len(a):.2f}')