n = input()
a = []
[a.append(input()) for x in range(int(n.split()[1]))]
print(int(n.split()[0]) + a.count('fechou') - a.count('clicou'))