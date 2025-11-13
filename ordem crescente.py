numeros=[]
for i in range(5):
    n=int(input(f"digite o {i+1}º número:"))
    numeros.append(n)
numeros.sort()
print("números em ordem crescente:",numeros)