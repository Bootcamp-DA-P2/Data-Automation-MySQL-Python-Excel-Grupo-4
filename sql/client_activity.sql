-- 1. Crear el usuario
CREATE USER 'admin'@'localhost' IDENTIFIED BY 'admin';

-- 2. Darle todos los permisos para que pueda crear bases de datos y tablas
GRANT ALL PRIVILEGES ON *.* TO 'admin'@'localhost' WITH GRANT OPTION;

-- 3. Refrescar los permisos
FLUSH PRIVILEGES;

use sakila;

Select country.country_id, country.country, country.last_update, city_id, city, address_id, address, address2, district, postal_code, phone, location, customer_id, firt_name, last_name, email, customer.active, create_date
from country
join 
city on country.country_id = city.country_id
join
address on address.city_id = city.city_id
join
customer on customer.address_id = customer.address_id;




