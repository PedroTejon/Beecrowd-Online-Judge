from struct import unpack, pack
a = input().split()
b = input().split()
a1 = float(a[0])
b1 = float(a[1])
a1 = unpack('f', pack('f', a1))[0]
b1 = unpack('f', pack('f', b1))[0]
print(f'A = {a1:.6f}, B = {b1:.6f}')
print(f'C = {float(b[0]):.6f}, D = {float(b[1]):.6f}')
print(f'A = {a1:.1f}, B = {b1:.1f}')
print(f'C = {float(b[0]):.1f}, D = {float(b[1]):.1f}')
print(f'A = {a1:.2f}, B = {b1:.2f}')
print(f'C = {float(b[0]):.2f}, D = {float(b[1]):.2f}')
print(f'A = {a1:.3f}, B = {b1:.3f}')
print(f'C = {float(b[0]):.3f}, D = {float(b[1]):.3f}')
print(f'A = {a1:.3E}, B = {b1:.3E}')
print(f'C = {float(b[0]):.3E}, D = {float(b[1]):.3E}')
print(f'A = {a1:.0f}, B = {b1:.0f}')
print(f'C = {float(b[0]):.0f}, D = {float(b[1]):.0f}')
