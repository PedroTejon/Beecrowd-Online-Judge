a = ''.join(list(filter(lambda x: x in 'aeiou', input())))
print('S' if a == a[::-1] else 'N')