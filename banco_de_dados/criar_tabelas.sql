CREATE TABLE relatorio_cadop (
    
    id SERIAL PRIMARY KEY,
    registro_ANS VARCHAR(10)  NOT NULL, 
    cnpj VARCHAR(14) UNIQUE NOT NULL,
    razao_social VARCHAR(150) NOT NULL,
    nome_fantasia VARCHAR(150),
    modalidade VARCHAR(100) NOT NULL,
    logradouro VARCHAR(100) NOT NULL,
    numero VARCHAR(20) NOT NULL,
    complemento VARCHAR(50),
    bairro VARCHAR(50) NOT NULL,
    cidade VARCHAR(50) NOT NULL,
    uf CHAR(2) NOT NULL,
    cep VARCHAR(8) NOT NULL,
    ddd VARCHAR(2), 
    telefone VARCHAR(15), 
    fax VARCHAR(15), 
    endereco_eletronico VARCHAR(80) NOT NULL,
    representante VARCHAR(100) NOT NULL,
    cargo_representante VARCHAR(100) NOT NULL,
    regiao_de_comercializacao SMALLINT,
    data_registro_ANS DATE NOT NULL 

);

CREATE TABLE demonstracoes_contabeis (
    id SERIAL PRIMARY KEY,
    data_contabil DATE NOT NULL, 
    reg_ANS VARCHAR(6) NOT NULL,
    cd_conta_contabil VARCHAR(20) NOT NULL,
    descricao VARCHAR(255) NOT NULL,
    vl_saldo_inicial NUMERIC(15,2) DEFAULT 0 NOT NULL,
    vl_saldo_final NUMERIC(15,2) DEFAULT 0 NOT NULL
);


ALTER TABLE demonstracoes_contabeis 
    ALTER COLUMN vl_saldo_inicial TYPE TEXT,
    ALTER COLUMN vl_saldo_final TYPE TEXT;
UPDATE demonstracoes_contabeis
SET vl_saldo_inicial = REPLACE(vl_saldo_inicial, ',', '.')::REAL,
    vl_saldo_final = REPLACE(vl_saldo_final, ',', '.')::REAL;

ALTER TABLE demonstracoes_contabeis 
ALTER COLUMN vl_saldo_inicial TYPE REAL USING vl_saldo_inicial::REAL,
ALTER COLUMN vl_saldo_final TYPE REAL USING vl_saldo_final::REAL;