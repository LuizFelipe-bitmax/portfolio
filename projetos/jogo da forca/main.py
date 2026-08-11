from game import criar_jogo,tentar_letra,venceu,perdeu,mostrar_situacao
from words import escolher_palavra

def main():
    PALAVRA = escolher_palavra()
    jogo = criar_jogo(PALAVRA)
    print("---JOGO DA FORCA---")
    while True:
        print("\nPalavra:",mostrar_situacao(jogo))
        print("Erros",jogo["erros"], "/" , jogo["max_tentativas"])
        print("Letras erradas:", ", ".join(jogo["letras_erradas"]))

        letra = input("Coloque uma letra:").strip()

        if len(letra) != 1 or not letra.isalpha():
            print("Coloque uma letra valida")
            continue

        tentativa_valida = tentar_letra(jogo,letra)

        if not tentativa_valida:
            print("Você ja tentou essa letra,digite outra")
            continue

        if venceu(jogo):
            print("PARABENS")
            break
        if perdeu(jogo):
            print("tente novamente!")
            break

if __name__ == "__main__":
    main()
