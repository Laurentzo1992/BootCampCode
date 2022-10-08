--PARTIE I

--CREATION DE TABLE customer

CREATE TABLE customer(
  customer_id SERIAL,
  first_name VARCHAR(45) NOT NULL,
  last_name VARCHAR(45) NOT NULL,
  PRIMARY KEY (customer_id)
);

--INSERTION DE DONNEES 

INSERT INTO customer(first_name, last_name) VALUE('jean', 'Doe'), ('Jerome', 'Lalu'), ('Lea', 'Rive');

--CREATION DE TABLE customer_profile

CREATE TABLE customer_profile(
  customer_id INTEGER NOT NULL,
  isLoggedIn BOOLEAN DEFAULT false,
  PRIMARY KEY (customer_id),
  CONSTRAINT fk_customer_id FOREIGN KEY(customer_id) REFERENCES customer(customer_id)
);

--INSERTION DE DONNEES AVEC LES SOUS REQUETES

INSERT INTO customer_profile(customer_id, isLoggedIn) VALUES((SELECT customer_id FROM customer WHERE first_name = 'jean'), true), ((SELECT customer_id FROM customer WHERE first_name = 'Jerome'), false);

--Afficher les données

SELECT customer.first_name FROM customer JOIN customer_profile ON customer.customer_id = customer_profile.customer_id WHERE isLoggedIn = true;
SELECT customer.first_name FROM customer FULL OUTER JOIN customer_profile ON customer.customer_id = customer_profile.customer_id;
SELECT customer.first_name FROM customer FULL OUTER JOIN customer_profile ON customer.customer_id = customer_profile.customer_id WHERE isLoggedIn = false;

--PARTIE II

--CREATION DE TABLE book


 CREATE TABLE book(
   book_id SERIAL,
   title VARCHAR(45) NOT NULL,
   author VARCHAR(45) NOT NULL,
   PRIMARY KEY (book_id)
);

--INSERTION DE DONNEES

INSERT INTO book(title, author) VALUES ('Alice au pays des merveilles', 'Lewis Carroll'), ('Harry Potter', 'JK Rowling'), ('Pour tuer un oiseau moqueur', 'Harper Lee');

--CREATION DE TABLE student

  CREATE TABLE student(
    student_id SERIAL,
    nom VARCHAR(45) NOT NULL UNIQUE,
    age INTEGER NOT NULL INTEGER NOT NULL CONSTRAINT age_check CHECK (age <= 15),
    PRIMARY KEY (student_id)
 );

--INSERTION DE DONNEES 

INSERT INTO student(nom, age) VALUES ('John', 12), ('Lera', 11), ('Patrick', '10'), ('Bob', '14');

--CREATION DE TABLE library

   CREATE TABLE library(
    student_id INTEGER NOT NULL,
    book_id INTEGER NOT NULL,
    borrowed_date date NOT NULL,
    PRIMARY KEY (student_id, book_id),
    FOREIGN KEY (student_id) REFERENCES student(student_id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (book_id) REFERENCES book(book_id) ON DELETE CASCADE ON UPDATE CASCADE
 );

--Set style to date time
SET datestyle = dmy;

INSERT INTO library(student_id, book_id, borrowed_date) VALUES 

((SELECT student_id FROM student WHERE nom = 'John'), 
(SELECT book_id FROM book WHERE title = 'Alice au pays des merveilles'), '15-02-2022'),

((SELECT student_id FROM student WHERE nom = 'Bob'), 
(SELECT book_id FROM book WHERE title = 'Pour tuer un oiseau moqueur'), '03-03-2021'),

((SELECT student_id FROM student WHERE nom = 'Lera'),
(SELECT book_id FROM book WHERE title = 'Alice au pays des merveilles'), '23-05-2021'),

((SELECT student_id FROM student WHERE nom = 'Bob'), 
(SELECT book_id FROM book WHERE title = 'Harry Potter'), '08-12-2021');

--Afficher les données

-- Sélectionnez toutes les colonnes de la table de jonction
-- Sélectionnez le nom de l'élève et le titre des livres empruntés
-- Sélectionnez l'âge moyen des enfants qui ont emprunté le livre Alice au pays des merveilles
-- Supprimer un étudiant de la table des étudiants, que s'est-il passé dans la table de jonction ?

SELECT * FROM library;
--
SELECT student.nom, book.title FROM student, book, library WHERE student.student_id = library.student_id AND book.book_id = library.book_id;
--
SELECT AVG(student.age) as age_moyen FROM student, book, library WHERE student.student_id = library.student_id AND book.book_id = library.book_id AND book.title = 'Alice au pays des merveilles';
--
DELETE FROM student WHERE nom = 'John';

--la donnee est suprime dans la table student et la cle a ete suprime dans la table library




