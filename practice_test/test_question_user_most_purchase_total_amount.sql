SELECT
	users.name,
	SUM(products.price)
FROM
	purchases
	inner join users on purchases.user_id = users.id
	inner join products on purchases.product_id = products.id
GROUP BY
	users.name
ORDER BY
	SUM(products.price) DESC
LIMIT 
	1
