# 🏷️ Controle de Estoque

Aplicação web simples em **Flask + SQLite** para gerenciar produtos, categorias e movimentações de estoque.  
Serve como exemplo de relacionamento **1:N (Categoria → Produto)** e base para relatórios e gráficos.

---

## 🚀 Funcionalidades

- ✅ **Categorias**: cadastro e listagem
- ✅ **Produtos**: cadastro, listagem e exclusão
- ✅ Relacionamento 1:N (cada produto pertence a uma categoria)
- 🕒 Preparado para incluir **movimentações** (entradas, saídas, devoluções)
- 📊 Futuro: **relatórios** e **gráficos** (estoque por categoria, evolução de entradas/saídas)
- 📁 Exportação planejada em **PDF/Excel**

---

## 🛠️ Tecnologias

- [Python 3](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/)
- [SQLite](https://www.sqlite.org/) (banco de dados local)
- [HTML/CSS](https://developer.mozilla.org/pt-BR/docs/Web) (frontend básico)

---

## ⚡ Como rodar localmente

```bash
# 1️⃣ Clone ou baixe este repositório
git clone https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git
cd projetos/controle-estoque

# 2️⃣ Crie e ative o ambiente virtual
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# 3️⃣ Instale as dependências
pip install -r requirements.txt

# 4️⃣ Inicie o servidor Flask
python app.py
