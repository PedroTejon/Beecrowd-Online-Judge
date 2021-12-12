efetividade = {
    'pedra': ['tesoura', 'lagarto'],
    'tesoura': ['papel', 'lagarto'],
    'papel': ['pedra', 'Spock'],
    'lagarto': ['Spock', 'papel'],
    'Spock': ['tesoura', 'pedra']
}

num = int(input())

for partida in range(num):
    sheldon, raj = input().split()
    if sheldon in efetividade[raj]:
        print(f'Caso #{partida + 1}: Raj trapaceou!')
    elif raj in efetividade[sheldon]:
        print(f'Caso #{partida + 1}: Bazinga!')
    else:
        print(f'Caso #{partida + 1}: De novo!')