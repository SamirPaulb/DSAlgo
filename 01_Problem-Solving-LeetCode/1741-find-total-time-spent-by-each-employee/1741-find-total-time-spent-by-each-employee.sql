# Write your MySQL query statement below
SELECT 
    event_day AS day,
    emp_id,
    SUM(out_time - in_time) AS total_time
    FROM Employees
    GROUP BY day, emp_id;
    

-- Group by statement is used to group the rows that have the same value. Whereas Order by statement sort the result-set either in ascending or in descending order.
