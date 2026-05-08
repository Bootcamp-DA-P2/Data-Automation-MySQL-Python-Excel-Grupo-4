use sakila;

SELECT 
    LOWER(TRIM(film.title)) AS title,
    LOWER(TRIM(cat.name)) AS category,
    length,
    rating,
    LOWER(TRIM(l.name)) AS language,
    COUNT(DISTINCT inv.inventory_id) AS total_inventory, -- Contamos cuántas copias físicas distintas existen para esta película
    COUNT(r.rental_id) AS total_rentals -- Contamos cuántas transacciones de alquiler existen en total
FROM film
JOIN film_category fcat ON fcat.film_id = film.film_id
JOIN category cat ON fcat.category_id = cat.category_id
JOIN language l ON l.language_id = film.language_id
JOIN inventory inv ON film.film_id = inv.film_id
JOIN rental r ON inv.inventory_id = r.inventory_id
GROUP BY 
    film.title,
    cat.name,
      l.name,
    film.length,
    film.rating;