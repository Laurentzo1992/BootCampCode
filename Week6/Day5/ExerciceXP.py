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

    def database_querry(self,query):
        connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE )
        cursor = connection.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        connection.close()
        return results

    # 2    
    def save(self):
        query = f"INSERT INTO Menu (name, Prix) VALUES ('{self.nom}', {self.prix})"
        return self.database_querry(query)


    def delete_from_db(self):
        query=f"DELETE FROM Menu where name ='{self.nom}'"
        return self.database_querry(query)
        
    def update_db(self,ancien):
        query=f"UPDATE Menu SET name = '{self.nom}' WHERE name = '{ancien}'"
        self.database_querry(query)
        query =f"UPDATE Menu SET Prix = {self.prix} WHERE name = '{self.nom}'" 
        self.database_querry(query)

    # 3
    def all_(self):
        query=f'SELECT name,Prix FROM Menu'
        results = self.database_querry(query)
        print(list(results))
        return results

    # 4 
    def get_by_name(self,name):
        query=f'select name from Menu where name ="{name}" '
        results= self.database_querry(query)
        if len(results) < 1:
            print('Aucune correspondance')
        else:    
            print(list(results))
