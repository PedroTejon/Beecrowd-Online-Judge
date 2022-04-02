try:
    while True:
        v, t = map(int, input().split())
        
        print(v * t * 2)
        
except EOFError:
    pass