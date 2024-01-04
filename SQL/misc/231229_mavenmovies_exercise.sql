use mavenmovies;

-- first name, last name and email of all employees
SELECT first_name, last_name, email
FROM customer
;

-- select distinct rental duration
SELECT DISTINCT rental_duration 
FROM film
;

-- payment records of first 100 customers by customer id
SELECT *
FROM payment
WHERE customer_id <= 100

-- films with "behind the scene" special feature
SELECT title, special_features
FROM film
WHERE special_features LIKE '%Behind the Scene%'


-- count of movies by rental duration
SELECT rental_duration, COUNT(film_id) num_of_films
FROM film
GROUP BY 1
ORDER BY 1

-- count, min, max, average of films by replacement cost
SELECT
    replacement_cost,
    COUNT(film_id) number_of_films,
    MIN(rental_rate) cheapest_rental,
    MAX(rental_rate) most_expensive_rental,
    ROUND(AVG(rental_rate), 2) average_rental_rate
FROM film
GROUP BY 1
ORDER BY 1;


-- customers with 15 or lower rentals
SELECT customer_id, COUNT(rental_id) num_of_rentals
FROM rental
GROUP BY 1
HAVING num_of_rentals < 15;


-- films sorted by length
SELECT title, `length`, rental_rate
from film
ORDER BY 2 desc;


-- categorize customers by store and active STATUS
SELECT 
    first_name, last_name,
    CASE
        WHEN store_id = 1 AND active = 1 THEN "store 1 active"
        WHEN store_id = 1 AND active = 0 THEN "store 1 inactive"
        WHEN store_id = 2 AND active = 1 THEN "store 2 active"
        WHEN store_id = 2 AND active = 0 THEN "store 2 inactive"
    ELSE "Error"
    END store_status
FROM customer
;