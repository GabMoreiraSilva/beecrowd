-- Autor: Gabriel Moreira Silva
-- Submissão: 23/11/2022 14:46
-- Link: https://www.beecrowd.com.br/judge/pt/problems/view/2605

SELECT products.name, providers.name 
FROM 
	products
	INNER JOIN providers ON products.id_providers = providers.id
WHERE products.id_categories = 6