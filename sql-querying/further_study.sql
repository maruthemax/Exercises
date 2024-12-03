--Top-rated apps in each category with ≥50,000 installs--
SELECT category, app_name, rating 
FROM analytics 
WHERE min_installs >= 50000 
GROUP BY category, app_name, rating 
HAVING rating = MAX(rating);


--Apps with names like “facebook”--
SELECT app_name FROM analytics WHERE app_name ILIKE '%facebook%';

--Apps with more than one genre--
SELECT app_name FROM analytics WHERE array_length(genres, 1) > 1;

--Apps with "education" in genres--
SELECT app_name FROM analytics WHERE 'Education' = ANY(genres);
