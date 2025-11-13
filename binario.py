def busca_binaria(vetor,valor):
    inicio = 0
    fim = len(vetor) - 1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if vetor[meio] == valor:
            return meio
        elif vetor[meio] < valor:
            inicio = meio + 1
        else:
            fim = meio - 1
    return -1
vetor = [5, 12, 23, 34, 45, 56, 67, 78, 89]
valor = 45
posicao = busca_binaria(vetor, valor)
if posicao != -1:
    print(f"Valor {valor} encontrado na posição {posicao}.")
else:
    print("Valor não encontrado.")
