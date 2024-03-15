import pandas as pd
from sqlalchemy import create_engine

# Parâmetros de conexão ao banco de dados PostgreSQL
DB_USER = 'bear'
DB_PASSWORD = 'dev!!!00'
DB_HOST = '144.22.211.147'
DB_PORT = 5436
DB_NAME = 'upbet'

# String de conexão ao banco de dados
connection_string = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

# Conectar ao banco de dados
engine = create_engine(connection_string)

# Consultar os dados da tabela bets
query_bets = "SELECT * FROM bets;"
df_bets = pd.read_sql_query(query_bets, engine)

# Criar DataFrame com customer_id únicos e somar os valores de amount e win correspondentes
df_customer_summary = df_bets.groupby('customer_id').agg({'amount': 'sum', 'win': 'sum'}).reset_index()

# Exibir o DataFrame
print(df_customer_summary)

# Fechar a conexão com o banco de dados
engine.dispose()
# Salvar o DataFrame em um arquivo CSV
df_customer_summary.to_csv('customer_summary.csv', index=False)

