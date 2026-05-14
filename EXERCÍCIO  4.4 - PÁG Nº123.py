# Perguntar o salário e aumentar os superiores a 1,250.00€ em 10% e os restantes 15%.

salario = float(input("Qual o valor do seu salário?"))

if salario <= 1_250.00:
    percentagem = 15

if salario > 1_250.00:
    percentagem = 10

aumento = salario * percentagem / 100

print(f"O seu aumento será de {aumento:.2f}")


# SUPER NOTA: Resumo do resumo

#     ATENÇÃO, quando é CÓDIGO:

# milhares → _
# decimais → .

#     ATENÇÃO, quando é OUTPUT:

# casas decimais → :.2f
# milhares → :,



