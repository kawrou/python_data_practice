SELECT
	products.name,
	COUNT(purchases.product_id)
FROM
	purchases
	inner join products on purchases.product_id = products.id
GROUP BY
	products.name
ORDER BY
	products.name

