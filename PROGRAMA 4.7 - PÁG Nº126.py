
# Conta de telefone Tchau com 3 faixas de preços:
# Se gastou.
# < 200 - extra: 0.20€/min
# 200 < e < 400 - extra: 0.18€/min
# > 400 - extra: 0.15€7min

minutos = int(input("Quantos minutos gastou este mês? "))


if minutos < 200:
    preco = 0.20

else:
    if minutos < 400:
        preco = 0.18

    else:
        preco = 0.15

print(f"Você gastou este mês {minutos*preco:.2f}€")



# ------- INVERTENDO OS LIMITES --------

 
minutos = int(input("Quantos minutos gastou este mês? "))

if minutos > 400:
    preco = 0.15
else:
    if minutos > 200:
        preco = 0.18
    else:
        preco = 0.20

print(f"Você gastou este mês {minutos * preco:.2f}€")
