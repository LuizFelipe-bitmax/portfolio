import random

PALAVRAS = [
    "python",
    "computador",
    "programacao",
    "desenvolvedor",
    "algoritmo",
    "variavel",
    "funcoes",
    "estrutura",
    "backend",
    "frontend"
]

def escolher_palavra():
    return random.choice(PALAVRAS)
