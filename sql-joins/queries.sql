-- write your queries here
SELECT 
    owners.id AS owner_id, 
    owners.first_name, 
    owners.last_name, 
    vehicles.id AS vehicle_id, 
    vehicles.make, 
    vehicles.model, 
    vehicles.year, 
    vehicles.price, 
    vehicles.owner_id
FROM 
    owners
FULL OUTER JOIN 
    vehicles
ON 
    owners.id = vehicles.owner_id;



SELECT 
    owners.first_name, 
    owners.last_name, 
    COUNT(vehicles.id) AS count
FROM 
    owners
LEFT JOIN 
    vehicles
ON 
    owners.id = vehicles.owner_id
GROUP BY 
    owners.first_name, 
    owners.last_name
ORDER BY 
    owners.first_name ASC;



SELECT 
    owners.first_name, 
    owners.last_name, 
    CAST(AVG(vehicles.price) AS INTEGER) AS average_price, 
    COUNT(vehicles.id) AS count
FROM 
    owners
INNER JOIN 
    vehicles
ON 
    owners.id = vehicles.owner_id
GROUP BY 
    owners.first_name, 
    owners.last_name
HAVING 
    COUNT(vehicles.id) > 1 AND AVG(vehicles.price) > 10000
ORDER BY 
    owners.first_name DESC;







------FROM Joins Exercise Solution--------
-- -- first query
-- SELECT * FROM owners o 
--   FULL OUTER JOIN vehicles v 
--     ON o.id=v.owner_id;

-- -- second query
-- SELECT first_name, last_name, 
--   COUNT(owner_id) FROM owners o 
--   JOIN vehicles v on o.id=v.owner_id 
--   GROUP BY (first_name, last_name) 
-- ORDER BY first_name;


-- -- third query
-- SELECT 
--   first_name, last_name, 
--   ROUND(AVG(price)) as average_price, 
--   COUNT(owner_id) 
-- FROM owners o 
-- JOIN vehicles v on o.id=v.owner_id 
-- GROUP BY 
--   (first_name, last_name) 
-- HAVING 
--   COUNT(owner_id) > 1 AND ROUND(AVG(price)) > 10000 
-- ORDER BY first_name DESC;