use sakila;

SELECT
	LOWER(fi.title) AS title,
    LOWER(fi.description) AS description,
    fi.release_year,
    fi.rental_rate,
    fi.rental_duration,
    fi.length,
    LOWER(fi.special_features) AS special_features,
    LOWER(ac.first_name) AS first_name,
    LOWER(ac.last_name) AS last_name
FROM film fi
JOIN film_actor fa on fi.film_id = fa.film_id
JOIN actor ac on fa.actor_id = ac.actor_id
WHERE
	fi.rental_rate IS NOT NULL
    AND fi.rental_rate > 0
    and fi.length > 0;

