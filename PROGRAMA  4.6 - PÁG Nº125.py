
# PROBLEMA: Lê 2 valores e imprime o que for maior.
# Usar "ELSE"

valor_1 = float(input("Digite um valor à sua escolha: "))
valor_2 = float(input("Digite outro valor: "))

if valor_1 > valor_2:
    print(f"Este valor {valor_1:.2f} é maior que {valor_2:.2f}")
else:
    print(f"O valor {valor_2:.2f} é maior que {valor_1:.2f} ")
