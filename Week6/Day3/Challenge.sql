-- Exercice 1


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
