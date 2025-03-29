SELECT 
r.razao_social, 
TO_CHAR(
SUM(d.vl_saldo_final - d.vl_saldo_inicial), 'FM999G999G999G999D99') AS total_despesas
FROM demonstracoes_contabeis d
JOIN relatorio_cadop r ON d.reg_ans = r.registro_ans  
WHERE r.razao_social ILIKE '%OPERADORA%' 
AND d.data_contabil >= '2024-01-01' 
AND d.data_contabil <= '2024-12-31' 
GROUP BY r.razao_social
ORDER BY SUM(d.vl_saldo_final - d.vl_saldo_inicial) DESC
LIMIT 10;