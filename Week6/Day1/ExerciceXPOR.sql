-- Va chercher les quatre premiers élèves. Vous devez classer les quatre étudiants par ordre alphabétique de nom_de_famille.
SELECT * from etudiants ORDER BY etudiant_name ASC LIMIT 4;

-- Récupérez les coordonnées du plus jeune étudiant.
SELECT etudiant_fname, etudiant_name, MIN(YEAR(age)) from etudiants;


-- Allez chercher trois élèves en sautant les deux premiers élèves.
SELECT * from etudiants LIMIT 3 OFFSET 2;