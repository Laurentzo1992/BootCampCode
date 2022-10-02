-- Exercice 1

-- Obtenez une liste de toutes les langues du film.
select *from language;

-- Obtenez une liste de tous les films joints avec leurs langues - sélectionnez les détails suivants : titre du film, description et nom de la langue. Essayez votre requête avec différentes jointures :

select film.title, film.description, language.name from film inner join language on language.language_id = film.language_id;
select film.title, film.description, language.name from film right outer join language on language.language_id = film.language_id;

-- Obtenez tous les films, même s'ils n'ont pas de langues.
select film.title, film.description, language.name from film join language on language.language_id = film.language_id;

-- Obtenez toutes les langues, même s'il n'y a pas de films dans ces langues.
select film.title, film.description, language.name from film right outer join language on language.language_id = film.language_id


CREATE TABLE new_film(
  id SERIAL, 
  name VARCHAR(45) NOT NULL,
  PRIMARY KEY (id)

insert into new_film(name) VALUES('rambo'), ('terminator'), ('terminator2'), ('terminator3'), ('terminator4')

CREATE TABLE customer_review (
  review_id SERIAL,
  film_id INTEGER NOT NULL,
  language_id INTEGER NOT NULL,
  titre  VARCHAR(45) NOT NULL, 
  note VARCHAR(45) NOT NULL,
  review_text TEXT NOT NULL,
  last_update date NOT NULL,
  PRIMARY KEY (review_id),
  FOREIGN KEY (film_id) REFERENCES new_film(id) ON DELETE CASCADE
);

insert into customer_review(film_id, language_id, titre, note, review_text, last_update) VALUES(1, 1, 'mauvais film', 2, 'veuillez revoir le tournage', '02-10-2022'), (1, 1, 'mauvais film', 2, 'veuillez revoir le tournage', '02-10-2022'),(1, 1, 'mauvais film', 2, 'veuillez revoir le tournage', '02-10-2022'),(1, 1, 'mauvais film', 2, 'veuillez revoir le tournage', '02-10-2022')

  delete from new_film where name = 'rambo';
  -- toute les données liées ont été suprimé

  --xercice 2

  -- Utilisez UPDATE pour changer la langue de certains films. Assurez-vous d'utiliser des langues valides.

  UPDATE language set name ='moore' where language_id = 5;
  UPDATE language set name ='dioula' where language_id = 3;
  UPDATE language set name ='san' where language_id = 6;

  -- Quelles clés étrangères (références) sont définies pour la table client ? Comment cela affecte-t-il la manière dont nous INSÉRONS dans la table client ?

  --store_id, address_id 

  -- Nous avons créé une nouvelle table appelée customer_review . Déposez ce tableau. Est-ce une étape facile ou nécessite-t-elle une vérification supplémentaire ?

  -- Découvrez combien de locations sont encore en suspens (c'est-à-dire qu'elles n'ont pas encore été retournées au magasin).

  



