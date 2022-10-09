------------------------------------------------------------------------------------------
--Instruction De Sélection De Base
------------------------------------------------------------------------------------------


-- Écrivez une requête pour afficher les noms (prénom, nom) en utilisant un nom d'alias "Prénom", "Nom" de la table des employés.
SELECT first_name as Firstname, last_name as Lastname FROM employees;

-- Écrivez une requête pour obtenir un ID de service unique à partir de la table des employés (c'est-à-dire sans doublons).

SELECT DISTINCT(department_id) FROM employees;

--Écrivez une requête pour obtenir les détails de tous les employés de la table des employés, faites-le par ordre décroissant de prénom.

SELECT * FROM employees ORDER BY first_name DESC;

--Écrivez une requête pour obtenir les noms (prénom, nom), le salaire et 15 % du salaire en tant que PF (c'est-à-dire alias) pour tous les employés.

SELECT first_name as PRENOM, last_name as NOM, salary as SALAIRE, (salary*0.15) as PF FROM employees;

--Écrivez une requête pour obtenir les identifiants, les noms (prénom, nom) et le salaire des employés par ordre croissant en fonction de leur salaire.

SELECT employee_id, first_name as PRENOM, last_name as NOM, salary as SALAIRE FROM employees ORDER BY salary ASC;

--Écrivez une requête pour obtenir la somme totale de tous les salaires versés aux employés.

SELECT SUM(salary) as SALIRE_TOTAL FROM employees;

--Rédigez une requête pour obtenir les salaires maximum et minimum versés aux employés.

SELECT MAX(salary) AS SALAIRE_MAXIMAL, MIN(salary) as SALAIRE_MINIMAL FROM employees;

--Rédigez une requête pour obtenir le salaire moyen versé aux employés.

SELECT AVG(salary) as SALAIRE_MOYEN FROM employees;

--Rédigez une requête pour obtenir le nombre d'employés travaillant dans l'entreprise.

SELECT COUNT(employee_id) AS NOMBRE_TRAVAILLEUR FROM employees;

--Écrivez une requête pour obtenir tous les prénoms de la table des employés en majuscules.

SELECT UPPER(first_name) FROM employees;

--Écrivez une requête pour obtenir les trois premiers caractères de chaque prénom de tous les employés de la table des employés.

SELECT SUBSTRING(first_name for 3) FROM employees;

--Écrivez une requête pour obtenir les noms complets de tous les employés de la table des employés. Vous devez inclure le prénom et le nom de famille.

SELECT CONCAT(first_name, ' ', last_name) as IDENTITE FROM employees;

--Écrivez une requête pour obtenir le prénom, le nom et la longueur du nom complet de tous les employés de la table des employés.

SELECT first_name, last_name, CHAR_LENGTH(first_name)+CHAR_LENGTH(last_name) as LONGUEUR_NOM_COMPLET FROM employees;

--Écrivez une requête pour vérifier si la colonne first_name de la table des employés contient des nombres.

SELECT first_name FROM employees WHERE first_name ~ '^[0-9]$';

--Écrivez une requête pour sélectionner les dix premiers enregistrements d'une table.

SELECT * FROM employees LIMIT 10;

----------------------------------------------------------------------------------
--Restriction Et Tri
----------------------------------------------------------------------------------

--Rédigez une requête pour afficher le prénom, le nom et le salaire de tous les employés dont le salaire est compris entre 10 000 $ et 15 000 $.

SELECT first_name, last_name, salary FROM employees WHERE salary BETWEEN 10000 and 15000;

--Rédigez une requête pour afficher le prénom, le nom et la date d'embauche de tous les employés qui ont été embauchés en 1987.

SELECT first_name, last_name, hire_date FROM employees WHERE hire_date BETWEEN '1987-01-01' and '1987-12-31';

--Écrivez une requête pour obtenir tous les employés dont le prénom contient à la fois les lettres « c » et « e ».

SELECT * FROM employees WHERE first_name LIKE '%c%' AND first_name LIKE '%e%';

--Rédigez une requête pour afficher le nom, le poste et le salaire de tous les employés qui ne travaillent pas en tant que programmeurs ou commis à l'expédition et qui ne reçoivent pas un salaire égal à 4 500 $, 10 000 $ ou 15 000 $.

 SELECT employees.last_name, jobs.job_title, employees.salary 
 FROM employees JOIN jobs ON jobs.job_id = employees.job_id 
 WHERE jobs.job_id NOT IN (SELECT DISTINCT jobs.job_id
      FROM jobs
      WHERE jobs.job_title = 'Programmer'
    ) AND employees.salary NOT IN (4500, 10000, 15000);

--Écrivez une requête pour afficher les noms de famille de tous les employés dont le nom de famille contient exactement six caractères.

SELECT last_name FROM employees WHERE CHAR_LENGTH(last_name) = 6;

--Écrivez une requête pour afficher le nom de famille de tous les employés qui ont la lettre « e » comme troisième caractère dans le nom.

SELECT last_name FROM employees WHERE SUBSTRING(last_name FROM 3 for 1) LIKE '%e%';

--Écrivez une requête pour afficher le titre des emplois apparaissant dans la table des employés.

SELECT DISTINCT(jobs.job_title) FROM jobs JOIN employees ON jobs.job_id = employees.job_id;

--Écrivez une requête pour sélectionner toutes les informations des employés dont le nom de famille est 'JONES' ou 'BLAKE' ou 'SCOTT' ou 'KING' ou 'FORD'.

SELECT * FROM employees WHERE last_name IN ('JONES', 'BLAKE', 'SCOTT', 'KING', 'FORD')
