-- Autor: Gabriel Moreira Silva
-- Submissão: 24/11/2022 14:28:15
-- Link: https://www.beecrowd.com.br/judge/pt/problems/view/2609

SELECT cat.name, SUM(products.amount)
FROM categories cat
INNER JOIN products ON products.id_categories = cat.id
GROUP BY cat.name