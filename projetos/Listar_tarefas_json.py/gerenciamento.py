import json

ARQUIVOS = "usuario.json"

def carregar_usuarios():
    try:
        with open(ARQUIVOS,"r",encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []
    
def salvar_usuarios(usuarios):
    with open(ARQUIVOS,"w",encoding="utf-8") as arquivo:
        json.dump(usuarios,arquivo,indent=4,ensure_ascii=False)
