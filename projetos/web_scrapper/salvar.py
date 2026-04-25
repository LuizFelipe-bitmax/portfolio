from pathlib import Path
import csv

def salvar_csv(dados):

    BASE_DIR = Path(__file__).resolve().parent
    caminho = BASE_DIR / "data" / "resultado.csv"

    caminho.parent.mkdir(exist_ok=True)

    if not dados:
        return
    
    chaves = dados[0].keys()

    with open(caminho, mode="w", newline="", encoding="utf-8") as arquivo:
        writer = csv.DictWriter(arquivo, fieldnames=chaves)
        writer.writeheader()
        writer.writerows(dados)

    print("SALVO EM:", caminho)
