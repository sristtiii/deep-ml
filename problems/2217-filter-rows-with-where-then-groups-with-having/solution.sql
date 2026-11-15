SELECT
    customer_id,
    COUNT(*) AS completed_orders,
    SUM(amount) AS total_spent
FROM orders
WHERE status = 'completed'
GROUP BY customer_id
HAVING COUNT(*) >= 2
   AND SUM(amount) >= 100;