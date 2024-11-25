SELECT
	users.name AS user_name,
	SUM(products.price) AS total_spending
FROM
	purchases
	INNER JOIN users ON purchases.user_id = user.id
	INNER JOIN products ON purchases.product_id = products.id
GROUP BY
	users.name,
ORDER BY
	users.name
