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










