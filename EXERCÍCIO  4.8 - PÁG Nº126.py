# Reescrever o Prob 4.4 da operadora Tchau usando o "else"

#    Dados:
# PLANO FALO POUCO: 100 minutos, preço 50€, minutos extra 0.20€/minuto.
# PLANO FALO MUITO: 500 minutos, preço 99€, minutos extra 0.15€/minuto.

#    Problema:
# Um programa que pergunte o plano e a quantidade de minutos consumida e depois
# calcular o preço a pagar. Se não for nenhum plano, não se calcula o preço.


plano_da_operadora = input("Qual é o seu plano? (falopouco / falomuito) ").strip().lower()
total_minutos_gastos = int(input("Quantos minutos gastou no total? "))

if plano_da_operadora == "falopouco":
    CUSTO_PLANO = 50
    MINUTOS_INCLUIDOS = 100
    PRECO_MINUTO_EXTRA = 0.20

    if total_minutos_gastos <= MINUTOS_INCLUIDOS:
        custo_total = CUSTO_PLANO
    else:
        minutos_extra = total_minutos_gastos - MINUTOS_INCLUIDOS
        custo_total = CUSTO_PLANO + minutos_extra * PRECO_MINUTO_EXTRA

    print(f"Vai pagar {custo_total}€ pelo plano falopouco.")

else:
    if plano_da_operadora == "falomuito":
        CUSTO_PLANO = 99
        MINUTOS_INCLUIDOS = 500
        PRECO_MINUTO_EXTRA = 0.15

        if total_minutos_gastos <= MINUTOS_INCLUIDOS:
            custo_total = CUSTO_PLANO
        else:
            minutos_extra = total_minutos_gastos - MINUTOS_INCLUIDOS
            custo_total = CUSTO_PLANO + minutos_extra * PRECO_MINUTO_EXTRA

        print(f"Vai pagar {custo_total}€ pelo plano falomuito.")
    else:
        print("Plano inválido. Não é possível calcular o preço.")

# IMPORTANTE:
# FAZER MAIS TARDE: Simplificar isto com elif, fazer uma versão onde o utilizador escolhe o plano por número (1 ou 2)
