
# Programa para calcular o custo do preço de EE gasta;
# Perguntar os KWh consumidos;
# Tipo de instalação (R - residenciais, I - indústriais, C - comércio)
# Calcular o valor a pagar de acordo com a tabela.

# Exercício:

# Peço ao utilizador quantos KWh consumiu e converto para float
kwh = float(input("Quantos KWh consumiu este mês? "))

# Peço o tipo de instalação e converto para maiúsculas para evitar erros
instalacao = input("Indique a letra do seu tipo de instalação? R - residenciais, I - indústriais, C - comercial? ").upper()

# Variável para controlar se a instalação é válida - Boas práticas!
valido = True

# Verifico se a instalação é residencial
# NBH - coloco "==" porque estou a testar qual das hipóteses é verdadeira! 
if instalacao == "R": # NBH - Sempre que queres trabalhar com texto literal (palavras, letras, frases), tens de usar aspas. 
    if kwh < 500:
        preco = 0.40
    # Se consumiu menos de 500 KWh, aplica-se o preço mais barato, Caso contrário, aplica-se o preço mais caro.
    else:
        preco = 0.65

# Verifico se a instalação é comercial
elif instalacao == "C":
    # Preço depende se consumiu menos ou mais de 1000 KWh
    if kwh < 1000:
        preco = 0.55
    else:
        preco = 0.60

# Verifico se a instalação é industrial
elif instalacao == "I":
    # Preço depende se consumiu menos ou mais de 5000 KWh
    if kwh < 5000:
        preco = 0.55
    else:
        preco = 0.60

# Se não for nenhum dos tipos válidos, marco como inválido.
else:
    valido = False

# Se a instalação for inválida, aviso o utilizador
if not valido:
    print(f"Erro: Não conheço essa instalação '{instalacao}'")
    
# Caso contrário, calculo e mostro o preço final
else:
    preco_a_pagar = kwh * preco

    # Uso :.2f para mostrar apenas duas casas decimais
    print(f"Vai pagar: {preco_a_pagar:.2f}€")
