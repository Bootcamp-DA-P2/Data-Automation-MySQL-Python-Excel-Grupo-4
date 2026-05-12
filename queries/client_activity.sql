use sakila;

SELECT DISTINCT
    cu.customer_id,
    LOWER(cu.first_name) AS first_name,
    LOWER(cu.last_name) AS last_name,
    LOWER(cu.email) AS email,
    cu.active,
    LOWER(ad.address) AS address,
    LOWER(ad.district) AS district,
    ad.postal_code,
    ad.phone,
    LOWER(ci.city) AS city,
    LOWER(co.country) AS country
FROM customer cu
JOIN address ad ON cu.address_id = ad.address_id
JOIN city ci ON ci.city_id = ad.city_id
JOIN country co ON ci.country_id = co.country_id;