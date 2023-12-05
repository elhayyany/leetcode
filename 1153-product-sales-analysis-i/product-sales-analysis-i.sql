# Write your MySQL query statement below
SELECT product_name, year, price
FROM Sales s 
JOIN Product p
WHERE  p.product_id = s.product_id