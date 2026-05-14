
#🔥 MINI‑DESAFIO — Cálculo de Desconto por Faixa de Preço

# Imagina que uma loja aplica descontos assim:
# Preço < 50€ → 0% de desconto
# Preço entre 50€ e 200€ → 10% de desconto
# Preço > 200€ → 20% de desconto

# 🎯 O teu objetivo:

# Pedir ao utilizador o preço do produto
# Determinar o desconto usando apenas if
# Calcular o valor final a pagar
# Mostrar o desconto aplicado e o preço final


preco_produto = float(input("Indique o preço do item?"))

if preco_produto < 50:
    desconto = 0

if preco_produto >= 50 and preco_produto <= 200:                  # MELHOR OPÇÃO: if 50 <= preco_produto <= 200:
    desconto = 10

if preco_produto > 200:
    desconto = 20

desconto = preco_produto*desconto/100

valor_final = preco_produto - desconto

print(f"O desconto é de {desconto:.2f}€ e o valor com desconto é de {valor_final:.2f}€")
