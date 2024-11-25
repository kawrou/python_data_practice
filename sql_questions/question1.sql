SELECT id, NAME FROM users WHERE age > 30 ORDER BY NAME

SELECT 
	CASE
		WHEN age < 30 THEN '<30'
		WHEN age BETWEEN 30 AND 40 THEN '30-40'
		ELSE '>40'
	END AS age_group,
	COUNT(*) AS user_count
FROM users
GROUP BY age_group

