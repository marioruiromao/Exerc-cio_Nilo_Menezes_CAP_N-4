
velocidade_carro = int(input("Qual é a velocidade do carro(Km/h)?"))

if velocidade_carro > 80:
    print("Você foi multado")
    multa = (velocidade_carro - 80)*5
    print(f"A sua multa é de {multa} Euros")

if velocidade_carro <= 80:
    print("A conduzir dentro da velocidade regulamentar")
    







