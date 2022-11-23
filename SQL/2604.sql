-- Autor: Gabriel Moreira Silva
-- Submissão: 23/11/2022 15:26:50 
-- Link: https://www.beecrowd.com.br/judge/pt/problems/view/2604

SELECT 
	products.id, 
	products.name 
FROM 
	products
WHERE 
	products.price < 10 OR products.price > 100