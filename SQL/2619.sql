-- Autor: Gabriel Moreira Silva
-- Submissão: 25/11/2022 23:49:26
-- Link: https://www.beecrowd.com.br/judge/pt/problems/view/2619

SELECT
	products.name,
	providers.name,
	products.price
FROM
	products
	INNER JOIN categories ON categories.id = products.id_categories
	INNER JOIN providers ON providers.id = products.id_providers
WHERE
	products.price > 1000 AND categories.name LIKE 'Super Luxury'