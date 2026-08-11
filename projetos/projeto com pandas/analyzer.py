import pandas as pd

def informações(df):
    return df.info()

def primeiras_linhas(df):
    return df.head()

def descrição(df):
    return df.describe()

def valores_nulos(df):
    return df.isnull().sum()

def valores_unicos(df):
    return df.nunique()

def valores_diferentes(df, coluna):
    return df[coluna].unique()

def tamanho_database(df):
    linhas,colunas = df.shape
    print("Linhas:",linhas)
    print("Colunas:",colunas)

def nomes_colunas(df):
    return df.columns

def tipos_dados(df):
    return df.dtypes

def valor_maximo(df):
    return df.max()

def valor_minimo(df):
    return df.min()

def ver_nomes(df):
    return df["nome"].value_counts()
