-- Obtenez une liste de toutes les langues du film.
select *from language;

-- Obtenez une liste de tous les films joints avec leurs langues - sélectionnez les détails suivants : titre du film, description et nom de la langue. Essayez votre requête avec différentes jointures :

select film.title, film.description, language.name from film inner join language on language.language_id = film.language_id;
select film.title, film.description, language.name from film right outer join language on language.language_id = film.language_id;

-- Obtenez tous les films, même s'ils n'ont pas de langues.
select film.title, film.description, language.name from film join language on language.language_id = film.language_id;

-- Obtenez toutes les langues, même s'il n'y a pas de films dans ces langues.
select film.title, film.description, language.name from film right outer join language on language.language_id = film.language_id



