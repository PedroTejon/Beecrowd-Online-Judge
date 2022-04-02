from math import factorial

try:
    while True:
        a, b = map(int, input().split())
        print(factorial(a) + factorial(b))
        
except EOFError:
    pass