numeros = [45, 12, 78, 3, 56, 23, 89, 10, 34, 67, 
           5, 90, 2, 8, 15, 49, 71, 19, 26, 30, 
           53, 60, 80, 99, 1]
print("Lista original:")
print(numeros)
def bolha_crescente(lista):
    n = len(lista)
    for i in range(n-1):
        for j in range(n-1-i):
            if lista[j] > lista[j+1]:   
                lista[j], lista[j+1] = lista[j+1], lista[j]
def bolha_decrescente(lista):
    n = len(lista)
    for i in range(n-1):
        for j in range(n-1-i):
            if lista[j] < lista[j+1]:   
                lista[j], lista[j+1] = lista[j+1], lista[j]
lista_crescente = numeros.copy()
lista_decrescente = numeros.copy()
bolha_crescente(lista_crescente)
bolha_decrescente(lista_decrescente)
print("\nLista ordenada em ordem crescente:")
print(lista_crescente)
print("\nLista ordenada em ordem decrescente:")
print(lista_decrescente)
