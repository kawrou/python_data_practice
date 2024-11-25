SELECT
	products.id AS product_id,
	products.name AS product_name,
	products.price AS product_price,
	products.description AS product_description
FROM
	products
	LEFT JOIN purchases ON products.id = purchases.product_id
WHERE 
	purchases.product_id IS NULL;

