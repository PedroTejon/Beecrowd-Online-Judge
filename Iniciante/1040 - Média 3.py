n = [float(x) for x in input().split()]
m = (n[0] * 2 + n[1] * 3 + n[2] * 4 + n[3] * 1) / 10
if m < 5:
    print(f'Media: {m:.1f}')
    print(f'Aluno reprovado.')
elif 5 <= m < 7:
    print(f'Media: {m:.1f}')
    print(f'Aluno em exame.')
    n.append(float(input()))
    m = (m + n[4]) / 2
    print(f'Nota do exame: {n[4]}')
    if m < 5:
        print(f'Aluno reprovado.')
    else:
        print(f'Aluno aprovado.')
    print(f'Media final: {m:.1f}')
elif 7 <= m:
    print(f'Media: {m:.1f}')
    print(f'Aluno aprovado.')