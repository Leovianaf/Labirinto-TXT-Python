# Função para ler o arquivo de labirinto
def ler_arquivo(entrada):
    labirinto = []
    with open(entrada) as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            labirinto.append(list(linha))
    return labirinto

# Função para encontrar um caminho no labirinto
def resolver_labirinto(labirinto):
    # Encontrar a posição da entrada
    for i in range(len(labirinto)):
        if "E" in labirinto[i]:
            entrada = (i, labirinto[i].index("E"))
            break

    # Encontrar a posição da saída
    for i in range(len(labirinto)):
        if "S" in labirinto[i]:
            saida = (i, labirinto[i].index("S"))
            break

    # Inicializar a pilha com a posição da entrada
    pilha = [entrada]

    # Inicializar um dicionário para armazenar os movimentos
    moves = {entrada: None}

    # Enquanto a pilha não estiver vazia
    while pilha:
        # Retirar a posição atual da pilha
        atual = pilha.pop()

        # Se a posição atual for a saída, encontramos um caminho
        if atual == saida:
            # Construir o caminho a partir do dicionário de movimentos
            caminho = []
            while atual is not None:
                caminho.append(atual)
                atual = moves[atual]
            caminho.reverse()
            return caminho

        # Obter as posições vizinhas válidas pra andar
        vizinhos = []
        for direcao in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            proximo = (atual[0] + direcao[0], atual[1] + direcao[1])
            if 0 <= proximo[0] < len(labirinto) and 0 <= proximo[1] < len(labirinto[0]):
                if labirinto[proximo[0]][proximo[1]] != "#":
                    if proximo not in moves:
                        vizinhos.append(proximo)

        # Adicionar os vizinhos à pilha e ao dicionário de movimentos
        for vizinho in vizinhos:
            pilha.append(vizinho)
            moves[vizinho] = atual

    # Se não houver caminho possível, retornar None
    return None

# Imprimir o labirinto de entrada
def imprimir_labirinto(labirinto):
    for linha in labirinto:
        print(" ".join(linha))
    print()

# Imprime o labirinto de saída e salva ele no arquivo saida.txt


def imprimir_rota_de_fuga(labirinto, caminho):
    for posicao in caminho:
        linha = list(labirinto[posicao[0]])
        linha[posicao[1]] = "o"
        labirinto[posicao[0]] = "".join(linha)
    # Imprimir o labirinto de saída
    print("Labirinto de saída:")
    imprimir_labirinto(labirinto)
    # Salvar o labirinto de saída em um arquivo
    with open("saida.txt", "w", encoding="utf-8") as saida:
        for linha in labirinto:
            saida.write(linha + "\n")


# Testar o código com um arquivo de labirinto
labirinto = ler_arquivo("entrada.txt")
print("Labirinto de entrada:")
imprimir_labirinto(labirinto)
caminho = resolver_labirinto(labirinto)
# Se existir caminho: é mostrado na tela; Se não: Ele informa que não foi encontrado
if caminho:
    imprimir_rota_de_fuga(labirinto, caminho)
else:
    print("Nenhum caminho para fuga foi encontrado!")
