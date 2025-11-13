notas = [6.5, 8.0, 4.7, 9.3, 7.5, 5.2, 10.0, 3.8, 6.9, 8.5,
         7.0, 2.5, 5.8, 9.0, 4.2, 6.0, 7.8, 8.9, 3.0, 9.7,
         6.4, 5.0, 8.2, 4.9, 7.1]
print("Notas originais:")
print(notas)
def bolha(lista):
    n = len(lista)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
bolha(notas)
print("\nNotas em ordem crescente:")
for i, nota in enumerate(notas):
    if nota >= 7:
        status = "Acima da média"
    else:
        status = "Abaixo da média"
    print(f"Posição {i + 1}: Nota = {nota:.1f} → {status}")
