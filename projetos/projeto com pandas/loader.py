import pandas as pd

def carregar_dados_csv(caminho):
    try:
        return pd.read_csv(caminho)
    except FileNotFoundError:
        return
