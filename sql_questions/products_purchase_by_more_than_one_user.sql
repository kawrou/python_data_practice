SELECT
	products.name AS product_name,
	COUNT(purchases.user_id) AS purchases
FROM
	purchases
	INNER JOIN products ON purchases.product_id = products.id
GROUP BY
	purchases.product_id,
	products.name
HAVING COUNT(purchases.user_id) > 1;
