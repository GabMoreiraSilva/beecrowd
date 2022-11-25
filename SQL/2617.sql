-- Autor: Gabriel Moreira Silva
-- Submissão: 25/11/2022 15:02
-- Link: https://www.beecrowd.com.br/judge/pt/problems/view/2617

SELECT 
	products.name,
	providers.name
FROM
	products
	INNER JOIN providers ON providers.id = products.id_providers
WHERE
	providers.name LIKE 'Ajax SA'