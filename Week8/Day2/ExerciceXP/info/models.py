from django.db import models

#model Animal
class Animal(models.Model):
	nom = models.CharField(null=False, max_length=200)
	pattes = models.IntegerField(null=False)
	poids = models.FloatField(null=False)
	taille = models.FloatField(null=False)
	vitesse  = models.FloatField(null=False)
	famille = models.ForeignKey('Famille', on_delete=models.CASCADE)


	def __str__(self):
		return self.nom

 	# def get_id(self,id):
 	# 	id = Animal.objects.get(famille)
 	# 	return self.id


#model Famille
class Famille(models.Model):
	nom_famille = models.CharField(null=False, max_length=200)

	def __str__(self):
		return self.nom_famille
# Create your models here.
