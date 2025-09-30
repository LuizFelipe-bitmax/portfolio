-- tp1_queries.sql
-- Consultas SQL para o projeto Amazon TP01

-- 1. Top 5 comentários úteis positivos (Rating >= 4)
SELECT ReviewID, ASIN, ClienteID, Data, Rating, Votes, Helpful
FROM Avaliacao
WHERE Rating >= 4
ORDER BY Helpful DESC
LIMIT 5;

-- Top 5 comentários úteis negativos (Rating <= 2)
SELECT ReviewID, ASIN, ClienteID, Data, Rating, Votes, Helpful
FROM Avaliacao
WHERE Rating <= 2
ORDER BY Helpful DESC
LIMIT 5;

-- 2. Produtos similares com melhor SalesRank
SELECT 
    p1.ASIN AS ASIN_Original,
    p1.Titulo AS Titulo_Original,
    p1.SalesRank AS SalesRank_Original,
    p2.ASIN AS ASIN_Similar,
    p2.Titulo AS Titulo_Similar,
    p2.SalesRank AS SalesRank_Similar
FROM Similares s
JOIN Produto p1 ON s.ASIN1 = p1.ASIN
JOIN Produto p2 ON s.ASIN2 = p2.ASIN
WHERE p2.SalesRank < p1.SalesRank
AND p1.SalesRank IS NOT NULL
AND p2.SalesRank IS NOT NULL
ORDER BY p1.ASIN, p2.SalesRank;

-- 3. Evolução diária das médias de avaliação
SELECT 
    Data, 
    ROUND(AVG(Rating)::numeric, 2) AS Media_Rating,
    COUNT(*) AS Count_Avaliacoes
FROM Avaliacao
GROUP BY Data
ORDER BY Data;

-- 4. Top 10 produtos por grupo
SELECT *
FROM (
    SELECT 
        Grupo,
        ASIN,
        Titulo,
        SalesRank,
        ROW_NUMBER() OVER (PARTITION BY Grupo ORDER BY SalesRank ASC) AS rank
    FROM Produto
    WHERE SalesRank IS NOT NULL
) AS sub
WHERE rank <= 10
ORDER BY Grupo, rank;

-- 5. Top 10 produtos com maior média de avaliações úteis positivas
SELECT 
    p.ASIN,
    p.Titulo,
    ROUND(AVG(a.Helpful)::numeric,2) AS Media_Helpful,
    COUNT(a.Helpful) AS Total_Avaliacoes
FROM Produto p
JOIN Avaliacao a ON p.ASIN = a.ASIN
WHERE a.Rating >= 4
GROUP BY p.ASIN, p.Titulo
HAVING COUNT(a.Helpful) > 0
ORDER BY Media_Helpful DESC, Total_Avaliacoes DESC
LIMIT 10;

-- 6. Top 5 categorias com maior média de avaliações úteis positivas
SELECT 
    c.Nome AS Categoria,
    ROUND(AVG(a.Helpful)::numeric,2) AS Media_Helpful,
    COUNT(a.Helpful) AS Total_Avaliacoes
FROM Categoria c
JOIN ProdutoCategoria pc ON c.CategoriaID = pc.CategoriaID
JOIN Avaliacao a ON pc.ASIN = a.ASIN
WHERE a.Rating >= 4
GROUP BY c.CategoriaID, c.Nome
HAVING COUNT(a.Helpful) > 0
ORDER BY Media_Helpful DESC, Total_Avaliacoes DESC
LIMIT 5;

-- 7. Top 10 clientes que mais comentaram por grupo
SELECT *
FROM (
    SELECT 
        p.Grupo,
        a.ClienteID,
        COUNT(*) AS Total_Avaliacoes,
        ROW_NUMBER() OVER (PARTITION BY p.Grupo ORDER BY COUNT(*) DESC) AS rank
    FROM Avaliacao a
    JOIN Produto p ON a.ASIN = p.ASIN
    GROUP BY p.Grupo, a.ClienteID
    HAVING COUNT(*) > 0
) AS sub
WHERE rank <= 10
ORDER BY Grupo, rank;
