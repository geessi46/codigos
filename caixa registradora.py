def calcular_desconto_progressivo(valor_total_compra):
    if valor_total_compra <= 100.00:
        percentual_desconto = 5
    elif 101.00 <= valor_total_compra <= 300.00:
        percentual_desconto = 10
    else: 
        percentual_desconto = 15
        
    valor_desconto = (percentual_desconto / 100.0) * valor_total_compra
    valor_final_pagar = valor_total_compra - valor_desconto
    
    
    return percentual_desconto, valor_desconto, valor_final_pagar


try:
    valor_original = float(input("Digite o valor total da compra (R$): "))
    
    if valor_original <= 0:
        print("O valor da compra deve ser positivo.")
    else:
       
        percentual, desconto, valor_final = calcular_desconto_progressivo(valor_original)
        
       
        print(f"\n--- Detalhes da Compra ---")
        print(f"Valor Original:          R$ {valor_original:.2f}")
        print(f"Percentual de Desconto:  {percentual}%")
        print(f"Valor do Desconto:       R$ {desconto:.2f}")
        print(f"Valor Final a Pagar:     R$ {valor_final:.2f}")
        print(f"---------------------------")

except ValueError:
    print("Entrada inválida. Digite um valor numérico válido.")