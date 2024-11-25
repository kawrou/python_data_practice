SELECT
	users.name AS user_name,
	products.name AS product_name
FROM
	purchases
	INNER JOIN users ON purchases.user_id = users.id
	INNER JOIN products on purchases.product_id = products.id
ORDER BY
	users.name
