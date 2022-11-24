-- Autor: Gabriel Moreira Silva
-- Submissão: 24/11/2022 15:10:09
-- Link: https://www.beecrowd.com.br/judge/pt/problems/view/2613

SELECT 
	mov.id, 
	mov.name
FROM 
	movies mov
	INNER JOIN prices pr ON pr.id = mov.id_prices
WHERE
	pr.value < 2.00