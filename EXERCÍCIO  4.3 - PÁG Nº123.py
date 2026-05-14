# Escreva um programa que peça 3 números e imprima o maior e o menor

n_1 = float(input("Digite um número:"))
n_2 = float(input("Digite mais um número:"))
n_3 = float(input("Digite um último número:"))

# Vamos começar por encontrar o MAIOR número:

if n_1 >= n_2 and n_1 >= n_3:
   maior = n_1

if n_2 >= n_1 and n_2 >= n_3:
    maior = n_2

if n_3 >= n_1 and n_3 >= n_2:
    maior = n_3

# Vamos, agora, encontrar o MENOR número:

if n_1 <= n_2 and n_1 <= n_3:
    menor = n_1

if n_2 <= n_1 and n_2 <= n_3:
    menor = n_2 

if n_3<= n_1 and n_3 <= n_2:
    menor = n_3 

print(f"O maior número é o {maior:10.2f} e o menor número é o {menor:10.2f}")
