metros = int(input())

custo = 7
if metros <= 30:
    custo += metros % 20
if metros < 10:
    metros -= metros % 10
else:
    metros -= 10
    