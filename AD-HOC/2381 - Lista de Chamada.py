numAlunos, numAlunoDesejado = map(int, input().split())
alunos = [input() for x in range(numAlunos)]
print(f'{sorted(alunos)[numAlunoDesejado - 1]}')