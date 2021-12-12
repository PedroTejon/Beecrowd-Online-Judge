numCasoTeste = int(input())
membros = ['Rolien', 'Naej', 'Elehcim', 'Odranoel']


for casoTeste in range(numCasoTeste):
    numInput = int(input())
    for _ in range(numInput):
        recebido = int(input())
        print(membros[recebido - 1])