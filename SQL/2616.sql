-- Autor: Gabriel Moreira Silva
-- Submissão: 25/11/2022 14:44
-- Link: https://www.beecrowd.com.br/judge/pt/problems/view/2616

SELECT 
	customers.id,
	customers.name 
FROM 
	customers
WHERE
	customers.id NOT IN (SELECT 
						 	locations.id_customers
						FROM
							locations
							INNER JOIN customers ON locations.id_customers = customers.id)