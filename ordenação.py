def bubble_sort(vetor):
    n = len(vetor)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if vetor[j] > vetor[j + 1]:
                vetor[j], vetor[j + 1] = vetor[j + 1], vetor[j]  
    return vetor
vetor = [42, 17, 83, 59, 24, 96, 11]
print("Vetor original:", vetor)
ordenado = bubble_sort(vetor)
print("Vetor ordenado:", ordenado)
