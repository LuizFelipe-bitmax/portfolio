import pandas as pd
import numpy as np

caminho = "projeto/analise_dados_pandas/dados/diamonds.csv"

def carregar_csv(caminho):
    dados = pd.read_csv(caminho)
    return dados

def mostrar_info(dados):
    print("Informações:")
    print(pd.info())

def mostrar_estatisticas_basicas(dados):
    print("Estatisticas")
    print(pd.describe())

def verificar_nulos(dados):
    print("Mostrar dados")
    print(pd.isnull().sum())

def calcular_estatisticas_preco(dados):
    media = np.mean(dados["price"])
    mediana = np.median(dados["price"])
    print("Media:",media)
    print("Mediana:",mediana)

def analiser_corte(dados):
    print("Preço medio por tipo de corte:")
    print(dados.groupby("cut")["price"].mean())

def quantidade_cor(dados):
    print("Quantidade de dados:")
    print(dados["color"].value_counts())

def salvar_dados(dados):
    dados_filtrados = dados[dados["price"]>1000]
    dados_filtrados.to_csv("projeto5/dados/diamonds_filtrados.csv",index=False)
    print("Arquivo filtrado salvo!")

