# Fazer um programa que leia 5 categorias e determine o preço dessa categoria usando o "elif"
# categoria X preço
# Ver tabela 4.1

categoria = int(input("Digite a categoria do produto: "))

if categoria == 1:
    preço = 10
elif categoria == 2:
    preço = 18
elif categoria == 3:
    preço = 23
elif categoria == 4:
    preço = 26
elif categoria == 5:
    preço = 31

else:
    print("categoria inválida, digite um número entre 1 e 5")
    preço = 0

print(f"O preço do produto é de {preço:8.2f}")
