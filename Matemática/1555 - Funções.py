n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    result = {'Rafael': (3 * x) * (3 * x) + y ** 2, 'Beto': 2 * (x ** 2) + (5 * y) ** 2, 'Carlos': -100 * x + y ** 3}
    print(f'{max(result, key=result.get)} ganhou')