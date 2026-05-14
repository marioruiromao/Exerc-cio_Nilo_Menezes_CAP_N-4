# PROB 4.6 - PÁG 126

# Escrever um programa que calcule o preço de uma viagem. Os primeiros 200Km
# custam 0.50€/Km, depois passam para 0.45€/Km.

km_percorridos = float(input("Quantos quilómetros vai viajar? "))

ATÉ_200 = 0.50
DEPOIS_DE_200 = 0.45

if km_percorridos <= 200:
    custo_viagem = km_percorridos * ATÉ_200
 
else:
    custo_viagem = 200 * ATÉ_200 + (km_percorridos - 200) * DEPOIS_DE_200
 

print(f"A sua viagem custar-lhe-á: {custo_viagem:.2f}€ ")




# ------ UMA VERSÃO MAIS PYTHONIC ------



km = float(input("Quantos quilómetros vai viajar? "))

PRECO_ATE_200 = 0.50
PRECO_DEPOIS_200 = 0.45

if km <= 200:
    custo = km * PRECO_ATE_200
else:
    excedente = km - 200
    custo = 200 * PRECO_ATE_200 + excedente * PRECO_DEPOIS_200

print(f"A sua viagem custar-lhe-á: {custo:.2f}€")
