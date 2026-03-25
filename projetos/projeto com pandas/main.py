from loader import carregar_dados_csv
from analyzer import informações

def main():
    print("Programa iniciando")
    caminho = "projeto4/data/dados.csv"
    df = carregar_dados_csv(caminho)

    if df is None:
        return
    
    informações(df)


if __name__ == "__main__":
    main()
