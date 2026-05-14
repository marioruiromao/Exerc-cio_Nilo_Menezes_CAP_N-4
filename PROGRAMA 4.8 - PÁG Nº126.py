# Fazer um programa que leia 5 categorias e determine o preço dessa categoria.
# categoria X preço

categoria = int(input("Digite a categoria do produto."))

if categoria == 1:
    preco = 10
else:
    if categoria == 2:
        preco = 18
    else:
        if categoria == 3:
            preco = 23
        else:
            if categoria == 4:
                preco = 26
            else:
                if categoria == 5:
                    preco = 31
                else:
                    print("Categoria invalida, digite um valor entre 1 e 5")
                    preco = 0

print(f"O preço do produto é {preco:8.2f}€")
                    

# IMPORTANTE:

# Visão geral do == em Python:

# O == em Python é o operador de igualdade de valor. Ele compara dois
# operandos (variáveis, literais, expressões) e devolve um booleano:

# True - se os valores forem considerados iguais;
# False - caso contrário.

#Diferença entre =, == e is
#  = (atribuição): coloca um valor dentro de uma variável.
#  == (igualdade de valor): compara se os valores são iguais.
#  is (identidade): verifica se duas variáveis apontam para o mesmo objeto na memória.

# Regra mental:
# Quer saber se “tem o mesmo valor”? → usa "=="
# Quer saber se “é exatamente o mesmo objeto”? → usa "is"
