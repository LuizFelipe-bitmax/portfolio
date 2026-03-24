import json

ARQUIVO = "tasks.json"

def carregar_tarefas():
    try:
        with open(ARQUIVO,"r",encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []
    
def salvar_tarefas(tarefas):
    with open(ARQUIVO,"w",encoding="utf-8") as arquivo:
        return json.dump(arquivo,tarefas,indent=4,ensure_ascii=False)
