a=int(input("digite o primeiro número:"))
b=int(input("digite o segundo número:"))
resultado=0
for i in range(abs(b)):
    resultado+=a
if b<0:
    resultado=-resultado
print(f"{a}x{b}={resultado}")