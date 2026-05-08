use sakila;

select
	lower(fi.title) 'Title',
    lower(fi.description) 'Description',
    fi.release_year,
    fi.rating,
    lower(ca.name) as 'Category',
    re.rental_date,
    re.return_date,
    pa.amount,
    pa.payment_date,
    concat(lower(cu.first_name),' ',lower(cu.last_name)) as 'Full Name',
    lower(ci.city) as 'City',
    lower(co.country) as 'Country',
    DATEDIFF(re.return_date, re.rental_date) AS rental_duration
from customer cu
join address ad on cu.address_id = ad.address_id
join city ci on ci.city_id = ad.city_id
join country co on ci.country_id = co.country_id
join rental re on cu.customer_id = re.customer_id
join payment pa on re.rental_id = pa.rental_id
join inventory inv on re.inventory_id = inv.inventory_id
join film fi on inv.film_id = fi.film_id
join film_category fic on fic.film_id = fi.film_id
join category ca on ca.category_id = fic.category_id
WHERE
    rental_date IS NOT NULL
    AND return_date IS NOT NULL
    AND amount > 0
    AND rental_date < return_date
order by
	rental_date asc
