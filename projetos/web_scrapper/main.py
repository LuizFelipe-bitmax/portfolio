from scraper import obter_html
from parser import extrair_dados
from salvar import salvar_csv
from logger_config import configurar_log


def main():

    logger = configurar_log()

    url = "http://quotes.toscrape.com"

    html  = obter_html(url,logger)


    if html is None:
        print("Não foi possivel acessar site")
        return
    
    dados = extrair_dados(html,logger)

    if not dados:
        print("Nenhum dado encontrado")
        return
    

    
    salvar_csv(dados)
    
    logger.info("Bem sucedido")
    print("Scraper finalizado")

if __name__ == "__main__":
    main()
