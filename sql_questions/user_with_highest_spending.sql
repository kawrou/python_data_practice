SELECT
	users.name AS user_name,
	SUM(products.price) AS total_spent
FROM
	purchases
	INNER JOIN users ON purchases.user_id = users.id
	INNER JOIN products on purchases.product_id = products.id
GROUP BY
	users.name
ORDERD BY
	total_spent DESC
LIMIT 1
