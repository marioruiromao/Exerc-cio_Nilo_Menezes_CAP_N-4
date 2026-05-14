#EXERCÍCIO 4.2 - NILO MENEZES

velocidade_carro = int(input("Qual a velocidade a que conduzia?"))

if velocidade_carro <= 80:
    print("A conduzir dentro da velocidade regulamentar")
if velocidade_carro > 80: # O 2º if é desnecessário e torna o programa mais lento. Evitar!
    print("Foi multado")
    multa = (velocidade_carro - 80) * 5
    print(f"A multa é de {multa}€")

# SUPER NOTA: #Regra de ouro para nunca te enganares:

#print() → mostrar informação  
#input() → pedir informação

# SUPER IMPORTANTE: Misturar os dois na mesma linha quase nunca faz sentido.


#  ---------- VERSÃO OTIMIZADA ----------

#  ALINHADA COM O EXERCICIO:

velocidade = int(input("Qual a velocidade a que conduzia? "))
limite = 80 # Ter presente esta condição, MUITO IMPORTANTE!!

if velocidade > limite:
    multa = (velocidade - limite) * 5
    print(f"Foi multado. Multa: {multa}€")

if velocidade <= limite: # Os 2 if não é a forma mais eficiente, mas para já, serve com base nos meu conhecimentos.
    print("Dentro da velocidade regulamentar")
