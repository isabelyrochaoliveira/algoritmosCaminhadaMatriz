def menu(mapa):
    while True:
        print("\n--------------- MENU ---------------\n"
              "\n1 - Caminhada Fixa"
              "\n2 - Caminhada Aleatória"
              "\n3 - Caminhada Gulosa"
              "\n4 - Sair")
        
        opcao = int(input("\nDigite o número da caminhada desejada:  "))

        if opcao == 4:
            break

        if opcao == 1:
            caminhadaFixa(mapa)

        elif opcao == 2:
            caminhadaAleatoria(mapa)

        elif opcao == 3:
            caminhadaGulosa(mapa)

        else:
            print("\nOpção inválida")
        
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------

def caminhadaFixa(mapa):
    print("\n---------- Caminhada FIXA ----------")

    contadorPassos = 0

    linha = 9
    coluna = 0

    movimentos = []
    caminho = []

    custoTotal = mapa[9][0]

    while linha != 0 or coluna != 9:
        if linha == 0:
            coluna += 1

            movimentos.append(0)

            caminho.append((linha, coluna))

            custoTotal += mapa[linha][coluna]

            contadorPassos += 1

        elif coluna == 9:
            linha -= 1

            movimentos.append(1)

            caminho.append((linha, coluna))

            custoTotal += mapa[linha][coluna]

            contadorPassos += 1

        else:

            if contadorPassos % 2 == 0:
                coluna += 1

                movimentos.append(0)

                caminho.append((linha, coluna))

                custoTotal += mapa[linha][coluna]

                contadorPassos += 1

            else:
                linha -= 1

                movimentos.append(1)

                caminho.append((linha, coluna))

                custoTotal += mapa[linha][coluna]

                contadorPassos += 1

        if contadorPassos % 5 == 0:
            mostrarCaminhoPercorrido(mapa, caminho, custoTotal)

    mostrarCaminhoPercorrido(mapa, caminho, custoTotal)

    print("\n---------- Caminhada FIXA ----------")
    print(f"Passos: {movimentos}")
    print(f"Custo total: {custoTotal}")
            
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------

def caminhadaAleatoria(mapa):
    import random
    
    for rodada in range(10):

        linha = 9
        coluna = 0

        movimentos = []

        custoTotal = mapa[9][0]    

        while linha != 0 or coluna != 9:
            if linha == 0:
                coluna += 1

                movimentos.append(0)

                custoTotal += mapa[linha][coluna]

            elif coluna == 9:
                linha -= 1

                movimentos.append(1)

                custoTotal += mapa[linha][coluna]

            else:

                passo = random.randint(0, 1)

                if passo == 0:
                    coluna += 1

                    movimentos.append(0)

                elif passo == 1:
                    linha -= 1

                    movimentos.append(1)

                custoTotal += mapa[linha][coluna]

        print(f"\n---------- Caminhada ALEATÓRIA {rodada+1} ----------")
        print(f"Passos: {movimentos}")
        print(f"Custo total: {custoTotal}")

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------

def caminhadaGulosa(mapa):

    contadorPassos = 0

    linha = 9
    coluna = 0

    movimentos = []
    caminho = []

    custoTotal = mapa[linha][coluna]

    while linha != 0 or coluna != 9:
        if linha == 0:

            coluna += 1

            movimentos.append(0)

            caminho.append((linha, coluna))

            custoTotal += mapa[linha][coluna]

            contadorPassos += 1

        elif coluna == 9:

            linha -= 1

            movimentos.append(1)

            caminho.append((linha, coluna))

            custoTotal += mapa[linha][coluna]

            contadorPassos += 1

        else:
            if mapa[linha-1][coluna] < mapa[linha][coluna+1]:

                linha -= 1

                movimentos.append(1)

                caminho.append((linha, coluna))

                custoTotal += mapa[linha][coluna]

                contadorPassos += 1

            elif mapa[linha-1][coluna] > mapa[linha][coluna+1]:

                coluna += 1

                movimentos.append(0)

                caminho.append((linha, coluna))

                custoTotal += mapa[linha][coluna]

                contadorPassos += 1

            else:
                coluna += 1

                movimentos.append(0)

                caminho.append((linha, coluna))

                custoTotal += mapa[linha][coluna]

                contadorPassos += 1

        if contadorPassos % 5 == 0:
            mostrarCaminhoPercorrido(mapa, caminho, custoTotal)

    mostrarCaminhoPercorrido(mapa, caminho, custoTotal)

    print("\n---------- Caminhada Gulosa ----------")
    print(f"Passos: {movimentos}")
    print(f"Custo total: {custoTotal}")

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
        
def mostrarMapa(mapa):
    for linha in mapa:
        print(linha)
    print()

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------

def mostrarCaminhoPercorrido(mapa, caminho, custoTotal):
    import copy

    mapaCopia = copy.deepcopy(mapa)

    for (x, y) in caminho:
        mapaCopia[x][y] = 0
        
    mostrarMapa(mapaCopia)
    print(f"\nCusto até agora: {custoTotal}\n")

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------

def coordenadaEmMapa(coordenada):
    
    mapa = []
    valores = []

    for i in range(10):
        linha = []
        for j in range(10):
            linha.append(0)
        mapa.append(linha)

    partes = coordenada.split(";")

    for parte in partes:
        parte = parte.strip()

        if parte == "":
            continue

        valores = parte.split(" ")

        x = int(valores[0])
        y = int(valores[1])
        custo = int(valores[2])
                
        mapa[x][y] = custo

    return mapa
    
#Programa principal ----------------------------------------------------------------------------------------------------------------------------------------------
#Ilha 1
coordenadas = "0 0 3; 0 1 25; 0 2 3; 0 3 8; 0 4 8; 0 5 1; 0 6 25; 0 7 1; 0 8 3; 0 9 8; 1 0 1; 1 1 3; 1 2 8; 1 3 3; 1 4 8; 1 5 1; 1 6 25; 1 7 3; 1 8 8; 1 9 1; 2 0 25; 2 1 1; 2 2 8; 2 3 1; 2 4 1; 2 5 1; 2 6 1; 2 7 25; 2 8 3; 2 9 1; 3 0 8; 3 1 25; 3 2 25; 3 3 25; 3 4 1; 3 5 3; 3 6 8; 3 7 8; 3 8 3; 3 9 25; 4 0 1; 4 1 1; 4 2 1; 4 3 25; 4 4 25; 4 5 3; 4 6 3; 4 7 25; 4 8 25; 4 9 8; 5 0 1; 5 1 25; 5 2 25; 5 3 1; 5 4 8; 5 5 8; 5 6 1; 5 7 3; 5 8 1; 5 9 8; 6 0 3; 6 1 8; 6 2 8; 6 3 3; 6 4 8; 6 5 3; 6 6 3; 6 7 3; 6 8 25; 6 9 8; 7 0 3; 7 1 25; 7 2 25; 7 3 3; 7 4 8; 7 5 1; 7 6 1; 7 7 8; 7 8 25; 7 9 3; 8 0 8; 8 1 1; 8 2 25; 8 3 3; 8 4 8; 8 5 8; 8 6 3; 8 7 3; 8 8 1; 8 9 25; 9 0 1; 9 1 25; 9 2 1; 9 3 1; 9 4 8; 9 5 25; 9 6 8; 9 7 3; 9 8 25; 9 9 1;"

#Ilha 2
#coordenadas = "0 0 8; 0 1 8; 0 2 3; 0 3 3; 0 4 25; 0 5 8; 0 6 25; 0 7 3; 0 8 8; 0 9 25; 1 0 1; 1 1 25; 1 2 8; 1 3 1; 1 4 8; 1 5 8; 1 6 8; 1 7 1; 1 8 8; 1 9 3; 2 0 1; 2 1 3; 2 2 3; 2 3 25; 2 4 8; 2 5 8; 2 6 1; 2 7 1; 2 8 8; 2 9 8; 3 0 25; 3 1 1; 3 2 3; 3 3 1; 3 4 8; 3 5 8; 3 6 25; 3 7 25; 3 8 25; 3 9 1; 4 0 25; 4 1 3; 4 2 3; 4 3 3; 4 4 3; 4 5 8; 4 6 8; 4 7 3; 4 8 25; 4 9 1; 5 0 8; 5 1 25; 5 2 1; 5 3 8; 5 4 3; 5 5 8; 5 6 8; 5 7 3; 5 8 3; 5 9 25; 6 0 25; 6 1 25; 6 2 3; 6 3 8; 6 4 1; 6 5 3; 6 6 25; 6 7 1; 6 8 25; 6 9 1; 7 0 1; 7 1 1; 7 2 1; 7 3 3; 7 4 8; 7 5 3; 7 6 1; 7 7 8; 7 8 25; 7 9 25; 8 0 3; 8 1 1; 8 2 3; 8 3 25; 8 4 3; 8 5 25; 8 6 8; 8 7 1; 8 8 8; 8 9 8; 9 0 8; 9 1 3; 9 2 8; 9 3 3; 9 4 25; 9 5 8; 9 6 1; 9 7 8; 9 8 3; 9 9 1;"

#Ilha 3
#coordenadas = "0 0 25; 0 1 1; 0 2 8; 0 3 25; 0 4 1; 0 5 25; 0 6 3; 0 7 3; 0 8 25; 0 9 25; 1 0 3; 1 1 25; 1 2 1; 1 3 3; 1 4 25; 1 5 25; 1 6 1; 1 7 1; 1 8 1; 1 9 25; 2 0 1; 2 1 8; 2 2 8; 2 3 8; 2 4 8; 2 5 25; 2 6 3; 2 7 25; 2 8 8; 2 9 3; 3 0 8; 3 1 8; 3 2 8; 3 3 1; 3 4 8; 3 5 8; 3 6 3; 3 7 3; 3 8 8; 3 9 3; 4 0 1; 4 1 8; 4 2 8; 4 3 1; 4 4 1; 4 5 3; 4 6 1; 4 7 8; 4 8 1; 4 9 1; 5 0 25; 5 1 8; 5 2 1; 5 3 8; 5 4 1; 5 5 1; 5 6 3; 5 7 25; 5 8 1; 5 9 25; 6 0 3; 6 1 8; 6 2 3; 6 3 1; 6 4 8; 6 5 1; 6 6 8; 6 7 3; 6 8 8; 6 9 8; 7 0 3; 7 1 3; 7 2 1; 7 3 8; 7 4 1; 7 5 3; 7 6 1; 7 7 3; 7 8 1; 7 9 25; 8 0 1; 8 1 3; 8 2 1; 8 3 8; 8 4 3; 8 5 3; 8 6 8; 8 7 1; 8 8 1; 8 9 25; 9 0 1; 9 1 1; 9 2 8; 9 3 8; 9 4 8; 9 5 1; 9 6 8; 9 7 8; 9 8 1; 9 9 8;"

mapa = coordenadaEmMapa(coordenadas)

menu(mapa)