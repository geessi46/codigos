
temperaturas = [
    25.5, 26.1, 27.0, 24.5, 23.9, 25.1, 28.3, 29.1, 30.5, 29.8,
    28.7, 27.4, 26.8, 25.3, 24.1, 23.5, 24.8, 26.9, 28.1, 29.5,
    30.1, 31.0, 30.8, 29.4, 28.0, 27.5, 26.4, 25.9, 24.9, 25.8
]





media_mensal = sum(temperaturas) / len(temperaturas)
maior_temp = max(temperaturas)
menor_temp = min(temperaturas)


dias_acima_media = 0
for temp in temperaturas:
    if temp > media_mensal:
        dias_acima_media += 1


print(f"\n--- Análise de Temperaturas do Mês (30 dias) ---")
print(f"Temperatura Média Mensal: R$ {media_mensal:.2f}°C")
print(f"Maior Temperatura Registrada: R$ {maior_temp:.1f}°C")
print(f"Menor Temperatura Registrada: R$ {menor_temp:.1f}°C")
print(f"Dias Acima da Média ({media_mensal:.2f}°C): {dias_acima_media} dias")
print(f"--------------------------------------------------")
