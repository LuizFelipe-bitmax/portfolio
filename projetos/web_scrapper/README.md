# 🕸️ Web Scraper 

Projeto desenvolvido em Python para coleta automatizada de dados (frases e autores) a partir de páginas web, com tratamento de erros, sistema de logs e exportação estruturada em CSV.

---

## 📌 Sobre o Projeto

Este projeto simula um cenário real de backend onde é necessário:

* Consumir dados de uma página web
* Processar e extrair informações relevantes
* Garantir robustez com tratamento de erros
* Registrar logs para monitoramento
* Persistir dados de forma estruturada

---

## 🚀 Tecnologias Utilizadas

* Python
* Requests
* BeautifulSoup
* Logging (nativo do Python)
* CSV

---

## ⚙️ Funcionalidades

✔️ Requisição HTTP com tratamento de erros
✔️ Parsing de HTML com BeautifulSoup
✔️ Extração estruturada de dados (texto + autor)
✔️ Sistema de logs para rastreamento da execução
✔️ Salvamento automático em arquivo CSV
✔️ Organização modular do código

---

## 📂 Estrutura do Projeto

```
web_scraper/
│
├── main.py          # Arquivo principal (orquestra execução)
├── scraper.py       # Responsável pela requisição HTTP
├── parser.py        # Extração dos dados do HTML
├── salvar.py        # Persistência dos dados (CSV)
├── logger.py        # Configuração de logs
│
├── data/            # Arquivos gerados (CSV)
├── logs/            # Logs da aplicação
│
├── requirements.txt
└── README.md
```

---

## ▶️ Como Executar

### 1. Clonar o repositório

```bash
git clone https://github.com/seu-usuario/seu-repo.git
cd web_scraper
```

---

### 2. Instalar dependências

```bash
pip install -r requirements.txt
```

---

### 3. Executar o projeto

```bash
python main.py
```

---

## 📊 Saída

Após execução, o sistema irá gerar:

* 📄 `data/resultado.csv` → dados extraídos
* 📄 `logs/scraper.log` → registro da execução

---

## 🧠 Aprendizados

Este projeto reforça conceitos fundamentais de backend:

* Arquitetura modular
* Separação de responsabilidades
* Manipulação de dados reais
* Tratamento de exceções
* Uso de logs em aplicações
* Boas práticas de organização de código

---

## 🔥 Possíveis Melhorias

* Paginação automática (coletar múltiplas páginas)
* Persistência em banco de dados (PostgreSQL / MongoDB)
* Criação de API para exposição dos dados
* Agendamento automático (cron jobs)
* Containerização com Docker

---

## 👨‍💻 Autor

Luiz Felipe

---

## 📎 Observação

Projeto desenvolvido com foco em aprendizado prático e simulação de cenários reais de desenvolvimento backend.
