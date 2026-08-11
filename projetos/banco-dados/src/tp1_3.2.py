import argparse
import psycopg2
import re
from datetime import datetime

def parse_amazon_file(file_path):
    products = []
    with open(file_path, "r", encoding="utf-8") as f:
        current = {}
        reviews = []
        for line in f:
            line = line.strip()
            if line.startswith("Id:"):
                if current:
                    current["reviews"] = reviews
                    products.append(current)
                    current = {}
                    reviews = []
            elif line.startswith("ASIN:"):
                current["ASIN"] = line.split(":",1)[1].strip()
            elif line.startswith("title:"):
                current["title"] = line.split(":",1)[1].strip()
            elif line.startswith("group:"):
                current["group"] = line.split(":",1)[1].strip()
            elif line.startswith("salesrank:"):
                val = line.split(":",1)[1].strip()
                current["salesrank"] = int(val) if val.isdigit() else None
            elif line.startswith("similar:"):
                parts = line.split()
                current["similar"] = parts[2:]  
            elif line.startswith("categories:"):
                current["categories"] = []
            elif line.startswith("|"):
                current["categories"].append(line.strip())
            elif re.match(r"\d{4}-\d{1,2}-\d{1,2} customer:", line):
                reviews.append(line)
        if current:
            current["reviews"] = reviews
            products.append(current)
    return products

def connect(args):
    return psycopg2.connect(
        host=args.db_host,
        port=args.db_port,
        dbname=args.db_name,
        user=args.db_user,
        password=args.db_pass
    )

def insert_data(conn, products):
    cur = conn.cursor()
    
    for p in products:
        # Produto
        cur.execute(
            "INSERT INTO Produto (ASIN, Titulo, Grupo, SalesRank) VALUES (%s,%s,%s,%s) ON CONFLICT (ASIN) DO NOTHING",
            (p.get("ASIN"), p.get("title"), p.get("group"), p.get("salesrank"))
        )
        
        # Categoria e ProdutoCategoria
        for idx, cat in enumerate(p.get("categories", []), start=1):
            cat_name = cat.split("|")[-1].split("[")[0].strip()
            cur.execute(
                "INSERT INTO Categoria (CategoriaID, Nome) VALUES (%s,%s) ON CONFLICT (CategoriaID) DO NOTHING",
                (idx, cat_name)
            )
            cur.execute(
                "INSERT INTO ProdutoCategoria (ASIN, CategoriaID) VALUES (%s,%s) ON CONFLICT DO NOTHING",
                (p.get("ASIN"), idx)
            )
        
        
        for similar_asin in p.get("similar", []):
            if similar_asin != p.get("ASIN"):
                cur.execute(
                    "INSERT INTO Similares (ASIN1, ASIN2) VALUES (%s,%s) ON CONFLICT DO NOTHING",
                    (p.get("ASIN"), similar_asin)
                )
        
        
        for r in p.get("reviews", []):
            m = re.match(r"(\d{4}-\d{1,2}-\d{1,2}) customer: (\S+) rating: (\d) votes: (\d+) helpful: (\d+)", r)
            if m:
                date_str, cliente_id, rating, votes, helpful = m.groups()
                date_obj = datetime.strptime(date_str, "%Y-%m-%d").date()
                

                cur.execute(
                    "INSERT INTO Cliente (ClienteID) VALUES (%s) ON CONFLICT (ClienteID) DO NOTHING",
                    (cliente_id,)
                )
                

                cur.execute(
                    "INSERT INTO Avaliacao (ASIN, ClienteID, Data, Rating, Votes, Helpful) VALUES (%s,%s,%s,%s,%s,%s)",
                    (p.get("ASIN"), cliente_id, date_obj, int(rating), int(votes), int(helpful))
                )
                
    conn.commit()
    cur.close()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--db-host", required=True)
    parser.add_argument("--db-port", required=True, type=int)
    parser.add_argument("--db-name", required=True)
    parser.add_argument("--db-user", required=True)
    parser.add_argument("--db-pass", required=True)
    parser.add_argument("--input", required=True)
    args = parser.parse_args()

    products = parse_amazon_file(args.input)
    conn = connect(args)
    insert_data(conn, products)
    conn.close()
    print(f"{len(products)} produtos inseridos (com categorias, similares, clientes e avaliações).")

if __name__ == "__main__":
    main()
