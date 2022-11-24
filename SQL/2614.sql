-- Autor: Gabriel Moreira Silva
-- Submissão: 24/11/2022 16:44:56
-- Link: https://www.beecrowd.com.br/judge/pt/problems/view/2614

SELECT 
	cust.name, 
	rent.rentals_date 
FROM 
	rentals rent
	INNER JOIN customers cust ON cust.id = rent.id_customers
WHERE
	rentals_date >= '2016-09-01' AND rentals_date <= '2016-09-30'