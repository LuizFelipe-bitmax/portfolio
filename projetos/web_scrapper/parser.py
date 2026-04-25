from bs4 import BeautifulSoup

def extrair_dados(html, logger):
    try:
        soup = BeautifulSoup(html, "html.parser")

        dados = []

        itens = soup.select(".quote")

        for item in itens:
            texto_tag = item.select_one(".text")
            autor_tag = item.select_one(".author")

            texto = texto_tag.get_text(strip=True) if texto_tag else "N/A"
            autor = autor_tag.get_text(strip=True) if autor_tag else "N/A"

            dados.append({
                "texto": texto,
                "autor": autor
            })

        logger.info(f"{len(dados)} itens extraídos")
        return dados

    except Exception as erro:
        logger.error(f"Erro ao extrair dados: {erro}")
        return []
