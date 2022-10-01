CREATE TABLE public."etudiants"(
 etudiant_id SERIAL PRIMARY KEY,
 etudiant_fname VARCHAR (50) NOT NULL,
 etudiant_name VARCHAR (50) NOT NULL,
 age DATE NOT NULL
);

INSERT INTO etudiants (etudiant_fname, etudiant_name, age)
VALUES('Marc', 'Bénichou', '02/11/1998'),
('Yann', 'Cohen', '03/12/2010'),
('Léa', 'Bénichou', '27/07/1987'),
('Amélie', 'Dux', '07/04/1996'),
('David', 'Grez', '14/06/2003'),
('Omer', 'Simpson', '03/10/1980'),



SELECT * étudiants;
