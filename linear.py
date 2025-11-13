def busca_linear(vetor, valor):
    for i in range(len(vetor)):
        if vetor[i]==valor:
              return i 
    return -1
vetor=[10,25,37,42,59,73]
valor=42
posicao=busca_linear(vetor,valor)
if posicao != -1:
    print(f"valor {valor} encontrado na posição {posicao}.")
else:
    print("valor não encontrado.")
