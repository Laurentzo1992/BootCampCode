--PARTIE I

-- CREATE TABLE customer(
--   customer_id SERIAL,
--   first_name VARCHAR(45) NOT NULL,
--   last_name VARCHAR(45) NOT NULL,
--   PRIMARY KEY (customer_id)
-- );

-- CREATE TABLE customer_profile(
--   customer_id INTEGER NOT NULL,
--   isLoggedIn BOOLEAN DEFAULT false,
--   PRIMARY KEY (customer_id),
--   CONSTRAINT fk_customer_id FOREIGN KEY(customer_id) REFERENCES customer(customer_id)
-- );
--INSERT into customer(first_name, last_name) VALUE('jean', 'Doe'), ('Jerome', 'Lalu'), ('Lea', 'Rive');
--INSERT into customer_profile(customer_id, isLoggedIn) VALUES((SELECT customer_id FROM customer WHERE first_name = 'jean'), true), ((SELECT customer_id FROM customer WHERE first_name = 'Jerome'), false);
-- CREATE TABLE customer_profile(
--SELECT customer.first_name FROM customer JOIN customer_profile ON customer.customer_id = customer_profile.customer_id WHERE isLoggedIn = true;
--SELECT customer.first_name FROM customer FULL OUTER JOIN customer_profile ON customer.customer_id = customer_profile.customer_id;
--SELECT customer.first_name FROM customer FULL OUTER JOIN customer_profile ON customer.customer_id = customer_profile.customer_id WHERE isLoggedIn = false;

--PARTIE II

--  CREATE TABLE book(
--    book_id SERIAL,
--    title VARCHAR(45) NOT NULL,
--    author VARCHAR(45) NOT NULL,
--    PRIMARY KEY (book_id)
-- );

--INSERT INTO book(title, author) VALUES ('Alice au pays des merveilles', 'Lewis Carroll'), ('Harry Potter', 'JK Rowling'), ('Pour tuer un oiseau moqueur', 'Harper Lee');

  CREATE TABLE student(
    student_id SERIAL,
    nom VARCHAR(45) NOT NULL,
    age INTEGER(2) NOT NULL,
    PRIMARY KEY (book_id)
    CONSTRAINT age_constraint age<=15;
 );