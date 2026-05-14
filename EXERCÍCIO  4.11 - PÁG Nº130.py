
# Prob de um empréstimo bancário em que:

# 1 - Valor da casa;
# 2 - A duração dos anos a pagar o empréstimo;
# 4 - O empréstimo não pode ultrapassar 30% do salário;
# 5 - A prestação deve ser definida pelo valor da casa a dividir pelos meses a pagar.


valor_casa = float(input("Qual é o valor de aquisição da casa? "))
salario = float(input("Qual é o valor do seu ordenado? "))
anos_de_empréstimo = int(input("Durante quantos anos vai pagar empréstimo bancário "))

duração_do_empréstimo = anos_de_empréstimo * 12
prestacao_mensal = valor_casa / duração_do_empréstimo
limite_da_prestação = salario * 0.30

if prestacao_mensal <= limite_da_prestação:
    print(f"O seu empréstimo está aprovado no valor de{limite_da_prestação:8.2f}€ mensais")
else:
    print("O seu empréstimo não foi aprovado!")


#   ____ SOLUÇÃO DO NILO ____

# INFO mais simples

valor = float(input("Digite o valor da casa: "))
salário = float(input("Digite o salário: "))
anos = int(input("Quantos anos para pagar: "))

meses = anos * 12
prestacao = valor / meses

if prestacao > salário * 0.3:
    print("Infelizmente você não pode obter o empréstimo")
else:
    print(f"Valor da prestação: R$ {prestacao:7.2f} Empréstimo OK")

 
