-- Autor: Gabriel Moreira Silva
-- Submissão: 23/11/2022 18:12:37
-- Link: https://www.beecrowd.com.br/judge/pt/problems/view/2606

SELECT 
	products.id,
	products.name
FROM
	categories
	INNER JOIN products ON products.id_categories = categories.id
WHERE
	categories.name LIKE 'super%';