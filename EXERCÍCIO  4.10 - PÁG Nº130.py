
# Programa que:
# 1. Pergunta 2 números ao utilizador
# 2. Pergunta qual operação quer realizar (+, -, *, /)
# 3. Mostra o resultado ou um erro se a operação não existir
# ________________________________________________________________________________________________________________________________________

# Explicação:

# Esta linha imprime a mensagem no ecrã.
# NOTA: não faz sentido guardar o resultado de print() numa variável, EX: menssagem = print("Digite 2 números, quaisquer, à sua escolha!")
# porque print() devolve sempre None. Por isso removemos a variável.
print("Digite 2 números, quaisquer, à sua escolha!")

# input() lê texto; float() converte esse texto para número decimal.
# Aqui guardamos o primeiro número na variável 'a'.
a = float(input("O primeiro número: "))

# O mesmo para o segundo número.
b = float(input("E agora o segundo número: "))

# Aqui pedimos ao utilizador que escolha a operação.
# O valor lido é sempre uma STRING, por isso vamos compará-lo com "+", "-", "*", "/".
operacao = input("Escolha a operação a realizar: (+, -, *, /) ")

# Criamos uma variável booleana (True/False) para indicar se a operação é válida. Usar uma variável booleana como valido = True é uma técnica simples 
# e explícita para controlar fluxo de validação durante a execução. Começa como True e só muda para False se o utilizador escrever algo errado.
valido = True

# Cada condição calcula o resultado e guarda-o SEMPRE na mesma variável: 'resultado'. Isto é importante porque no final queremos imprimir apenas uma variável.
if operacao == "+":
    resultado = a + b      
elif operacao == "-":
    resultado = a - b      
elif operacao == "*":
    resultado = a * b      
elif operacao == "/":
    resultado = a / b      
else:
    # Se não for nenhuma das opções acima, marcamos como inválido.
    valido = False
# Aqui verificamos se a operação era válida,'not valido' significa "se valido for False".
if not valido:
    # Mostramos uma mensagem de erro indicando a operação desconhecida.
    print(f"Erro: não conheço essa operação: {operacao}")
else:
    print(f"O resultado da sua escolha é: {resultado:10.2f}")
