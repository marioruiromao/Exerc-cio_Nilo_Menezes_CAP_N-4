
v_1 = int(input("Primeiro valor:  "))

v_2 = int(input("segundo valor:   "))

if v_1 > v_2:
    print("O primeiro valor é o maior!")

if v_2 > v_1:
    print("O segundo valor é o maior!")


# Quando digito 2 número iguais e não aparece "nada", é porque não defini a condição para esse caso, que é o caso do programa acima.

# Deveria ser:

a = int(input("Digite um número: "))
b = int(input("Digite outro número: "))

if a > b:
    print("O primeiro é maior")
elif a < b:
    print("O segundo é maior")
elif a == b:
    print("Os números são iguais")

# Ou então com else

a = int(input("Digite um número: "))
b = int(input("Digite outro número: "))

if a > b:
    print("O primeiro é maior")
elif a < b:
    print("O segundo é maior")
else:
    print("Os números são iguais")

# Aqui o else funciona porque se não é maior nem menor, só pode ser igual.