valor=int(input("digite um valor inteiro:"))
notas=[100,50,20,10,5]
print(f"Valor: {valor}")
for nota in notas:
    quantidade=valor//nota
    valor=valor%nota
    print(f"Notas de {nota}:{quantidade}")