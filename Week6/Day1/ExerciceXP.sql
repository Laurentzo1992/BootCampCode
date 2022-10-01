

CREATE TABLE public."items"(
 item_id SERIAL PRIMARY KEY,
 item_name VARCHAR (50) NOT NULL
 item_price REAL (10) NOT NULL
);

CREATE TABLE public."customers"(
 customer_id SERIAL PRIMARY KEY,
 customer_fname VARCHAR (50) NOT NULL,
 customer_name VARCHAR (100) NOT NULL
);

INSERT INTO items (item_name)
VALUES('Petit bureau', 100),
('Grand bureau', 300),
('Ventilateur ', 80),


INSERT INTO customers (customer_fname, customer_name)
VALUES('Greg','Jones'),
('Sandra','Jones'),
('Scott','Scott'),
('Trevor','Vert'),
('Mélanie','Johnson')


SELECT * from items;

SELECT item_name, item_price from items WHERE item_price > 80;

SELECT item_name, item_price from items WHERE item_price <= 300;

SELECT customer_fname, customer_name from customers WHERE customer_name LIKE %Smith%
SELECT customer_fname, customer_name from customers WHERE customer_name LIKE %Jones%
SELECT customer_fname, customer_name from customers WHERE customer_fname LIKE %Scott%