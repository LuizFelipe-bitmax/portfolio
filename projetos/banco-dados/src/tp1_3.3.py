import argparse
import psycopg2
from psycopg2.extras import RealDictCursor
import csv
import os
import re

def get_connection(db_host, db_port, db_name, db_user, db_pass):
    conn = psycopg2.connect(
        host=db_host,
        port=db_port,
        dbname=db_name,
        user=db_user,
        password=db_pass
    )
    cur = conn.cursor(cursor_factory=RealDictCursor)
    return conn, cur

def export_to_csv(data, filename, output_dir="out"):
    if not data:
        print(f"Nenhum dado para exportar: {filename}")
        return
    os.makedirs(output_dir, exist_ok=True)
    # Substituir caracteres inválidos
    safe_name = re.sub(r'[^\w\-_\. ]', '_', filename)
    filepath = os.path.join(output_dir, f"{safe_name}.csv")
    with open(filepath, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
    print(f"Exportado CSV: {filepath}")

def print_results(results, title=None):
    if title:
        print(f"\n=== {title} ===")
    if not results:
        print("Nenhum resultado.")
        return
    headers = results[0].keys()
    print(" | ".join(headers))
    print("-" * len(" | ".join(headers)))
    for row in results:
        print(" | ".join(str(row[h]) for h in headers))

def fetch_query(cur, query, asin=None):
    if asin:
        query = re.sub(r'\bASIN\b', f"'{asin}'", query)
    cur.execute(query)
    return cur.fetchall()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--db-host", required=True)
    parser.add_argument("--db-port", type=int, default=5432)
    parser.add_argument("--db-name", required=True)
    parser.add_argument("--db-user", required=True)
    parser.add_argument("--db-pass", required=True)
    parser.add_argument("--product-asin", help="Filtrar consultas por ASIN")
    parser.add_argument("--output", action="store_true", help="Exportar resultados para CSV")
    parser.add_argument("--output-dir", default="/app/out", help="Diretório de saída dos CSV")
    args = parser.parse_args()

    conn, cur = get_connection(args.db_host, args.db_port, args.db_name, args.db_user, args.db_pass)

    queries = {
        "Top 5 Positivos": """
            SELECT ReviewID, ASIN, ClienteID, Data, Rating, Votes, Helpful
            FROM Avaliacao
            WHERE Rating >= 4
            ORDER BY Helpful DESC
            LIMIT 5;
        """,
        "Top 5 Negativos": """
            SELECT ReviewID, ASIN, ClienteID, Data, Rating, Votes, Helpful
            FROM Avaliacao
            WHERE Rating <= 2
            ORDER BY Helpful DESC
            LIMIT 5;
        """,
        "Produtos Similares Melhor SalesRank": """
            SELECT p1.ASIN AS ASIN_Original, p1.Titulo AS Titulo_Original, p1.SalesRank AS SalesRank_Original,
                   p2.ASIN AS ASIN_Similar, p2.Titulo AS Titulo_Similar, p2.SalesRank AS SalesRank_Similar
            FROM Similares s
            JOIN Produto p1 ON s.ASIN1 = p1.ASIN
            JOIN Produto p2 ON s.ASIN2 = p2.ASIN
            WHERE p2.SalesRank < p1.SalesRank
            AND p1.SalesRank IS NOT NULL
            AND p2.SalesRank IS NOT NULL
            ORDER BY p1.ASIN, p2.SalesRank;
        """,
        "Evolução diária média": """
            SELECT Data, ROUND(AVG(Rating)::numeric,2) AS Media_Rating, COUNT(*) AS Count_Avaliacoes
            FROM Avaliacao
            GROUP BY Data
            ORDER BY Data;
        """,
        "Top 10 Produtos por Grupo": """
            SELECT * FROM (
                SELECT Grupo, ASIN, Titulo, SalesRank,
                       ROW_NUMBER() OVER (PARTITION BY Grupo ORDER BY SalesRank ASC) AS rank
                FROM Produto
                WHERE SalesRank IS NOT NULL
            ) AS sub
            WHERE rank <= 10
            ORDER BY Grupo, rank;
        """,
        "Top 10 Produtos com média úteis positivas": """
            SELECT p.ASIN, p.Titulo, ROUND(AVG(a.Helpful)::numeric,2) AS Media_Helpful,
                   COUNT(a.Helpful) AS Total_Avaliacoes
            FROM Produto p
            JOIN Avaliacao a ON p.ASIN = a.ASIN
            WHERE a.Rating >= 4
            GROUP BY p.ASIN, p.Titulo
            HAVING COUNT(a.Helpful) > 0
            ORDER BY Media_Helpful DESC, Total_Avaliacoes DESC
            LIMIT 10;
        """,
        "Top 5 Categorias média úteis positivas": """
            SELECT c.Nome AS Categoria, ROUND(AVG(a.Helpful)::numeric,2) AS Media_Helpful,
                   COUNT(a.Helpful) AS Total_Avaliacoes
            FROM Categoria c
            JOIN ProdutoCategoria pc ON c.CategoriaID = pc.CategoriaID
            JOIN Avaliacao a ON pc.ASIN = a.ASIN
            WHERE a.Rating >= 4
            GROUP BY c.CategoriaID, c.Nome
            HAVING COUNT(a.Helpful) > 0
            ORDER BY Media_Helpful DESC, Total_Avaliacoes DESC
            LIMIT 5;
        """,
        "Top 10 Clientes por Grupo": """
            SELECT * FROM (
                SELECT p.Grupo, a.ClienteID, COUNT(*) AS Total_Avaliacoes,
                       ROW_NUMBER() OVER (PARTITION BY p.Grupo ORDER BY COUNT(*) DESC) AS rank
                FROM Avaliacao a
                JOIN Produto p ON a.ASIN = p.ASIN
                GROUP BY p.Grupo, a.ClienteID
                HAVING COUNT(*) > 0
            ) AS sub
            WHERE rank <= 10
            ORDER BY Grupo, rank;
        """
    }

    for title, query in queries.items():
        results = fetch_query(cur, query, asin=args.product_asin)
        print_results(results, title)
        if args.output:
            export_to_csv(results, title, args.output_dir)

    cur.close()
    conn.close()
    print("\nExecução finalizada com sucesso.")

if __name__ == "__main__":
    main()
