# CREATION DE LA BASE DE DONNEE 
# EXERCICE XP
import psycopg2

#CRETATION DE LA TABLE menu

#  CREATE TABLE menu(
#     id SERIAL NOT NULL,
#      nom VARCHAR(50) NOT NULL,
#      prix NUMERIC NOT NULL,
#      PRIMARY KEY(id)
#  )

HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = 'letmein'
DATABASE = 'dvdrental'

connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE )
cursor = connection.cursor()


class MenuItem:
    
    def __init__(self, id, nom, prix):
        self.id = id
        self.nom = nom
        self.prix = prix
        
    def save():
        pass

    def delete():
        pass

    def update():
        pass

    def all():
        pass
    
    def get_by_namequi(id):
        pass
    