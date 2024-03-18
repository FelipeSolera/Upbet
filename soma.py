import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

def connection(DB_USER,DB_PASSWORD,DB_HOST,DB_PORT,DB_NAME):
    connection_string = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
    engine = create_engine(connection_string)
    return engine

def query(engine, query):
    df_bets = pd.read_sql_query(query, engine)
    return df_bets


def transformation(df):
    df_customer_summary = df.groupby('customer_id').agg({'amount': 'sum', 'win': 'sum'}).reset_index()
    print(df_customer_summary)
    return df_customer_summary

def write_dataframe(df, path):
    df.to_csv(path, index=False)

load_dotenv()

# Parâmetros de conexão ao banco de dados PostgreSQL
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')    

engine = connection(DB_USER,DB_PASSWORD,DB_HOST,DB_PORT,DB_NAME)

query_bets = "SELECT * FROM bets;"
df_bets = query(engine, query_bets)
df_customer_summary = transformation(df_bets)
engine.dispose()
write_dataframe(df_customer_summary, 'customer_summary.csv')

