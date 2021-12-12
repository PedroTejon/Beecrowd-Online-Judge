n = int(input())
pessoas = list(map(int, input().split()))

print(pessoas.index(min(pessoas)) + 1)