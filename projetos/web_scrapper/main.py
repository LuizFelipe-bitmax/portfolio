from scraper import obter_html
from parser import extrair_dados
from salvar import salvar_csv
from logger_config import configurar_log

def main():
    logger = configurar_log()

    base_url = "http://quotes.toscrape.com"
    url = base_url

    todos_dados = []

    logger.info("Iniciando scraper com paginação")

    while url:
        print(f"Acessando: {url}")

        html = obter_html(url, logger)

        if html is None:
            print("Erro ao acessar o site.")
            break

        dados, proxima = extrair_dados(html, logger)

        if not dados:
            print("Nenhum dado encontrado.")
            break

        todos_dados.extend(dados)

        if proxima:
            url = base_url + proxima
        else:
            url = None

    salvar_csv(todos_dados)

    logger.info(f"Total coletado: {len(todos_dados)}")
    print("Scraping finalizado com paginação!")

if __name__ == "__main__":
    main()
