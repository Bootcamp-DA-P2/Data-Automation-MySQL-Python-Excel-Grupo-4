use sakila;

select
	cu.customer_id as customer_id,
	LOWER(cu.first_name) AS first_name,
	LOWER(cu.last_name) AS last_name,
	LOWER(cu.email) AS email,
	cu.active,
	LOWER(ad.address) AS address,
	LOWER(ad.district) AS district,
	ad.postal_code, 
	ad.phone,
    LOWER(ci.city) AS city,
    LOWER(co.country) AS country,
    re.rental_date,
    re.return_date,
    pa.amount,
    pa.payment_date,
    DATEDIFF(re.return_date, re.rental_date) AS rental_duration,
    re.rental_id as rental_id
from customer cu
join address ad on cu.address_id = ad.address_id
join city ci on ci.city_id = ad.city_id
join country co on ci.country_id = co.country_id
join rental re on cu.customer_id = re.customer_id
join payment pa on re.rental_id = pa.rental_id
WHERE
    rental_date IS NOT NULL
    AND return_date IS NOT NULL
    AND amount > 0
    AND rental_date < return_date;