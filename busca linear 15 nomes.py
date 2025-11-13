nomes = ["Ana", "Bruno", "Carlos", "Daniela", "Eduardo", "Fernanda", "Gabriel", 
         "Helena", "Igor", "Joana", "Kleber", "Larissa", "Marcos", "Nathalia", "Otávio"]
busca = input("Digite o nome que deseja procurar: ")
encontrado = False
for i in range(len(nomes)):
    if nomes[i].lower() == busca.lower():
        print(f"Nome '{busca}' encontrado na posição {i}.")
        encontrado = True
        break
if not encontrado:
    print(f"Nome '{busca}' não encontrado na lista.")
