-- Autor: Gabriel Moreira Silva
-- Submissão: 24/11/2022 15:10:09
-- Link: https://www.beecrowd.com.br/judge/pt/problems/view/2611

SELECT mov.id, mov.name 
FROM 
	movies mov
	INNER JOIN genres gen ON gen.id = mov.id_genres
WHERE
	gen.description LIKE 'Action'