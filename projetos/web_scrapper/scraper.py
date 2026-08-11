import requests

def obter_html(url,logger):
    try:
        headers = {
            "User-Agent" : "Mozilla/5.0"
        }

        resposta = requests.get(url,headers=headers,timeout=10)
        resposta.raise_for_status()

        logger.info("Bem sucedido")
        return resposta.text
    
    except requests.exceptions.RequestException as erro:
        logger.erro(f"Erro na aquisição: {erro}")
        return None
    
