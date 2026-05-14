# PROBLEMA 4.1.1
# Cáculo de IMPOSTO A PAGAR

# DADOS:
# Salários menores que 1000€ NÃO PAGAM IMPOSTO(0%)
# 1000 =< pagam 20% <= 3000€
# > 3000€ pagam 35%

salario = float(input(f"Digite o valor do seu slário:"))


if salario < 1000:
    imposto = 0

if salario >= 1000 and salario <= 3000:  
    imposto = 20

if salario > 3000:
    imposto = 35


valor_a_pagar = salario*imposto/100

print(f"Imposto a pagar {valor_a_pagar:.2f}€")
