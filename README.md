# Projeto: Pagamento de Afiliados da Upbet

## Descrição do Projeto:

O projeto consistiu em desenvolver uma solução para calcular os pagamentos de afiliados com base nos dados de apostas fornecidos e aplicar as porcentagens determinadas pelas regras estabelecidas.

## Abordagem:

Análise dos Dados: Iniciamos o projeto analisando os dados fornecidos, que incluíam informações sobre apostas, clientes e afiliados.

Conexão com o Banco de Dados: Utilizamos a biblioteca SQLAlchemy para estabelecer uma conexão com o banco de dados PostgreSQL, onde os dados de apostas e clientes estavam armazenados.

Cálculo dos Pagamentos: Desenvolvemos um algoritmo para calcular os pagamentos dos afiliados com base nas porcentagens definidas e nos valores de apostas registrados no banco de dados.

Processamento de Dados com Pandas: Utilizamos a biblioteca Pandas para manipular e processar os dados de forma eficiente, realizando operações como agrupamento, filtragem e cálculos agregados.

## Funcionalidades

- **Calcular Pagamento**: O script lê os dados do arquivo CSV "affiliates.csv" e calcula os pagamentos com base em uma lógica específica.
- **Aplicar Cálculo aos Dados**: O script aplica a função de cálculo a cada linha na coluna "payment" do DataFrame lido do arquivo CSV.
- **Salvar Resultados**: O DataFrame resultante, incluindo os pagamentos calculados, é salvo em um novo arquivo CSV.

## Utilização

1. Certifique-se de ter os requisitos instalados (Python 3.x e pandas).
2. Coloque seu arquivo CSV de pagamentos com o nome `affiliates.csv` na mesma pasta que o script `pagamento.py`.
3. Execute o script `pagamento.py`.
4. O script calculará os pagamentos e salvará os resultados em um arquivo CSV chamado `affiliates_calculated.csv` na mesma pasta.

