use sakila;

SELECT
    re.rental_id,
    re.rental_date,
    re.return_date,
    re.customer_id,     
    inv.film_id,         
    inv.inventory_id,
    pa.amount,
    pa.payment_date,
    DATEDIFF(re.return_date, re.rental_date) AS rental_duration
FROM rental re
JOIN payment pa ON re.rental_id = pa.rental_id
JOIN inventory inv ON re.inventory_id = inv.inventory_id
WHERE 
    re.rental_date IS NOT NULL 
    AND re.return_date IS NOT NULL 
    AND pa.amount > 0 
    AND re.rental_date < re.return_date
ORDER BY re.rental_date ASC;