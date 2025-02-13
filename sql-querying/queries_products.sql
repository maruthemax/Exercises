-- Comments in SQL Start with dash-dash --
-- Add a product to the table with the name of "chair", price of 44.00, and can_be_returned of false
INSERT INTO products (name, price, can_be_returned) VALUES ('chair', 44.00, false);

-- Add a product to the table with the name of "stool", price of 25.99, and can_be_returned of true
INSERT INTO products (name, price, can_be_returned) VALUES ('stool', 25.99, true);

-- Add a product to the table with the name of "table", price of 124.00, and can_be_returned of false
INSERT INTO products (name, price, can_be_returned) VALUES ('table', 124.00, false);

-- Display all rows and columns in the products table
SELECT * FROM products;

-- Display all product names
SELECT name FROM products;

-- Display all product names and prices
SELECT name, price FROM products;

-- Add a new product "lamp" with a price of 39.99, and it can be returned
INSERT INTO products (name, price, can_be_returned) VALUES ('lamp', 39.99, true);

-- Display products that can be returned
SELECT * FROM products WHERE can_be_returned = true;

-- Display products with a price less than 44.00
SELECT * FROM products WHERE price < 44.00;

-- Display products with a price between 22.50 and 99.99
SELECT * FROM products WHERE price BETWEEN 22.50 AND 99.99;

-- Update all products to reflect a $20 discount
UPDATE products SET price = price - 20;

-- Remove products with a price less than $25
DELETE FROM products WHERE price < 25;

-- Increase all remaining products' prices by $20
UPDATE products SET price = price + 20;

-- Update all products to make them returnable
UPDATE products SET can_be_returned = true;
