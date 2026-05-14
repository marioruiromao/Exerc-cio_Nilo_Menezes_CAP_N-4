
# EXERCÍCIO 4.14 - Rescrever o programa com if-elif-else e adicione as linhas necessárias para o executar.

# if a < 10:
    # print("a é menor que 10")
# if a >= 10 and a < 20:
    # print("a é maior que 10 e menor que 20")
# if a >= 20:
    # print("a é maior que 20")

# RESOLUÇÃO: -----------------------------------------------------------------------------------------------

a = float(input("Digite um número à sua escolha:  "))

if a < 10:
    print("a é menor que 10")
elif a < 20:
    print("a está entre 10 e 20")
else:
    print("a é maior ou igual a 20")
