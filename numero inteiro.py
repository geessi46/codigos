numero=int(input("digite um número inteiro:"))
soma=0
for digito in str(abs(numero)):
    soma+=int(digito)
print("a soma dos dígitos é:",soma)