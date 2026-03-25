def criar_jogo(palavra_secreta, max_tentativas=6):
    jogo = {
        "palavra": palavra_secreta.lower(),
        "letras_certas": [],
        "letras_erradas": [],
        "erros": 0,
        "max_tentativas": max_tentativas
    }
    return jogo


def tentar_letra(jogo, letra):
    letra = letra.lower()

    if letra in jogo["letras_certas"] or letra in jogo["letras_erradas"]:
        return False

    if letra in jogo["palavra"]:
        jogo["letras_certas"].append(letra)
    else:
        jogo["letras_erradas"].append(letra)
        jogo["erros"] += 1

    return True


def venceu(jogo):
    for letra in jogo["palavra"]:
        if letra not in jogo["letras_certas"]:
            return False
    return True


def perdeu(jogo):
    return jogo["erros"] >= jogo["max_tentativas"]


def mostrar_situacao(jogo):
    resultado = []

    for letra in jogo["palavra"]:
        if letra in jogo["letras_certas"]:
            resultado.append(letra)
        else:
            resultado.append("_")

    return " ".join(resultado)
