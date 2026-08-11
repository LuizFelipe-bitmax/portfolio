-- Criação das tabelas do banco de dados Amazon Luiz Felipe

-- Tabela Produto
CREATE TABLE Produto (
    ASIN VARCHAR(10) PRIMARY KEY CHECK (LENGTH(ASIN) > 0),
    Titulo VARCHAR(255),
    Grupo VARCHAR(50),
    SalesRank INT,
    Descontinuado BOOLEAN DEFAULT FALSE
);

-- Tabela Categoria
CREATE TABLE Categoria (
    CategoriaID INT PRIMARY KEY CHECK (CategoriaID > 0),
    Nome VARCHAR(100) NOT NULL,
    CategoriaPaiID INT REFERENCES Categoria(CategoriaID)
);

-- Tabela ProdutoCategoria (N:M)
CREATE TABLE ProdutoCategoria (
    ASIN VARCHAR(10) REFERENCES Produto(ASIN),
    CategoriaID INT REFERENCES Categoria(CategoriaID),
    PRIMARY KEY (ASIN, CategoriaID)
);

-- Tabela Similares (N:M recursivo)
CREATE TABLE Similares (
    ASIN1 VARCHAR(10) REFERENCES Produto(ASIN),
    ASIN2 VARCHAR(10) REFERENCES Produto(ASIN),
    PRIMARY KEY (ASIN1, ASIN2),
    CHECK (ASIN1 <> ASIN2)
);

-- Tabela Cliente
CREATE TABLE Cliente (
    ClienteID VARCHAR(20) PRIMARY KEY CHECK (LENGTH(ClienteID) > 0)
);

-- Tabela Avaliacao
CREATE TABLE Avaliacao (
    ReviewID SERIAL PRIMARY KEY,
    ASIN VARCHAR(10) REFERENCES Produto(ASIN),
    ClienteID VARCHAR(20) REFERENCES Cliente(ClienteID),
    Data DATE,
    Rating INT CHECK (Rating BETWEEN 1 AND 5),
    Votes INT DEFAULT 0 CHECK (Votes >= 0),
    Helpful INT DEFAULT 0 CHECK (Helpful >= 0 AND Helpful <= Votes)
);
