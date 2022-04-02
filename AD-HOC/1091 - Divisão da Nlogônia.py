n = int(input())
while n != 0:
    x_div, y_div = map(int, input().split())
    
    for x in range(n):
        x, y = map(int, input().split())
        
        if x == x_div or y == y_div:
            print("divisa")
            continue
        
        print(('N' if y > y_div else 'S') + ('E' if x > x_div else 'O'))
    
    n = int(input())