-- Comments in SQL Start with dash-dash --
-- Find the app with ID 1880
SELECT * FROM analytics WHERE id = 1880;

-- Find apps updated on August 01, 2018
SELECT id, app_name FROM analytics WHERE last_updated = '2018-08-01';

-- Count the number of apps in each category
SELECT category, COUNT(*) FROM analytics GROUP BY category;

-- Find the top 5 most-reviewed apps
SELECT app_name, reviews FROM analytics ORDER BY reviews DESC LIMIT 5;

-- Find the most-reviewed app with rating >= 4.8
SELECT app_name FROM analytics WHERE rating >= 4.8 ORDER BY reviews DESC LIMIT 1;

-- Calculate the average rating for each category
SELECT category, AVG(rating) AS avg_rating FROM analytics GROUP BY category ORDER BY avg_rating DESC;

-- Find the most expensive app with a rating below 3
SELECT app_name, price, rating FROM analytics WHERE rating < 3 ORDER BY price DESC LIMIT 1;

-- Find apps with min installs <= 50 and a rating
SELECT app_name FROM analytics WHERE min_installs <= 50 AND rating IS NOT NULL ORDER BY rating DESC;

-- Find apps rated < 3 with at least 10,000 reviews
SELECT app_name FROM analytics WHERE rating < 3 AND reviews >= 10000;

-- Find the top 10 most-reviewed apps costing between $0.10 and $1
SELECT app_name, reviews FROM analytics WHERE price BETWEEN 0.10 AND 1.00 ORDER BY reviews DESC LIMIT 10;

-- Find the most out-of-date app
SELECT app_name, last_updated FROM analytics WHERE last_updated = (SELECT MIN(last_updated) FROM analytics);

-- Find the most expensive app
SELECT app_name, price FROM analytics WHERE price = (SELECT MAX(price) FROM analytics);

-- Count the total number of reviews in the Play Store
SELECT SUM(reviews) FROM analytics;

-- Find categories with more than 300 apps
SELECT category FROM analytics GROUP BY category HAVING COUNT(*) > 300;

-- Find the app with the highest min_installs/reviews ratio
SELECT app_name, reviews, min_installs, (min_installs::float / reviews) AS proportion 
FROM analytics 
WHERE min_installs >= 100000 
ORDER BY proportion DESC LIMIT 1;
