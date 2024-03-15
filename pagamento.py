import pandas as pd

# Carregar os dados do arquivo CSV "affiliates.csv"
affiliates_df = pd.read_csv("affiliates.csv")

# Definir a função para calcular o pagamento
def calcular_pagamento(payment):
    if payment <= 100:
        return 0.10 * payment
    elif payment <= 200:
        return 0.15 * payment
    elif payment <= 300:
        return 0.20 * payment
    elif payment <= 400:
        return 0.25 * payment
    elif payment <= 500:
        return 0.30 * payment
    else:
        return 0.50 * payment

# Aplicar a função de cálculo para cada linha na coluna "payment" da tabela "affiliates"
affiliates_df["calculated_payment"] = affiliates_df["payment"].apply(calcular_pagamento)

# Exibir o DataFrame com os pagamentos calculados
print(affiliates_df)
# Salvar o DataFrame em um arquivo CSV
affiliates_df.to_csv("affiliates_calculated.csv", index=False)
