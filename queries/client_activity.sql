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
    LOWER(co.country) AS country,
    LOWER(ci.city) AS city
from customer cu
join address ad on cu.address_id = ad.address_id
join city ci on ci.city_id = ad.city_id
join country co on ci.country_id = co.country_id;
