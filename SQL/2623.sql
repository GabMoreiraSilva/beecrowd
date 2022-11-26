-- Autor: Gabriel Moreira Silva
-- Submissão: 26/11/2022 23:04:27
-- Link: https://www.beecrowd.com.br/judge/pt/problems/view/2623

SELECT 
	products.name,
	categories.name
FROM
	products
	INNER JOIN categories ON categories.id = products.id_categories
WHERE
	products.amount > 100 
	AND products.id_categories IN(1,2,3,6,9)