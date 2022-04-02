n = int(input())

for _ in range(n):
    h, m, act = map(int, input().split())
    
    print(f'{h:0>2}:{m:0>2} - A porta {"abriu" if act else "fechou"}!')