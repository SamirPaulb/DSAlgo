# Write your MySQL query statement below
SELECT 
    date_id, make_name, 
    COUNT(DISTINCT lead_id) AS unique_leads, 
    COUNT(DISTINCT partner_id) AS unique_partners
    FROM DailySales
    GROUP BY make_name, date_id