-- Write your PostgreSQL query statement below
SELECT 
    query_name,
    ROUND (AVG(rating * 1.0 / position)::numeric, 2) AS quality,
    ROUND (SUM(CASE WHEN rating < 3 THEN 1 ELSE 0 END) * 1.0 / COUNT(*) * 100.0, 2) AS poor_query_percentage
FROM
    Queries
WHERE 
    query_name IS NOT NULL
GROUP BY 
    query_name;