
# Corrigir o exercício:

# média = input("Digite sua média:")

# if média < 4:
    # print("Infelizmente você reprovou")
# if média < 7:
    # print("Você ficou de recuperação")
# if média > 7:
    # print("Você passou de ano")


# RESOLUÇÃO: -------------------------------------------

media = float(input("Digite a sua média: "))

if media < 4:
    print("Infelizmente reprovou!")

elif media < 7:
    print("Você tem que repetir o exame")

else:
    print("Parabéns, passou!")
