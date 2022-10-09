
-- 1 Créez une table appelée product_orderset une table appelée items. 
-- Vous décidez quels champs doivent figurer dans chaque tableau, 
-- mais assurez-vous que le itemstableau comporte une colonne appelée prix.

-- 2 Il doit y avoir une relation un à plusieurs entre la product_orderstable 
-- et la itemstable. Une commande peut contenir plusieurs articles,
--  mais un article ne peut appartenir qu'à une seule commande.

CREATE TABLE items(
   id SERIAL NOT NULL,
   nom VARCHAR(20) NOT NULL,
   prix NUMERIC NOT NULL,
   PRIMARY KEY(id)
);

  CREATE TABLE product_orders(
    id SERIAL NOT NULL,
    items_id INTEGER NOT NULL,
    num VARCHAR(20) NOT NULL UNIQUE,
    date_com date NOT NULL,
    PRIMARY KEY(id),
    CONSTRAINT fk_items FOREIGN KEY (items_id) REFERENCES items(id) ON DELETE CASCADE ON UPDATE CASCADE
 );


  CREATE TABLE users(
    id SERIAL NOT NULL,
    items_id INTEGER NOT NULL,
    num VARCHAR(20) NOT NULL UNIQUE,
    date_com date NOT NULL,
    PRIMARY KEY(id),
    CONSTRAINT fk_items FOREIGN KEY (items_id) REFERENCES items(id) ON DELETE CASCADE ON UPDATE CASCADE
 );

--INSERTION DE DONNEES DANA LA TABLE ARTICLE 

INSERT INTO items(nom, prix) VALUES('HP Envi', 900000), 
                                 ('HP Envi 2000', 1900000),
                                 ('Iphone 14', 950000),
                                 ('Iphone 13', 850000),
                                 ('Iphone 12', 750000)

--INSERTION DE DONNEES DANA LA TABLE COMMANDE

INSERT INTO product_orders(items_id, num, date_com) VALUES((SELECT id FROM items WHERE nom = 'Iphone 14'),'A001', NOW()),
                                             ((SELECT id FROM items WHERE nom = 'Iphone 14'),'A004', NOW()),
                                             ((SELECT id FROM items WHERE nom = 'Iphone 13'),'A002', NOW()),
                                             ((SELECT id FROM items WHERE nom = 'Iphone 13'),'A003', NOW()),
                                             ((SELECT id FROM items WHERE nom = 'Iphone 12'),'A005', NOW()),
                                             ((SELECT id FROM items WHERE nom = 'HP Envi 2000'),'A006', NOW()),
                                             ((SELECT id FROM items WHERE nom = 'HP Envi'),'A007', NOW()),
                                             ((SELECT id FROM items WHERE nom = 'ordinateur'),'A008', NOW()),
                                             ((SELECT id FROM items WHERE nom = 'souris'),'A009', NOW()),
                                             ((SELECT id FROM items WHERE nom = 'souris'),'A0010', NOW());
                                 


-- 3 Créez une fonction qui renvoie le prix total d'une commande donnée.



CREATE OR REPLACE FUNCTION prix_total(fn VARCHAR(50)) 
 RETURNS NUMERIC AS $prixtotal$
 BEGIN
    RETURN(SELECT SUM(items.prix) FROM items INNER JOIN product_orders ON items.id = product_orders.items_id WHERE product_orders.num = fn);
 END;
 $prixtotal$ LANGUAGE plpgsql;

 SELECT * FROM prix_total('A001');