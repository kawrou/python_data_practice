SELECT * FROM products where NAME LIKE '%a%' ORDER BY price DESC

SELECT AVG(price)::NUMERIC(10,2) FROM products

SELECT id, name, price
FROM products
WHERE price > (
	SELECT AVG(price) FROM products
);

SELECT 
	users.name AS user_name, 
	products.name AS product_name
FROM purchases
INNER JOIN users on purchases.user_id = users.id
INNER JOIN products on purchases.product_id = products.id

