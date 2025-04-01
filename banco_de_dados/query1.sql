UPDATE demonstracoes_contabeis
SET vl_saldo_inicial = REPLACE(vl_saldo_inicial, ',', '.')::REAL,
    vl_saldo_final = REPLACE(vl_saldo_final, ',', '.')::REAL;

ALTER TABLE demonstracoes_contabeis 
ALTER COLUMN vl_saldo_inicial TYPE REAL USING vl_saldo_inicial::REAL,
ALTER COLUMN vl_saldo_final TYPE REAL USING vl_saldo_final::REAL;

SELECT d.data_contabil, r.razao_social, d.descricao,
TO_CHAR(SUM(d.vl_saldo_final - d.vl_saldo_inicial),'FM999G999G999G999D99') AS total_despesas
FROM demonstracoes_contabeis d
JOIN relatorio_cadop r ON d.reg_ans = r.registro_ans  
WHERE r.razao_social ILIKE '%OPERADORA%' 
AND d.descricao ILIKE '%EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR %'
AND d.data_contabil >= '2024-10-01'
GROUP BY r.razao_social, d.data_contabil, d.descricao
ORDER BY SUM(d.vl_saldo_final - d.vl_saldo_inicial ) DESC
LIMIT 10;

