Projeto Amazon — TP01
📌 Descrição

Este projeto implementa as metas de um trabalho academico da disciplina de Banco de Dados.
Ele utiliza PostgreSQL e Python dentro de containers Docker para:

Criar o esquema do banco.

Carregar os dados do arquivo snap_amazon.txt.

Executar consultas SQL de análise.

📂 Estrutura do Projeto
TP01/
├─ data/          # Arquivos de entrada (ex: snap_amazon.txt)
├─ out/           # Arquivos de saída (CSV, logs, resultados)
├─ sql/           # Scripts SQL (schema_postgresql.sql, tp1_queries.sql)
├─ src/           # Scripts Python (tp1_3.2.py, tp1_3.3.py)
├─ docker-compose.yml
├─ Dockerfile
├─ requirements.txt
├─ README.md

🚀 Como Executar
1️⃣ Subir os serviços

Este comando inicia o banco de dados PostgreSQL e o container Python:

docker compose up -d --build

2️⃣ Criar o esquema no banco

O esquema está no arquivo sql/schema_postgresql.sql.
Para aplicar manualmente:

docker exec -i tp01-db psql -U postgres -d tp01 < sql/schema_postgresql.sql


Obs: tp01-db é o nome do serviço configurado no docker-compose.yml.

3️⃣ Carregar os dados

Rodar o script tp1_3.2.py para inserir os dados de data/snap_amazon.txt no banco:

docker exec -it tp01-app python src/tp1_3.2.py

4️⃣ Executar as consultas

Rodar o script tp1_3.3.py para executar as queries em sql/tp1_queries.sql
e salvar os resultados em out/:

docker exec -it tp01-app python src/tp1_3.3.py

📊 Resultados

Os resultados das consultas ficam salvos na pasta out/.

Cada query gera um arquivo CSV separado, que pode ser aberto em qualquer editor de planilhas ou analisado via Python.

🛠 Tecnologias

Python 3.11 (slim)

PostgreSQL 15

Docker + Docker Compose
