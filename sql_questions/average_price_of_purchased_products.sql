SELECT
	AVG(products.price)::NUMERIC(10,2)
	AS average_price
FROM
	purchases
	inner join products on purchases.product_id = products.id
