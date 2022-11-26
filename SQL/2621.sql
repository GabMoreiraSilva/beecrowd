-- Autor: Gabriel Moreira Silva
-- Submissão: 26/11/2022 14:07:56 
-- Link: https://www.beecrowd.com.br/judge/pt/problems/view/2621

SELECT
	products.name
FROM
	products
	INNER JOIN providers ON providers.id = products.id_providers
WHERE
	products.amount >= 10 
	AND products.amount <= 20 
	AND providers.name LIKE 'P%'