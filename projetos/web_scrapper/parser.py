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

        proxima_pagina = soup.select_one(".next a")
        if proxima_pagina:
            link = proxima_pagina.get("href")
        else:
            link = None

        logger.info(f"{len(dados)} itens extraídos")
        return dados, link

    except Exception as erro:
        logger.error(f"Erro ao extrair dados: {erro}")
        return [], None
