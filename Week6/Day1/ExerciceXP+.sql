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


-- Récupérer toutes les données de la table.
SELECT * étudiants;

-- Récupérer tous les prénoms et noms de famille des étudiants .
SELECT etudiant_fname, etudiant_name from etudiants;

-- Récupérer l'étudiant dont l'id est égal à 2.
SELECT etudiant_fname, etudiant_name from etudiants WHERE id=2;

-- Récupérez l'élève dont le nom est Benichou ET le prénom est Marc.
SELECT etudiant_fname, etudiant_name from etudiants WHERE etudiant_fname LIKE '%Marc%' and etudiant_name LIKE '%Bénichou%';

-- Récupérez les étudiants dont les prénoms contiennent la lettre a .

SELECT etudiant_fname, etudiant_name from etudiants WHERE etudiant_fname LIKE '%a%';

-- Récupérez les étudiants dont le prénom commence par la lettre a .
SELECT etudiant_fname, etudiant_name from etudiants WHERE etudiant_fname LIKE 'a%';

-- Récupérer les étudiants dont les prénoms se terminent par la lettre a .
SELECT etudiant_fname, etudiant_name from etudiants WHERE etudiant_fname LIKE '%a';

-- Récupérer les étudiants dont l'avant-dernière lettre de leur prénom est a (Exemple : Le a h).
SELECT etudiant_fname, etudiant_name from etudiants WHERE etudiant_fname LIKE '%ah';



-- Récupérer les étudiants dont les identifiants sont égaux à 1 AND 3 .
SELECT etudiant_fname, etudiant_name from etudiants WHERE id=2 AND id=3;

-- Récupérez les étudiants dont la date de naissance est égale ou postérieure au 01/01/2000. (afficher toutes leurs informations).
SELECT * from etudiants WHERE age <= '01/01/2000';
