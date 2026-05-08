use sakila;

SELECT 
	LOWER(TRIM(title)) AS title,
	LOWER(TRIM(description)) AS description,
	release_year,
	rental_duration,
	rental_rate,
	length,
	replacement_cost,
	rating,
    LOWER(TRIM(cat.name)) AS category,
    LOWER(TRIM(l.name)) AS language,
    COUNT(inv.inventory_id) AS total_inventory
FROM film
JOIN film_category fcat ON fcat.film_id = film.film_id
JOIN category cat ON fcat.category_id = cat.category_id
JOIN language l ON l.language_id = film.language_id
JOIN inventory inv ON film.film_id = inv.film_id
GROUP BY 
	film.title, 
    film.description,
    film.release_year,
    film.rental_duration,
    film.rental_rate,
    film.length,
    film.replacement_cost,
    film.rating,
    cat.name,
    l.name;
    
    


