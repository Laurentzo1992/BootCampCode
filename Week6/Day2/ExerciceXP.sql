-- Dans la base de données dvdrental, écrivez une requête pour sélectionner toutes les colonnes de la table « client ».
select * from customer;

-- Écrivez une requête pour afficher les noms ( first_name , last_name ) en utilisant un alias nommé « full_name ».

select (first_name, last_name) as full_name from customer;

-- Permet d'obtenir toutes les dates auxquelles les comptes ont été créés. Écrivez une requête pour sélectionner tous les create_date de la table « client » (il ne doit pas y avoir de doublons).

select distinct(create_date) from customer;

-- Écrivez une requête pour obtenir tous les détails du client à partir de la table des clients, elle doit être affichée dans l'ordre décroissant de leur prénom.

select * from customer order by first_name desc;

-- Rédigez une requête pour obtenir l'ID du film, le titre, la description, l'année de sortie et le tarif de location par ordre croissant en fonction de leur tarif de location

select film_id, title, description, release_year, replacement_cost from film order by replacement_cost asc;

-- Écrivez une requête pour obtenir l'adresse et le numéro de téléphone de tous les clients vivant dans le district du Texas, ces détails peuvent être trouvés dans le tableau "adresse".

select address.address, address.phone, address.district from address inner join customer on address.address_id = customer.address_id where district ='Texas';

-- Écrivez une requête pour récupérer tous les détails du film où l'identifiant du film est 15 ou 150.

select * from film where  film_id in (15,150);
select * from film where  film_id = 15 or film_id = 150;

-- Écrivez une requête qui devrait vérifier si votre film préféré existe dans la base de données. Demandez à votre requête d'obtenir l'ID du film, le titre, la description, la durée et le tarif de location, ces détails peuvent être trouvés dans le tableau "film".


select film_id, title, description, length, replacement_cost from film where  title = 'African Egg';

-- Pas de chance de trouver votre film ? Peut-être avez-vous fait une erreur dans l'orthographe du nom. Écrivez une requête pour obtenir l'ID du film, le titre, la description, la durée et le tarif de location de tous les films commençant par les deux premières lettres de votre film préféré.

select film_id, title, description, length, replacement_cost from film where  title like 'Af%';

-- Écrivez une requête qui trouvera les 10 films les moins chers.

select title, replacement_cost from film order by replacement_cost desc limit 10;

-- Pas satisfait des résultats. Écrivez une requête qui trouvera les 10 prochains films les moins chers.
-- Bonus : Essayez de ne pas utiliser LIMIT.

select title, replacement_cost from film order by replacement_cost desc limit 10;

-- Écrivez une requête qui joindra les données de la table des clients et de la table des paiements. Vous souhaitez obtenir le montant et la date de chaque paiement effectué par un client, classé par son identifiant (de 1 à…).

select (customer.first_name,customer.last_name) as customer_name, payment.amount, payment.payment_date from customer inner join payment on customer.customer_id = payment.customer_id order by payment.customer_id asc

-- Vous devez vérifier votre inventaire. Écrivez une requête pour obtenir tous les films qui ne sont pas dans l'inventaire.

select film.title, film.description from film inner join inventory on film.film_id = inventory.film_id
-- ou
SELECT title FROM film WHERE EXISTS (
SELECT * FROM inventory WHERE inventory.film_id = film.film_id
)

-- Rédigez une requête pour trouver quelle ville se trouve dans quel pays.
select country.country, city.city from country inner join city on country.country_id = city.country_id

-- Bonus Vous voulez être en mesure de voir comment vos vendeurs s'en sortent ? Écrivez une requête pour obtenir l'identifiant du client, ses noms (prénom et nom), le montant et la date de paiement commandé par l'identifiant du membre du personnel qui lui a vendu le dvd.

SELECT (customer.first_name, customer.last_name) as customer, payment.amount, (staff.first_name, staff.last_name) as vendeur FROM customer, payment, staff WHERE EXISTS (
SELECT * FROM payment, staff WHERE customer.customer_id = payment.customer_id and staff.staff_id = payment.staff_id
)
















