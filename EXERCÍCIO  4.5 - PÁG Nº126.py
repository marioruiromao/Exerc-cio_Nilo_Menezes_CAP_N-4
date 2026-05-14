# Problema 4.5 - PÁG126

# Um programa que pergunte a velocidade de um carro.
# Se ultrapassar os 80Km/h dizer que foi multado.
# Mostrar a multa que é de 5€ por cada Km a mais dos 80Km/h.

velocidade_carro = int(input("A que velocidade se desloca o carro? "))

if velocidade_carro > 80:
    print("Foi multado!")
    valor_multa = (velocidade_carro - 80)*5
    print(f"A sua multa foi de {valor_multa}€")
else:
    print("Não foi multado")




# OUTRA VERSÃO + PYTHONIC

velocidade = int(input("A que velocidade se desloca o carro? "))

if velocidade <= 80:
    print("Não foi multado.")
else:
    multa = (velocidade - 80) * 5
    print(f"Foi multado! A multa é de {multa:.2f}€.")
