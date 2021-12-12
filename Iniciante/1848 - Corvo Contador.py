caw = 0
num = 0
while caw != 3:
    inp = input()
    if len(inp) == 3:
        num += sum([4 // (posi + 1)  for posi, char in enumerate(inp) if char == '*'])
    else:
        print(num)
        num = 0
        caw += 1