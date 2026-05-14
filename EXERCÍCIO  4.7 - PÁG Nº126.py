# Analise o Prob 4.3, e diga se faz sentido usar o "else". Justifique!

# Prob.4.3 - Escreva um programa que leia 3 valores e que imprima o maior e o menor.


v_1 = int(input("Digite um número: "))
v_2 = int(input("Digite outro número: "))
v_3 = int(input("Digite o último número: "))

# Maior
if v_1 >= v_2 and v_1 >= v_3:
    print(f"O maior valor é {v_1}")

if v_2 >= v_1 and v_2 >= v_3:
    print(f"O maior valor é {v_2}")

if v_3 >= v_1 and v_3 >= v_2:
    print(f"O maior valor é {v_3}")

# Menor
if v_1 <= v_2 and v_1 <= v_3:
    print(f"O menor valor é {v_1}")

if v_2 <= v_1 and v_2 <= v_3:
    print(f"O menor valor é {v_2}")

if v_3 <= v_1 and v_3 <= v_2:
    print(f"O menor valor é {v_3}")


#JUSTIFICAÇÃO:
    
# Como não existe relação de exclusão direta, não existe motivo para usar "else".
# Nenhuma delas é o “contrário” da outra. Se v_1 não é o maior, isso não
# significa que v_2 é o maior, pois pode ser v_3
