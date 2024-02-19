-- Write your PostgreSQL query statement below
SELECT  a.machine_id, ROUND(AVG(ac.timestamp - a.timestamp)::numeric, 3) AS processing_time
FROM Activity AS a
INNER JOIN Activity AS ac
ON a.machine_id = ac.machine_id 
    AND a.process_id = ac.process_id
    AND a.activity_type = 'start'
    AND a.activity_type <> ac.activity_type
GROUP BY a.machine_id;
    