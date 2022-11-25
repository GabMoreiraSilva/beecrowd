-- Autor: Gabriel Moreira Silva
-- Submissão: 25/11/2022 15:21 
-- Link: https://www.beecrowd.com.br/judge/pt/problems/view/2618

SELECT
	prod.name,
	prov.name,
	cat.name
FROM
	products prod
	INNER JOIN providers prov ON prov.id = prod.id_providers
	INNER JOIN categories cat ON cat.id = prod.id_categories
WHERE
	prov.name LIKE 'Sansul SA' AND cat.name = 'Imported'