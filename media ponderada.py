
PESO_N1 = 2
PESO_N2 = 3
PESO_N3 = 5
SOMA_PESOS = PESO_N1 + PESO_N2 + PESO_N3 



try:
    
    n1 = float(input("Digite a Nota 1 (Peso 2): "))
    n2 = float(input("Digite a Nota 2 (Peso 3): "))
    n3 = float(input("Digite a Nota 3 (Peso 5): "))
    
    
    if not (0 <= n1 <= 10 and 0 <= n2 <= 10 and 0 <= n3 <= 10):
        print("As notas devem estar entre 0 e 10.")
    else:
        
        media_final = (n1 * PESO_N1 + n2 * PESO_N2 + n3 * PESO_N3) / SOMA_PESOS
        
       
        if media_final >= 5.0:
            situacao = "APROVADO"
        elif 3.0 <= media_final <= 4.999: 
            situacao = "RECUPERAÇÃO"
        else:
            situacao = "REPROVADO"
            
       
        print(f"\n--- Resultado do Aluno ---")
        print(f"Média Final:  {media_final:.2f}")
        print(f"Situação:     {situacao}")
        print(f"--------------------------")

except ValueError:
    print("Entrada inválida. Digite valores numéricos válidos para as notas.")

