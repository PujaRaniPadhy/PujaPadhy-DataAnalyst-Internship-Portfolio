-- Business Question 1
-- Top 5 products by total quantity sold

SELECT Description, SUM(Quantity) AS total_quantity
FROM sales
GROUP BY Description
ORDER BY total_quantity DESC
LIMIT 5;


-- Business Question 2
-- Country with highest sales

SELECT Country, SUM(Quantity * Price) AS total_sales
FROM sales
GROUP BY Country
ORDER BY total_sales DESC;


-- Business Question 3
-- Average product price

SELECT AVG(Price) AS average_price
FROM sales;


-- Business Question 4
-- Total sales by customer

SELECT [Customer ID], SUM(Quantity * Price) AS total_spent
FROM sales
GROUP BY [Customer ID]
ORDER BY total_spent DESC;


-- Business Question 5
-- Total quantity sold by country

SELECT Country, SUM(Quantity) AS total_quantity
FROM sales
GROUP BY Country
ORDER BY total_quantity DESC;