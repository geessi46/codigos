import string


def verificar_forca_senha(senha):
    
    regras_nao_atendidas = []
    
 
    if len(senha) < 8:
        regras_nao_atendidas.append("A senha deve ter no mínimo 8 caracteres.")

   
    tem_maiuscula = False
    tem_minuscula = False
    tem_digito = False
    tem_especial = False
    
    caracteres_especiais = string.punctuation 

    for caracter in senha:
        if caracter.isupper():
            tem_maiuscula = True
        elif caracter.islower():
            tem_minuscula = True
        elif caracter.isdigit():
            tem_digito = True
        elif caracter in caracteres_especiais:
            tem_especial = True
            
    if not tem_maiuscula:
        regras_nao_atendidas.append("A senha deve conter pelo menos 1 letra maiúscula.")
    if not tem_minuscula:
        regras_nao_atendidas.append("A senha deve conter pelo menos 1 letra minúscula.")
    if not tem_digito:
        regras_nao_atendidas.append("A senha deve conter pelo menos 1 dígito numérico.")
    if not tem_especial:
        regras_nao_atendidas.append("A senha deve conter pelo menos 1 caracter especial.")
        

    if not regras_nao_atendidas:
        return "FORTE", []
    else:
        return "FRACA", regras_nao_atendidas


senha_digitada = input("Digite sua senha (visível): ")


if not senha_digitada:
    print("A senha não pode ser vazia.")
else:
   
    status, falhas = verificar_forca_senha(senha_digitada)
    
    print(f"\n--- Resultado da Análise ---")
    print(f"Status da Senha: **{status}**")
    
  
    if status == "FRACA":
        print("\nRegras Não Atendidas:")
        for regra in falhas:
            print(f"- {regra}")
    
    print(f"----------------------------")


