-- Write your PostgreSQL query statement below
SELECT we.id
FROM weather as we
INNER JOIN weather as w
ON we.recordDate = w.recordDate + INTERVAL '1 day'
WHERE we.temperature > w.temperature; 