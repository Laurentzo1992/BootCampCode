
-- 1 Créez une table appelée product_orderset une table appelée items. 
-- Vous décidez quels champs doivent figurer dans chaque tableau, 
-- mais assurez-vous que le itemstableau comporte une colonne appelée prix.

-- 2 Il doit y avoir une relation un à plusieurs entre la product_orderstable 
-- et la itemstable. Une commande peut contenir plusieurs articles,
--  mais un article ne peut appartenir qu'à une seule commande.

--CREATION DE DONNEES DANS LA TABLE ARTICLE 

CREATE TABLE items(
   id SERIAL NOT NULL,
   nom VARCHAR(20) NOT NULL,
   prix NUMERIC NOT NULL,
   PRIMARY KEY(id)
);

--CREATION DE DONNEES DANS LA TABLE COMMANDE 

  CREATE TABLE product_orders(
    id SERIAL NOT NULL,
    items_id INTEGER NOT NULL,
    num VARCHAR(20) NOT NULL UNIQUE,
    date_com date NOT NULL,
    PRIMARY KEY(id),
    CONSTRAINT fk_items FOREIGN KEY (items_id) REFERENCES items(id) ON DELETE CASCADE ON UPDATE CASCADE
 );


--CREATION DE DONNEES DANS LA TABLE USERS 

  CREATE TABLE users(
    id SERIAL NOT NULL,
    product_orders_id INTEGER NOT NULL,
    nom VARCHAR(50) NOT NULL,
    prenom VARCHAR(50) NOT NULL,
    PRIMARY KEY(id),
    CONSTRAINT fk_product_orders FOREIGN KEY (product_orders_id) REFERENCES product_orders(id) ON DELETE CASCADE ON UPDATE CASCADE
 );

--INSERTION DE DONNEES DANS LA TABLE ARTICLE 

INSERT INTO items(nom, prix) VALUES('HP Envi', 900000), 
                                 ('HP Envi 2000', 1900000),
                                 ('Iphone 14', 950000),
                                 ('Iphone 13', 850000),
                                 ('Iphone 12', 750000)


--INSERTION DE DONNEES DANS LA TABLE COMMANDE

INSERT INTO product_orders(items_id, nom, premon) VALUES((SELECT id FROM items WHERE nom = 'Iphone 14'),'A001', NOW()),
                                             ((SELECT id FROM items WHERE nom = 'Iphone 14'),'A004', NOW()),
                                             ((SELECT id FROM items WHERE nom = 'Iphone 13'),'A002', NOW()),
                                             ((SELECT id FROM items WHERE nom = 'Iphone 13'),'A003', NOW()),
                                             ((SELECT id FROM items WHERE nom = 'Iphone 12'),'A005', NOW()),
                                             ((SELECT id FROM items WHERE nom = 'HP Envi 2000'),'A006', NOW()),
                                             ((SELECT id FROM items WHERE nom = 'HP Envi'),'A007', NOW()),
                                             ((SELECT id FROM items WHERE nom = 'ordinateur'),'A008', NOW()),
                                             ((SELECT id FROM items WHERE nom = 'souris'),'A009', NOW()),
                                             ((SELECT id FROM items WHERE nom = 'souris'),'A0010', NOW());

--INSERTION DE DONNEES DANS LA TABLE USERS

INSERT INTO users(product_orders_id, nom, prenom) VALUES((SELECT id FROM product_orders WHERE num = 'A001'),'KABORE', 'Jules'),
                                             ((SELECT id FROM product_orders WHERE num = 'A001'),'SAWADOGO', 'Laure'),
                                             ((SELECT id FROM product_orders WHERE num = 'A001'),'SANKARA', 'Henry'),
                                             ((SELECT id FROM product_orders WHERE num = 'A002'),'KOFFI', 'Ines'),
                                             ((SELECT id FROM product_orders WHERE num = 'A002'),'YAO', 'Armelle'),
                                             ((SELECT id FROM product_orders WHERE num = 'A002'),'KIPRE', 'Anaatasi'),
                                             ((SELECT id FROM product_orders WHERE num = 'A006'),'KINDA', 'Alice'),
                                             ((SELECT id FROM product_orders WHERE num = 'A006'),'TRAORE', 'Madi'),
                                             ((SELECT id FROM product_orders WHERE num = 'A006'),'DAMIBA', 'Paul'),
                                             ((SELECT id FROM product_orders WHERE num = 'A006'),'ZONGO', 'Emil');
                              



-- 3 Créez une fonction qui renvoie le prix total d'une commande donnée.


CREATE OR REPLACE FUNCTION prix_total(fn VARCHAR(50)) 
 RETURNS NUMERIC AS $prixtotal$
 BEGIN
    RETURN(SELECT SUM(items.prix) FROM items INNER JOIN product_orders ON items.id = product_orders.items_id WHERE product_orders.num = fn);
 END;
 $prixtotal$ LANGUAGE plpgsql;

 SELECT * FROM prix_total('A001');

--Bonus :
-- Créez une table appelée users.
-- Il doit y avoir une relation un à plusieurs entre la userstable et la product_orderstable.
-- Créez une fonction qui renvoie le prix total pour une commande donnée d'un utilisateur donné.

CREATE OR REPLACE FUNCTION prix_total1(fn VARCHAR(50), lan VARCHAR(50)) 
 RETURNS NUMERIC AS $prixtotal$
 BEGIN
    RETURN(SELECT SUM(items.prix) FROM items INNER JOIN product_orders ON items.id = product_orders.items_id WHERE product_orders.num = fn AND product_orders.num = lan);
 END;
 $prixtotal$ LANGUAGE plpgsql;

 SELECT * FROM prix_total1('SANKARA', 'Henry');
 